---
id: "DT-texto-max35-v1"
name: "Texto Maximo 35 Caracteres"
type: "datatype"
domain_id: "_datatypes"
status: "active"
version: "1.0.0"

source: "iso20022"
standard_alignment_strategy: "reference"
standard_reference: null

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "DT-texto-max35-v1.yml"
oas_schema_ref: "#/components/schemas/DT-texto-max35-v1"

ai_keywords: ["texto", "max35text", "identificacion", "iban"]
aliases: ["Max35Text"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Texto Maximo 35 Caracteres

## Descripcion funcional

Tipo de dato basico ISO 20022 (`Max35Text`) para texto libre de hasta 35
caracteres. Usado tipicamente para numeros de cuenta, IBAN o identificadores
cortos.

## Estructura

| Restriccion | Valor |
|---|---|
| Tipo | string |
| minLength | 1 |
| maxLength | 35 |
| pattern | alfanumerico + puntuacion basica |

## Standard alignment

- **Estrategia**: reference (tipo de dato base ISO 20022, sin adaptacion).

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (BC) | [BC-MEDIOSPAGO-cuenta-identificacion-v1](../dominios/DOM-MEDIOSPAGO/business-components/BC-MEDIOSPAGO-cuenta-identificacion-v1.md) |
| Usado por (BC) | [BC-MEDIOSPAGO-cuenta-identificacion-v2](../dominios/DOM-MEDIOSPAGO/business-components/BC-MEDIOSPAGO-cuenta-identificacion-v2.md) |

## Machine-readable summary

```yaml
id: "DT-texto-max35-v1"
domain_id: "_datatypes"
consumed_by: ["BC-MEDIOSPAGO-cuenta-identificacion-v1", "BC-MEDIOSPAGO-cuenta-identificacion-v2"]
ai_keywords: ["texto", "max35text", "identificacion", "iban"]
```
