---
id: "DT-fecha-hora-v1"
name: "Fecha y Hora ISO"
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

individual_oas_file: "DT-fecha-hora-v1.yml"
oas_schema_ref: "#/components/schemas/DT-fecha-hora-v1"

ai_keywords: ["fecha", "hora", "timestamp", "isodatetime"]
aliases: ["ISODateTime"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Fecha y Hora ISO

## Descripcion funcional

Estampa de tiempo completa con zona horaria o UTC explicita, basada en
`ISODateTime` de ISO 20022 / ISO 8601.

## Estructura

| Restriccion | Valor |
|---|---|
| Tipo | string |
| format | date-time |
| pattern | `AAAA-MM-DDTHH:mm:ss(.sss)?(Z|+-HH:mm)` |

## Standard alignment

- **Estrategia**: reference (tipo de dato base ISO 8601/20022, sin adaptacion).

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (MC) | MC-saldos-cuenta-v1 |

## Machine-readable summary

```yaml
id: "DT-fecha-hora-v1"
domain_id: "_datatypes"
consumed_by: ["MC-saldos-cuenta-v1"]
ai_keywords: ["fecha", "hora", "timestamp", "isodatetime"]
```
