---
id: "MC-MEDIOSPAGO-identificacion-cuenta-v1"
name: "Identificacion de Cuenta (mensaje)"
type: "message-component"
domain_id: "DOM-MEDIOSPAGO"
status: "active"
version: "1.0.0"

source: "custom"
standard_alignment_strategy: "n/a"
standard_reference: null

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "MC-MEDIOSPAGO-identificacion-cuenta-v1.yml"
oas_schema_ref: "#/components/schemas/MC-MEDIOSPAGO-identificacion-cuenta-v1"

composed_from:
  - component_id: "BC-MEDIOSPAGO-cuenta-identificacion-v1"
    branch_consumed: "v1"

ai_keywords: ["cuenta", "identificacion", "mensaje", "consulta"]
aliases: []

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Identificacion de Cuenta (mensaje)

## Descripcion funcional

Envuelve `BC-MEDIOSPAGO-cuenta-identificacion-v1` para su exposicion como
parte de un mensaje de respuesta de consulta de cuenta. Pass-through 1 a 1
del BC, sin campos adicionales propios del mensaje.

## Composed from

| Business Component | Rama consumida | Campos reutilizados |
|---|---|---|
| BC-MEDIOSPAGO-cuenta-identificacion-v1 | v1 | todos |

## Estructura

| Campo | Tipo | Obligatorio | Origen | Descripcion |
|---|---|---|---|---|
| `identification` | DT-texto-max35-v1 | Si | BC | Numero de cuenta o IBAN |
| `type` | string (enum) | Si | BC | Tipo de cuenta |
| `currency` | CS-codigo-moneda-v1 | Si | BC | Moneda |
| `status` | string (enum) | No | BC | Estado del contrato |

## Standard alignment

No aplica — `source: custom` (composicion propia del mensaje).

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (MD) | MD-MEDIOSPAGO-consultar-cuenta-v1 |

## Machine-readable summary

```yaml
id: "MC-MEDIOSPAGO-identificacion-cuenta-v1"
domain_id: "DOM-MEDIOSPAGO"
composed_from: ["BC-MEDIOSPAGO-cuenta-identificacion-v1"]
consumed_by: ["MD-MEDIOSPAGO-consultar-cuenta-v1"]
ai_keywords: ["cuenta", "identificacion", "mensaje", "consulta"]
```

## Checklist de publicacion

- [x] El yaml individual existe y coincide en nombre base.
- [x] Tabla "Composed from" completa, con rama EXACTA consumida del BC.
- [x] `owner_team_id_override` correcto.
- [ ] `catalog.yaml` actualizado.
