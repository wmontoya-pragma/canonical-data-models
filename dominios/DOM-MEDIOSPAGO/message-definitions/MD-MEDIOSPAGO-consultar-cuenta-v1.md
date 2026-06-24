---
id: "MD-MEDIOSPAGO-consultar-cuenta-v1"
name: "Consultar Cuenta"
type: "message-definition"
domain_id: "DOM-MEDIOSPAGO"
status: "active"
version: "1.0.0"

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

assembled_fragment_file: "MD-MEDIOSPAGO-consultar-cuenta-v1.fragment.yml"

composed_from:
  - component_id: "MC-MEDIOSPAGO-identificacion-cuenta-v1"
    branch_consumed: "v1"
  - component_id: "MC-MEDIOSPAGO-saldos-cuenta-v1"
    branch_consumed: "v1"

published_in_oas:
  - domain_id: "DOM-MEDIOSPAGO"
    branch: "v1"
    operation: "GET /accounts/{id}"

ai_keywords: ["consultar", "cuenta", "saldo", "identificacion", "get"]
aliases: []

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Consultar Cuenta

## Descripcion funcional

Respuesta del endpoint `GET /accounts/{id}`: combina la identificacion de
la cuenta con sus saldos actuales en un solo mensaje de respuesta.

## Composed from

| Message Component | Rama consumida | Rol en el mensaje |
|---|---|---|
| MC-MEDIOSPAGO-identificacion-cuenta-v1 | v1 | Cuerpo principal: identificacion de la cuenta |
| MC-MEDIOSPAGO-saldos-cuenta-v1 | v1 | Sub-objeto `balances`: saldos de la cuenta |

## Envelope structure

| Campo | Tipo | Obligatorio | Descripcion |
|---|---|---|---|
| `account` | MC-identificacion-cuenta-v1 | Si | Identificacion de la cuenta |
| `balances` | MC-saldos-cuenta-v1 | Si | Saldos de la cuenta |

## Used in OAS operations

| Dominio | Rama | Operacion | Tipo |
|---|---|---|---|
| DOM-MEDIOSPAGO | v1 | `GET /accounts/{id}` | response |

## Machine-readable summary

```yaml
id: "MD-MEDIOSPAGO-consultar-cuenta-v1"
domain_id: "DOM-MEDIOSPAGO"
composed_from: ["MC-MEDIOSPAGO-identificacion-cuenta-v1", "MC-MEDIOSPAGO-saldos-cuenta-v1"]
published_in_oas: ["DOM-MEDIOSPAGO/v1/GET /accounts/{id}"]
ai_keywords: ["consultar", "cuenta", "saldo", "identificacion", "get"]
```

## Checklist de publicacion

- [x] Tabla "Composed from" completa con rama consumida de cada MC.
- [x] Envelope structure documentada (agrega `account`/`balances` como wrappers).
- [x] Tabla "Used in OAS operations" actualizada.
- [ ] `assembled_fragment_file` pendiente de generar por el build real.
- [ ] Aprobado por comite (PoC: pendiente, comite no formalizado aun).
