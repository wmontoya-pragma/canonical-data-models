---
# ============================================================
# Plantilla_MessageComponent.md — V2
# ============================================================
# Front matter obligatorio para todo Message Component (MC).
# Reemplazar todos los valores {{...}} antes de publicar.

id: "MC-{{dominio}}-{{nombre}}-v{{MAJOR}}"
name: "{{Nombre legible del Message Component}}"
type: "message-component"
domain_id: "DOM-{{DOMINIO}}"
status: "draft"
version: "{{MAJOR}}.{{MINOR}}.{{PATCH}}"

# --- Origen / fuente (V2) ---
source: "custom"
standard_alignment_strategy: "n/a"
standard_reference: null

# --- Estrategia de rama MAJOR (V2) ---
major_branch_strategy: "n/a"
branch_lineage: []

# --- Gobierno ---
owner_team_id_override: null

# --- Modelo de archivos (V2) ---
individual_oas_file: "MC-{{dominio}}-{{nombre}}-v{{MAJOR}}.yaml"
oas_schema_ref: "#/components/schemas/{{NombreSchema}}"

# --- Composición: de qué BC(s) se construye este MC ---
composed_from:
  - component_id: "BC-{{dominio}}-{{nombre}}"
    branch_consumed: "v{{MAJOR}}"   # rama EXACTA del BC que este MC consume

ai_keywords: []
aliases: []

created_date: "{{YYYY-MM-DD}}"
updated_date: "{{YYYY-MM-DD}}"
---

# {{Nombre legible del Message Component}}

## Descripción funcional

{{Qué representa este Message Component y en qué tipo de mensajes aparece.}}

## Composed from

| Business Component | Rama consumida | Campos reutilizados |
|---|---|---|
| {{BC-XXX}} | v{{X}} | {{todos / subset}} |

## Estructura

| Campo | Tipo | Obligatorio | Origen (BC / propio) | Descripción |
|---|---|---|---|---|
| `{{campo1}}` | `{{tipo}}` | Sí/No | {{BC-XXX / propio}} | {{descripción}} |

## Standard alignment

> Completar solo si `source != custom`.

- **Estrategia**: {{reference / mapping / gap-fit}}
- **Referencia al estándar**: {{link o id en _canonical-standards/}}

## Relaciones

| Tipo de relación | Componente |
|---|---|
| Usado por (MD) | {{MD-XXX}} |

## Branch lineage (si es Fork)

| Versión | Tipo de rama | Heredado de | Owner |
|---|---|---|---|
| v1 | trunk | — | {{TEAM-XXX}} |

## Machine-readable summary

```yaml
id: "MC-{{dominio}}-{{nombre}}-v{{MAJOR}}"
domain_id: "DOM-{{DOMINIO}}"
composed_from: []
consumed_by: []
ai_keywords: []
```

## Checklist de publicación

- [ ] El yaml individual existe y coincide en nombre base con este `.md`.
- [ ] Tabla "Composed from" completa, con rama EXACTA consumida de cada BC.
- [ ] `source`/`standard_alignment_strategy` completos si aplica.
- [ ] `owner_team_id_override` correcto.
- [ ] `catalog.yaml` actualizado.
