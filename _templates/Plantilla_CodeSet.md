---
# ============================================================
# Plantilla_CodeSet.md — V2
# ============================================================
# Front matter obligatorio para todo Code-set (lista de valores controlados).

id: "CS-{{dominio}}-{{nombre}}-v{{MAJOR}}"
name: "{{Nombre legible del Code-set}}"
type: "code-set"
domain_id: "DOM-{{DOMINIO}}"     # o "_codesets" si es transversal a varios dominios
status: "draft"
version: "{{MAJOR}}.{{MINOR}}.{{PATCH}}"

# --- Origen / fuente (V2) ---
source: "custom"
standard_alignment_strategy: "n/a"
standard_reference: null

# --- Estrategia de rama MAJOR (V2) ---
# Caso típico de Fork en Code-sets: "lista completa del estándar" (trunk)
# vs. "subconjunto operativo habilitado por el banco" (fork).
major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "CS-{{dominio}}-{{nombre}}-v{{MAJOR}}.yaml"
oas_schema_ref: "#/components/schemas/{{NombreSchema}}"

ai_keywords: []
aliases: []

created_date: "{{YYYY-MM-DD}}"
updated_date: "{{YYYY-MM-DD}}"
---

# {{Nombre legible del Code-set}}

## Descripción funcional

{{Qué representa esta lista de valores y dónde se usa.}}

## Valores

| Código | Etiqueta | Descripción | Vigente |
|---|---|---|---|
| `{{CODE1}}` | {{Etiqueta}} | {{descripción}} | Sí/No |

## Standard alignment

> Completar solo si `source != custom`.

- **Estrategia**: {{reference / mapping / gap-fit}}
- **Referencia al estándar**: {{link o id en _canonical-standards/}}
- **Subconjunto vs. estándar completo** (si aplica): {{ej: "el estándar ISO tiene 40 códigos, el banco habilita 12"}}

## Relaciones

| Tipo de relación | Componente |
|---|---|
| Usado por | {{BC-XXX / MC-XXX}} |

## Branch lineage (si es Fork)

| Versión | Tipo de rama | Heredado de | Owner | Alcance |
|---|---|---|---|---|
| v1 | trunk | — | {{TEAM-XXX}} | Lista completa del estándar |
| v2 | fork | v1 | {{TEAM-YYY}} | Subconjunto operativo del banco |

## Machine-readable summary

```yaml
id: "CS-{{dominio}}-{{nombre}}-v{{MAJOR}}"
domain_id: "DOM-{{DOMINIO}}"
consumed_by: []
ai_keywords: []
```

## Checklist de publicación

- [ ] El yaml individual existe y coincide en nombre base con este `.md`.
- [ ] Todos los códigos vigentes documentados, con los obsoletos marcados `Vigente: No` (no eliminados).
- [ ] `source`/`standard_alignment_strategy` completos si aplica.
- [ ] `owner_team_id_override` correcto.
- [ ] `catalog.yaml` actualizado.
