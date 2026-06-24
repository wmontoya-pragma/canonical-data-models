---
# ============================================================
# Plantilla_MessageDefinition.md — V2
# ============================================================
# Front matter obligatorio para todo Message Definition (MD).
# Un MD representa el mensaje final (request/response/evento) que
# se ENSAMBLA a partir de uno o más MC, y es lo que efectivamente
# se publica dentro de un OAS de dominio.

id: "MD-{{dominio}}-{{nombre}}-v{{MAJOR}}"
name: "{{Nombre legible del Message Definition}}"
type: "message-definition"
domain_id: "DOM-{{DOMINIO}}"
status: "draft"
version: "{{MAJOR}}.{{MINOR}}.{{PATCH}}"

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

# --- Modelo de archivos (V2) ---
# El MD no tiene yaml "individual" como BC/MC; tiene un FRAGMENTO
# que el pipeline de build ensambla dentro del OAS final del dominio.
assembled_fragment_file: "MD-{{dominio}}-{{nombre}}-v{{MAJOR}}.fragment.yaml"

# --- Composición: de qué MC(s) se construye este MD ---
composed_from:
  - component_id: "MC-{{dominio}}-{{nombre}}"
    branch_consumed: "v{{MAJOR}}"

# --- Dónde termina publicado ---
published_in_oas:
  - domain_id: "DOM-{{DOMINIO}}"
    branch: "v{{MAJOR}}"
    operation: "{{METHOD}} {{/path}}"

ai_keywords: []
aliases: []

created_date: "{{YYYY-MM-DD}}"
updated_date: "{{YYYY-MM-DD}}"
---

# {{Nombre legible del Message Definition}}

## Descripción funcional

{{Qué representa este mensaje: request, response o evento, y en qué flujo de negocio se usa.}}

## Composed from

| Message Component | Rama consumida | Rol en el mensaje |
|---|---|---|
| {{MC-XXX}} | v{{X}} | {{ej: cuerpo principal, sub-objeto "deudor", etc.}} |

## Envelope structure

> Documentar solo si el MD agrega campos propios FUERA de los MC que compone
> (ej. metadata de transacción, paginación, headers de negocio).

| Campo | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `{{campo_envelope}}` | `{{tipo}}` | Sí/No | {{descripción}} |

## Used in OAS operations

| Dominio | Rama | Operación | Tipo |
|---|---|---|---|
| {{DOM-XXX}} | v{{X}} | `{{METHOD}} {{/path}}` | request / response / evento |

## Branch lineage (si es Fork)

| Versión | Tipo de rama | Heredado de | Owner |
|---|---|---|---|
| v1 | trunk | — | {{TEAM-XXX}} |

## Machine-readable summary

```yaml
id: "MD-{{dominio}}-{{nombre}}-v{{MAJOR}}"
domain_id: "DOM-{{DOMINIO}}"
composed_from: []
published_in_oas: []
ai_keywords: []
```

## Checklist de publicación

- [ ] Tabla "Composed from" completa con rama consumida de cada MC.
- [ ] Envelope structure documentada si el MD agrega campos propios fuera de los MCs.
- [ ] Tabla "Used in OAS operations" actualizada con todas las operaciones reales.
- [ ] `assembled_fragment_file` coincide con el nombre real del yaml generado por el build.
- [ ] `published_in_oas` actualizado con todos los OAS/ramas donde efectivamente termina este MD.
- [ ] Si Fork: `branch_lineage` completo.
- [ ] Aprobado por comité y referenciado desde el documento de dominio.
