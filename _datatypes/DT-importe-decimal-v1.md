---
id: "DT-importe-decimal-v1"
name: "Importe Decimal"
type: "datatype"
domain_id: "_datatypes"
status: "active"
version: "1.0.0"

source: "iso20022"
standard_alignment_strategy: "gap-fit"
standard_reference: "STD-iso20022-accountbalance"

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "DT-importe-decimal-v1.yml"
oas_schema_ref: "#/components/schemas/DT-importe-decimal-v1"

ai_keywords: ["monto", "decimal", "saldo", "importe"]
aliases: ["DecimalNumber", "Amount"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Importe Decimal

## Descripcion funcional

Numero decimal positivo con maximo dos posiciones decimales, basado en
`DecimalNumber` de ISO 20022. A diferencia de `ActiveCurrencyAndAmount`
(ISO), este DataType NO incluye la moneda — se deja deliberadamente solo
el valor numerico para que el componente consumidor (MC) decida si
referencia la moneda via DataType compuesto o directamente via CodeSet.

## Estructura

| Restriccion | Valor |
|---|---|
| Tipo | number (double) |
| minimum | 0.00 |
| multipleOf | 0.01 |

## Standard alignment

- **Estrategia**: gap-fit — el estandar ISO (`ActiveCurrencyAndAmount`)
  empareja monto+moneda en un solo objeto; el banco separa ambos campos
  para permitir que el MC referencie la moneda directamente via CodeSet.
- **Referencia al estandar**: [STD-iso20022-accountbalance](../_canonical-standards/iso20022/STD-iso20022-accountbalance.md)

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (MC) | [MC-MEDIOSPAGO-saldos-cuenta-v1](../dominios/DOM-MEDIOSPAGO/message-components/MC-MEDIOSPAGO-saldos-cuenta-v1.md) |

## Machine-readable summary

```yaml
id: "DT-importe-decimal-v1"
domain_id: "_datatypes"
consumed_by: ["MC-MEDIOSPAGO-saldos-cuenta-v1"]
ai_keywords: ["monto", "decimal", "saldo", "importe"]
```
