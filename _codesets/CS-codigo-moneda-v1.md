---
id: "CS-codigo-moneda-v1"
name: "Codigo de Moneda"
type: "code-set"
domain_id: "_codesets"
status: "active"
version: "1.0.0"

source: "iso20022"
standard_alignment_strategy: "reference"
standard_reference: "STD-iso20022-currency-code"

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "CS-codigo-moneda-v1.yml"
oas_schema_ref: "#/components/schemas/CS-codigo-moneda-v1"

ai_keywords: ["moneda", "currency", "divisa", "iso4217"]
aliases: ["CurrencyCode", "Codigo de Divisa"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Codigo de Moneda

## Descripcion funcional

Lista de codigos de moneda de tres letras basada en ISO 4217, usada para
identificar la divisa de un monto monetario en cualquier componente del
repositorio (saldos, montos de transferencia, tasas, etc.).

## Valores

| Codigo | Etiqueta | Descripcion | Vigente |
|---|---|---|---|
| `USD` | Dolar estadounidense | Moneda de EEUU | Si |
| `EUR` | Euro | Moneda de la Eurozona | Si |
| `COP` | Peso colombiano | Moneda de Colombia | Si |
| `MXN` | Peso mexicano | Moneda de Mexico | Si |
| `BRL` | Real brasileno | Moneda de Brasil | Si |
| `GBP` | Libra esterlina | Moneda del Reino Unido | Si |
| `JPY` | Yen japones | Moneda de Japon | Si |

## Standard alignment

- **Estrategia**: reference — se adopta la lista ISO 4217 completa, sin
  subconjunto propio del banco por ahora.
- **Referencia al estandar**: `STD-iso20022-currency-code`

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (DataType) | DT-monto-moneda-v1 |
| Usado por (MC, referencia directa con prioridad) | MC-saldos-cuenta-v1 |

## Branch lineage (si es Fork)

No aplica.

## Machine-readable summary

```yaml
id: "CS-codigo-moneda-v1"
domain_id: "_codesets"
consumed_by: ["DT-monto-moneda-v1", "MC-saldos-cuenta-v1"]
ai_keywords: ["moneda", "currency", "divisa", "iso4217"]
```

## Checklist de publicacion

- [x] El yaml individual existe y coincide en nombre base con este `.md`.
- [x] Todos los codigos vigentes documentados.
- [x] `source`/`standard_alignment_strategy` completos.
- [x] `owner_team_id_override` correcto.
- [ ] `catalog.yaml` actualizado.
