---
id: "MC-MEDIOSPAGO-saldos-cuenta-v1"
name: "Saldos de Cuenta (mensaje)"
type: "message-component"
domain_id: "DOM-MEDIOSPAGO"
status: "active"
version: "1.0.0"

source: "iso20022"
standard_alignment_strategy: "mapping"
standard_reference: "STD-iso20022-accountbalance"

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "MC-MEDIOSPAGO-saldos-cuenta-v1.yml"
oas_schema_ref: "#/components/schemas/MC-MEDIOSPAGO-saldos-cuenta-v1"

composed_from:
  - component_id: "DT-importe-decimal-v1"
    branch_consumed: "v1"
  - component_id: "DT-fecha-hora-v1"
    branch_consumed: "v1"
  - component_id: "CS-codigo-moneda-v1"
    branch_consumed: "v1"

ai_keywords: ["saldo", "balance", "cuenta", "disponible", "contable"]
aliases: ["BalanceTypes"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Saldos de Cuenta (mensaje)

## Descripcion funcional

Estructura canonica para exponer saldos contable y disponible de una
cuenta. Basado en `AccountBalanceA01` (ISO 20022) / Depository Positions
(BIAN), mapeado a una estructura propia mas simple para el mensaje.

> **Ejemplo deliberado de la regla V2 relajada**: este MC no compone
> ningun BC — solo DataTypes y un CodeSet referenciado directamente.

## Composed from

| Componente | Tipo | Rama consumida | Rol en el mensaje |
|---|---|---|---|
| [DT-importe-decimal-v1](../../../_datatypes/DT-importe-decimal-v1.md) | DataType | v1 | Monto de `closingLedgerBalance` y `availableBalance` (sin moneda embebida) |
| [DT-fecha-hora-v1](../../../_datatypes/DT-fecha-hora-v1.md) | DataType | v1 | `lastUpdateDateTime` |
| [CS-codigo-moneda-v1](../../../_codesets/CS-codigo-moneda-v1.md) | CodeSet | v1 | Moneda comun a ambos saldos, referenciada **directamente desde el MC** (prioridad sobre pasar por un BC) |

## Estructura

| Campo | Tipo | Obligatorio | Origen | Descripcion |
|---|---|---|---|---|
| `closingLedgerBalance` | [DT-importe-decimal-v1](../../../_datatypes/DT-importe-decimal-v1.md) | Si | DataType | Saldo contable al cierre |
| `availableBalance` | [DT-importe-decimal-v1](../../../_datatypes/DT-importe-decimal-v1.md) | Si | DataType | Saldo disponible para transaccionar |
| `currency` | [CS-codigo-moneda-v1](../../../_codesets/CS-codigo-moneda-v1.md) | Si | CodeSet (directo) | Moneda de ambos saldos |
| `lastUpdateDateTime` | [DT-fecha-hora-v1](../../../_datatypes/DT-fecha-hora-v1.md) | Si | DataType | Ultima actualizacion |

## Standard alignment

- **Estrategia**: mapping — `AccountBalanceA01` (ISO) empareja monto+moneda
  por cada saldo; este MC separa la moneda a nivel de mensaje (un solo
  campo `currency` para ambos saldos) por simplicidad de la API.
- **Referencia al estandar**: [STD-iso20022-accountbalance](../../../_canonical-standards/iso20022/STD-iso20022-accountbalance.md)

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (MD) | [MD-MEDIOSPAGO-consultar-cuenta-v1](../message-definitions/MD-MEDIOSPAGO-consultar-cuenta-v1.md) |

## Machine-readable summary

```yaml
id: "MC-MEDIOSPAGO-saldos-cuenta-v1"
domain_id: "DOM-MEDIOSPAGO"
composed_from: ["DT-importe-decimal-v1", "DT-fecha-hora-v1", "CS-codigo-moneda-v1"]
consumed_by: ["MD-MEDIOSPAGO-consultar-cuenta-v1"]
ai_keywords: ["saldo", "balance", "cuenta", "disponible", "contable"]
```

## Checklist de publicacion

- [x] El yaml individual existe y coincide en nombre base.
- [x] Tabla "Composed from" completa.
- [x] No referencia BC (valido bajo regla V2 relajada); CodeSet referenciado directamente con prioridad documentada.
- [x] `catalog.yaml` actualizado.
