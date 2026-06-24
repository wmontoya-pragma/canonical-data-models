---
id: "BC-MEDIOSPAGO-cuenta-identificacion-v2"
name: "Identificacion de Cuenta"
type: "business-component"
domain_id: "DOM-MEDIOSPAGO"
status: "active"
version: "2.0.0"

source: "bian"
standard_alignment_strategy: "gap-fit"
standard_reference: "STD-bian-current-accounts"

major_branch_strategy: "evolution"
branch_lineage: ["BC-MEDIOSPAGO-cuenta-identificacion-v1"]

owner_team_id_override: null

individual_oas_file: "BC-MEDIOSPAGO-cuenta-identificacion-v2.yml"
oas_schema_ref: "#/components/schemas/BC-MEDIOSPAGO-cuenta-identificacion-v2"

ai_keywords: ["cuenta", "identificacion", "account", "open banking", "alias"]
aliases: ["AccountIdentification v2"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Identificacion de Cuenta (v2)

## Descripcion funcional

Evolucion de v1: agrega `accountNickname`, un alias personalizado que el
cliente asigna a su cuenta desde canales digitales (Open Banking / App
movil). Extension del banco sobre el estandar BIAN/ISO base.

## Atributos

| Atributo | Tipo | Obligatorio | Descripcion |
|---|---|---|---|
| `identification` | DT-texto-max35-v1 | Si | Numero de cuenta contractual o IBAN |
| `type` | string (enum: CACC, SVGS, COMM, ONLD) | Si | Tipo de cuenta |
| `currency` | CS-codigo-moneda-v1 | Si | Moneda de la cuenta |
| `accountNickname` | DT-texto-max35-v1 | Si (nuevo en v2) | Alias personalizado asignado por el cliente |

## Standard alignment

- **Estrategia**: gap-fit — base 1 a 1 con el estandar; `accountNickname`
  es una **extension** del banco sin equivalente en BIAN/ISO.

## Reglas de negocio

- `accountNickname` es obligatorio en v2 (a diferencia de status, que se
  retiro de la version expuesta por simplicidad de esta API).

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (MC) | _Pendiente de crear MC v2 si se requiere_ |
| Referencia (DataType) | DT-texto-max35-v1 |
| Referencia (CodeSet) | CS-codigo-moneda-v1 |
| Referencia (StandardReference) | STD-bian-current-accounts |

## Branch lineage (Evolution)

| Version | Tipo de rama | Heredado de | Owner |
|---|---|---|---|
| v1 | trunk | — | TEAM-HERMES |
| v2 | evolution | BC-MEDIOSPAGO-cuenta-identificacion-v1 | TEAM-HERMES |

## Machine-readable summary

```yaml
id: "BC-MEDIOSPAGO-cuenta-identificacion-v2"
domain_id: "DOM-MEDIOSPAGO"
consumed_by: []
ai_keywords: ["cuenta", "identificacion", "account", "open banking", "alias"]
```

## Checklist de publicacion

- [x] El yaml individual existe y coincide en nombre base.
- [x] `branch_lineage` completo (Evolution desde v1).
- [x] `owner_team_id_override` correcto.
- [ ] `catalog.yaml` actualizado.
