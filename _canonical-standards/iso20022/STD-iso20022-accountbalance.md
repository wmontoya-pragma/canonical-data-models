---
id: "STD-iso20022-accountbalance"
name: "AccountBalanceA01 (ISO 20022) / Depository Positions (BIAN)"
type: "standard-reference"
standard: "iso20022"
standard_version: "AccountBalanceA01"
status: "active"

source_url: "ISO 20022 AccountBalanceA01 + BIAN Depository Positions"
vendorized_date: "2026-06-24"

ai_keywords: ["saldo", "balance", "accountbalance", "iso20022", "bian"]
aliases: ["AccountBalanceA01"]
---

# AccountBalanceA01 (ISO 20022) / Depository Positions (BIAN)

## Definicion oficial

Estructura canonica para la exposicion de saldos disponibles y contables
de un producto de deposito. Cada saldo (`closingLedgerBalance`,
`availableBalance`) empareja monto y moneda en un solo objeto
(`ActiveCurrencyAndAmount`).

## Estructura oficial

| Campo | Tipo | Obligatorio (estandar) | Descripcion oficial |
|---|---|---|---|
| `closingLedgerBalance` | `ActiveCurrencyAndAmount` | Si | Saldo contable al cierre |
| `availableBalance` | `ActiveCurrencyAndAmount` | Si | Saldo disponible |
| `lastUpdateDateTime` | `ISODateTime` | Si | Ultima actualizacion |

`ActiveCurrencyAndAmount` (tipo de dato base referenciado): empareja
`amount` (DecimalNumber) + `currency` (CurrencyCode) en un solo objeto.

## Usado como referencia por

| Componente | Estrategia declarada |
|---|---|
| MC-MEDIOSPAGO-saldos-cuenta-v1 | mapping |
| DT-importe-decimal-v1 | gap-fit |

## Notas de vendorizacion

- **Diferencia conocida**: el banco separa `amount` y `currency` en dos
  campos independientes a nivel de DataType (`DT-importe-decimal-v1` sin
  moneda) en lugar de usar `ActiveCurrencyAndAmount` emparejado, para
  permitir que el MC declare la moneda una sola vez para ambos saldos
  (en vez de repetirla en cada saldo como hace el estandar).

## Checklist de publicacion

- [x] Contenido fiel al estandar oficial.
- [x] `source_url` y `vendorized_date` completos.
- [x] Diferencias de gap-fit documentadas.
