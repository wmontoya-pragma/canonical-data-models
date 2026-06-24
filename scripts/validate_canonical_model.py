#!/usr/bin/env python3
"""
validate_canonical_model.py — V2

Valida, sobre todos los .md de dominios/**, las reglas de composicion
del modelo canonico:

  MD  -> puede referenciar: MC (1+), DataType (1+)
  MC  -> puede referenciar: MC (1+), BC (1+), DataType (1+)
  BC  -> puede referenciar: BC (1+), DataType (1+), y/o StandardReference (ISO/BIAN)

Y las reglas de alineacion a estandar para BC/MC/CS con source != custom:
  standard_alignment_strategy debe ser uno de: reference | mapping | gap-fit
  y debe declarar standard_reference (excepto reference, que es opcional
  por ser solo inspiracion conceptual).

Tambien valida:
  - Convencion sibling: cada BC/MC/CS .md tiene su .yaml individual
    hermano (individual_oas_file existe en la misma carpeta).
  - El yaml individual no debe estar envuelto en components/schemas
    (debe ser un Schema Object "pelado" en la raiz).

Uso:
  python3 validate_canonical_model.py [--root .]

Exit code 0 si todo es valido, 1 si hay errores (para uso en CI).
"""

import argparse
import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: falta PyYAML. Instalar con: pip install pyyaml")
    sys.exit(2)

# Prefijos validos por tipo de componente, segun id (ej. "BC-...", "MC-...")
PREFIX_TO_TYPE = {
    "BC": "business-component",
    "MC": "message-component",
    "MD": "message-definition",
    "CS": "code-set",
    "DT": "datatype",
    "STD": "standard-reference",
}

# Reglas de composicion V2 (actualizadas):
#   MD  -> MC (1+), DataType (1+)
#   MC  -> MC (1+) y/o BC (0+, OPCIONAL), DataType (1+), CodeSet (1+, prioridad
#          de referencia directa MC->CodeSet sobre pasar por un BC)
#   BC  -> BC (1+), DataType (1+), CodeSet (1+), y/o StandardReference (ISO/BIAN)
ALLOWED_REFERENCES = {
    "message-definition": {"message-component", "datatype"},
    "message-component": {"message-component", "business-component", "datatype", "code-set"},
    "business-component": {"business-component", "datatype", "code-set", "standard-reference"},
}

# Para message-component, business-component ya NO es obligatorio (regla V2
# relajada): un MC puede componerse solo de MC/DataType/CodeSet sin BC.
OPTIONAL_REFERENCE_TYPES = {
    "message-component": {"business-component"},
}

VALID_ALIGNMENT_STRATEGIES = {"n/a", "reference", "mapping", "gap-fit"}


def extract_front_matter(md_path: Path):
    """Extrae el front matter YAML (entre --- ... ---) de un .md."""
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        return {"__parse_error__": str(e)}


def component_type_from_id(component_id: str):
    prefix = component_id.split("-")[0]
    return PREFIX_TO_TYPE.get(prefix)


def find_component_files(root: Path):
    """Encuentra todos los .md de componentes bajo dominios/, _canonical-standards/ y _datatypes/."""
    paths = []
    for pattern in ["dominios/**/*.md", "_canonical-standards/**/*.md", "_datatypes/**/*.md"]:
        paths.extend(root.glob(pattern))
    # Excluir READMEs y archivos que no son componentes (sin front matter "id")
    return paths


def validate_composition_rules(fm: dict, md_path: Path, errors: list):
    """Valida que composed_from solo referencie tipos permitidos para este tipo de componente."""
    own_type = fm.get("type")
    if own_type not in ALLOWED_REFERENCES:
        return  # tipos sin reglas de composicion (ej. standard-reference, code-set simple)

    composed_from = fm.get("composed_from") or []
    allowed = ALLOWED_REFERENCES[own_type]

    for entry in composed_from:
        ref_id = entry.get("component_id", "") if isinstance(entry, dict) else str(entry)
        ref_type = component_type_from_id(ref_id)
        if ref_type is None:
            errors.append(f"{md_path}: composed_from referencia '{ref_id}' con prefijo de id no reconocido.")
            continue
        if ref_type not in allowed:
            errors.append(
                f"{md_path}: tipo '{own_type}' no puede referenciar tipo '{ref_type}' "
                f"(componente '{ref_id}'). Permitidos para {own_type}: {sorted(allowed)}."
            )


def validate_standard_alignment(fm: dict, md_path: Path, errors: list):
    """Valida coherencia de source / standard_alignment_strategy / standard_reference."""
    source = fm.get("source")
    if source is None:
        return  # tipos sin este campo (MD, standard-reference, etc.)

    strategy = fm.get("standard_alignment_strategy", "n/a")
    if strategy not in VALID_ALIGNMENT_STRATEGIES:
        errors.append(
            f"{md_path}: standard_alignment_strategy='{strategy}' invalida. "
            f"Debe ser una de: {sorted(VALID_ALIGNMENT_STRATEGIES)}."
        )

    if source != "custom" and strategy == "n/a":
        errors.append(
            f"{md_path}: source='{source}' (no custom) pero standard_alignment_strategy='n/a'. "
            f"Debe declarar reference, mapping o gap-fit."
        )

    if strategy in ("mapping", "gap-fit") and not fm.get("standard_reference"):
        errors.append(
            f"{md_path}: standard_alignment_strategy='{strategy}' requiere 'standard_reference' "
            f"apuntando a un documento en _canonical-standards/."
        )


def validate_sibling_yaml(fm: dict, md_path: Path, errors: list, warnings: list):
    """Valida la convencion sibling .md + .yaml, y que el yaml no este envuelto en components/schemas."""
    individual_oas_file = fm.get("individual_oas_file")
    if not individual_oas_file:
        return  # MD y otros tipos no usan este campo

    yaml_path = md_path.parent / individual_oas_file
    if not yaml_path.exists():
        errors.append(f"{md_path}: individual_oas_file='{individual_oas_file}' no existe en {md_path.parent}.")
        return

    try:
        yaml_content = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        errors.append(f"{yaml_path}: error de parseo YAML: {e}")
        return

    if isinstance(yaml_content, dict) and "components" in yaml_content:
        errors.append(
            f"{yaml_path}: el yaml individual NO debe estar envuelto en 'components: schemas: ...'. "
            f"Debe ser un Schema Object pelado en la raiz (type, properties, etc.)."
        )

    if isinstance(yaml_content, dict) and "type" not in yaml_content:
        warnings.append(f"{yaml_path}: no se encontro la clave 'type' en la raiz; verificar que sea un Schema Object valido.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Raiz del repositorio")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = []
    warnings = []
    checked = 0

    for md_path in find_component_files(root):
        fm = extract_front_matter(md_path)
        if fm is None:
            continue  # no es un componente (sin front matter), ej. un README
        if "__parse_error__" in fm:
            errors.append(f"{md_path}: front matter YAML invalido: {fm['__parse_error__']}")
            continue
        if "id" not in fm:
            continue  # documento sin id, no es un artefacto canonico (ej. plantilla)

        checked += 1
        validate_composition_rules(fm, md_path, errors)
        validate_standard_alignment(fm, md_path, errors)
        validate_sibling_yaml(fm, md_path, errors, warnings)

    print(f"Componentes verificados: {checked}")

    if warnings:
        print(f"\n⚠ Advertencias ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n✗ Errores ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\n✓ Todas las reglas de composicion y alineacion a estandar son validas.")
    sys.exit(0)


if __name__ == "__main__":
    main()
