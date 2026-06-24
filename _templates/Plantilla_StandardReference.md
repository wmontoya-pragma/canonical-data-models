---
# ============================================================
# Plantilla_StandardReference.md — V2
# ============================================================
# Ficha de un componente de estándar externo (ISO 20022 o BIAN)
# tal cual, SIN modificaciones del banco. Vive en
# _canonical-standards/{iso20022|bian}/. Es solo de lectura:
# el contenido se "vendoriza" desde la fuente oficial, no se edita
# a mano para reflejar reglas propias del banco (eso va en BC/MC/MD
# con standard_alignment_strategy: mapping o gap-fit).

id: "STD-{{iso20022|bian}}-{{nombre}}"
name: "{{Nombre oficial del componente en el estándar}}"
type: "standard-reference"
standard: "iso20022"          # iso20022 | bian
standard_version: "{{ej: 2019, o release de BIAN}}"
status: "active"               # active | superseded

# Origen exacto en la fuente oficial, para trazabilidad de vendorización
source_url: "{{URL o referencia al documento oficial}}"
vendorized_date: "{{YYYY-MM-DD}}"

ai_keywords: []
aliases: []
---

# {{Nombre oficial del componente en el estándar}}

## Definición oficial

{{Copiar/traducir fielmente la definición del estándar — sin adaptaciones del banco.}}

## Estructura oficial

| Campo | Tipo | Obligatorio (estándar) | Descripción oficial |
|---|---|---|---|
| `{{campo1}}` | `{{tipo}}` | Sí/No | {{descripción tal cual el estándar}} |

## Usado como referencia por

> Lista de BC/MC/MD/CS del repositorio que declaran
> `standard_reference` apuntando a este documento.

| Componente | Estrategia declarada |
|---|---|
| {{BC-XXX}} | {{reference / mapping / gap-fit}} |

## Notas de vendorización

- **Versión del estándar fichada**: {{versión}}
- **Diferencias conocidas con versiones más nuevas del estándar** (si aplica): {{nota}}

## Checklist de publicación

- [ ] El contenido es fiel al estándar oficial, sin adaptaciones del banco.
- [ ] `source_url` y `vendorized_date` completos.
- [ ] No contiene reglas de negocio propias del banco (eso va en el BC/MC que referencia este documento).
