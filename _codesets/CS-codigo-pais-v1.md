---
id: "CS-codigo-pais-v1"
name: "Codigo de Pais"
type: "code-set"
domain_id: "_codesets"
status: "active"
version: "1.0.0"

source: "iso20022"
standard_alignment_strategy: "reference"
standard_reference: null

major_branch_strategy: "n/a"
branch_lineage: []

owner_team_id_override: null

individual_oas_file: "CS-codigo-pais-v1.yml"
oas_schema_ref: "#/components/schemas/CS-codigo-pais-v1"

ai_keywords: ["pais", "country", "residencia fiscal", "iso3166"]
aliases: ["CountryCode"]

created_date: "2026-06-24"
updated_date: "2026-06-24"
---

# Codigo de Pais

## Descripcion funcional

Lista de codigos de pais Alpha-2 basada en ISO 3166-1, usada para
identificar residencia fiscal o ubicacion geografica.

> Componente cargado en el PoC para fines de referencia, aun sin
> consumidores reales en el modelo (pendiente de uso en un BC/MC futuro).

## Valores

| Codigo | Etiqueta | Descripcion | Vigente |
|---|---|---|---|
| `CO` | Colombia | — | Si |
| `US` | Estados Unidos | — | Si |
| `ES` | Espana | — | Si |
| `MX` | Mexico | — | Si |
| `BR` | Brasil | — | Si |
| `GB` | Reino Unido | — | Si |
| `JP` | Japon | — | Si |

## Standard alignment

- **Estrategia**: reference — lista ISO 3166-1 completa.

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por | _Ninguno todavia_ |

## Machine-readable summary

```yaml
id: "CS-codigo-pais-v1"
domain_id: "_codesets"
consumed_by: []
ai_keywords: ["pais", "country", "residencia fiscal", "iso3166"]
```

## Checklist de publicacion

- [x] El yaml individual existe.
- [x] Codigos vigentes documentados.
- [ ] Sin consumidores reales aun; revisar si se requiere antes de publicar como `active`.
