---
# ============================================================
# Plantilla_BC_Generica.md — V2
# ============================================================
# Front matter obligatorio para todo Business Component (BC).
# Reemplazar todos los valores {{...}} antes de publicar.
# No eliminar campos: si no aplica, dejar el valor por defecto indicado.

id: "BC-{{dominio}}-{{nombre}}-v{{MAJOR}}"
name: "{{Nombre legible del Business Component}}"
type: "business-component"
domain_id: "DOM-{{DOMINIO}}"
status: "draft"              # draft | active | deprecated | sunset
version: "{{MAJOR}}.{{MINOR}}.{{PATCH}}"

# --- Origen / fuente (V2) ---
source: "custom"              # custom | iso20022 | bian
standard_alignment_strategy: "n/a"   # n/a | reference | mapping | gap-fit
standard_reference: null      # id del documento en _canonical-standards/ si source != custom

# --- Estrategia de rama MAJOR (V2) ---
major_branch_strategy: "n/a"  # n/a | evolution | fork
branch_lineage: []            # lista de ids de los que desciende, si es Fork

# --- Gobierno ---
owner_team_id_override: null  # null = hereda owner_team_id del dominio; o "TEAM-XXX" si este componente tiene dueño distinto

# --- Modelo de archivos (V2) ---
individual_oas_file: "BC-{{dominio}}-{{nombre}}-v{{MAJOR}}.yaml"   # yaml hermano, mismo nombre base que este .md
oas_schema_ref: "#/components/schemas/{{NombreSchema}}"

# --- Descubribilidad para IA (RAG + MCP) ---
ai_keywords: []
aliases: []

created_date: "{{YYYY-MM-DD}}"
updated_date: "{{YYYY-MM-DD}}"
---

# {{Nombre legible del Business Component}}

## Descripción funcional

{{Qué representa este Business Component en el negocio, en lenguaje no técnico.}}

## Atributos

| Atributo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `{{atributo1}}` | `{{tipo}}` | Sí/No | {{descripción}} |

## Standard alignment

> Completar solo si `source != custom`.

- **Estrategia**: {{reference / mapping / gap-fit}}
- **Referencia al estándar**: {{link o id en _canonical-standards/}}
- **Justificación de gap-fit** (si aplica): {{por qué el estándar no cubre el caso de uso}}

## Reglas de negocio

- {{Regla 1}}

## Relaciones

| Tipo de relación | Componente |
|---|---|
| Usado por (MC) | {{MC-XXX}} |

## Branch lineage (si es Fork)

> Completar solo si `major_branch_strategy: fork`.

| Versión | Tipo de rama | Heredado de | Owner |
|---|---|---|---|
| v1 | trunk | — | {{TEAM-XXX}} |
| v2 | fork | v1 | {{TEAM-YYY}} |

## Machine-readable summary

```yaml
id: "BC-{{dominio}}-{{nombre}}-v{{MAJOR}}"
domain_id: "DOM-{{DOMINIO}}"
consumed_by: []
ai_keywords: []
```

## Checklist de publicación

- [ ] El yaml individual (`individual_oas_file`) existe y coincide en nombre base con este `.md`.
- [ ] `source` y, si aplica, `standard_alignment_strategy`/`standard_reference` completos.
- [ ] `owner_team_id_override` correcto (o explícitamente `null` si hereda del dominio).
- [ ] `catalog.yaml` actualizado con esta entrada.
- [ ] Si es Fork: `branch_lineage` completo y tabla de branch lineage llena.
