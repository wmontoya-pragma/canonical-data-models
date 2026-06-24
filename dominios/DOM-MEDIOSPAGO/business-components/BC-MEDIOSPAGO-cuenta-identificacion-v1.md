---
id: "BC-MEDIOSPAGO-cuenta-identificacion-v1"
name: "Identificacion de Cuenta"
type: "business-component"
domain_id: "DOM-MEDIOSPAGO"
status: "active"
version: "1.0.0"

source: "bian"
standard_alignment_strategy: "gap-fit"
standard_reference: "STD-bian-current-accounts"

major_branch_strategy: "evolution"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "BC-MEDIOSPAGO-cuenta-identificacion-v1.yml"
oas_schema_ref: "#/components/schemas/BC-MEDIOSPAGO-cuenta-identificacion-v1"

ai_keywords: ["cuenta", "identificacion", "account", "bian", "iso20022"]
aliases: ["AccountIdentification"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Identificacion de Cuenta (v1)

## Descripcion funcional

Identificacion canonica base de una cuenta financiera o de deposito,
alineada 1 a 1 con BIAN (Current Accounts) e ISO 20022 (FinancialAccount24).

## Atributos

| Atributo | Tipo | Obligatorio | Descripcion |
|---|---|---|---|
| `identification` | [DT-texto-max35-v1](../../../_datatypes/DT-texto-max35-v1.md) | Si | Numero de cuenta contractual o IBAN |
| `type` | string (enum: CACC, SVGS, COMM, ONLD) | Si | Tipo de cuenta |
| `currency` | [CS-codigo-moneda-v1](../../../_codesets/CS-codigo-moneda-v1.md) | Si | Moneda de la cuenta |
| `status` | string (enum: ENABLED, DISABLED, PENDING, FROZEN) | No | Estado operativo del contrato |

## Standard alignment

- **Estrategia**: gap-fit — 1 a 1 con el estandar, sin extensiones en esta version.
- **Referencia al estandar**: [STD-bian-current-accounts](../../../_canonical-standards/bian/STD-bian-current-accounts.md)

## Reglas de negocio

- `identification` debe ser unico por cuenta en el Core bancario.
- `status` ausente se interpreta como `ENABLED` por defecto.

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (MC) | [MC-MEDIOSPAGO-identificacion-cuenta-v1](../message-components/MC-MEDIOSPAGO-identificacion-cuenta-v1.md) |
| Referencia (DataType) | [DT-texto-max35-v1](../../../_datatypes/DT-texto-max35-v1.md) |
| Referencia (CodeSet) | [CS-codigo-moneda-v1](../../../_codesets/CS-codigo-moneda-v1.md) |
| Referencia (StandardReference) | [STD-bian-current-accounts](../../../_canonical-standards/bian/STD-bian-current-accounts.md) |
| Evolucion (version siguiente) | [BC-MEDIOSPAGO-cuenta-identificacion-v2](./BC-MEDIOSPAGO-cuenta-identificacion-v2.md) |

## Branch lineage (si es Fork)

No aplica — `major_branch_strategy: evolution` (ver [v2](./BC-MEDIOSPAGO-cuenta-identificacion-v2.md) como evolucion de este).

## Machine-readable summary

```yaml
id: "BC-MEDIOSPAGO-cuenta-identificacion-v1"
domain_id: "DOM-MEDIOSPAGO"
consumed_by: ["MC-MEDIOSPAGO-identificacion-cuenta-v1"]
ai_keywords: ["cuenta", "identificacion", "account", "bian", "iso20022"]
```

## Checklist de publicacion

- [x] El yaml individual existe y coincide en nombre base.
- [x] `source`/`standard_alignment_strategy`/`standard_reference` completos.
- [x] `owner_team_id_override` correcto (hereda TEAM-HERMES).
- [x] `catalog.yaml` actualizado.
