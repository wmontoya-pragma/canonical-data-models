---
id: "STD-bian-current-accounts"
name: "Current Accounts (BIAN) / FinancialAccount24 (ISO 20022)"
type: "standard-reference"
standard: "bian"
standard_version: "BIAN Service Landscape (Current Accounts)"
status: "active"

source_url: "https://bian.org/servicelandscape/ (Current Accounts) + ISO 20022 FinancialAccount24"
vendorized_date: "2026-06-24"

ai_keywords: ["cuenta", "account", "bian", "iso20022", "financialaccount24"]
aliases: ["AccountIdentification (BIAN/ISO)"]
---

# Current Accounts (BIAN) / FinancialAccount24 (ISO 20022)

## Definicion oficial

Componente conceptual que combina el dominio de negocio "Current Accounts"
de BIAN (identificacion y estado de una cuenta de deposito) con la
estructura de datos `FinancialAccount24` de ISO 20022 (identificacion,
tipo y moneda de una cuenta financiera).

## Estructura oficial

| Campo | Tipo | Obligatorio (estandar) | Descripcion oficial |
|---|---|---|---|
| `identification` | `Max35Text` | Si | Numero de cuenta contractual o IBAN |
| `type` | `string` (enum) | Si | Tipo de cuenta (CACC, SVGS, COMM, ONLD) |
| `currency` | `CurrencyCode` | Si | Moneda de la cuenta (ISO 4217) |
| `status` | `string` (enum) | No | Estado operativo del contrato (ENABLED, DISABLED, PENDING, FROZEN) |

## Usado como referencia por

| Componente | Estrategia declarada |
|---|---|
| BC-MEDIOSPAGO-cuenta-identificacion-v1 | gap-fit |
| BC-MEDIOSPAGO-cuenta-identificacion-v2 | gap-fit |

## Notas de vendorizacion

- **Version fichada**: BIAN Service Landscape vigente + ISO 20022 FinancialAccount24.
- **Diferencia conocida**: el banco extiende el estandar en v2 con `accountNickname`,
  campo de personalizacion para Open Banking que no existe en BIAN/ISO base.

## Checklist de publicacion

- [x] Contenido fiel al estandar oficial.
- [x] `source_url` y `vendorized_date` completos.
- [x] No contiene reglas de negocio propias del banco.
