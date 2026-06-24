---
id: "BC-MEDIOSPAGO-cuenta-origen-v1"
name: "Cuenta Origen"
type: "business-component"
domain_id: "DOM-MEDIOSPAGO"
status: "draft"
version: "1.0.0"

# --- Origen / fuente (V2) ---
source: "custom"
standard_alignment_strategy: "n/a"
standard_reference: null

# --- Estrategia de rama MAJOR (V2) ---
major_branch_strategy: "n/a"
branch_lineage: []

# --- Gobierno ---
owner_team_id_override: null   # hereda owner_team_id del dominio DOM-MEDIOSPAGO -> TEAM-HERMES

# --- Modelo de archivos (V2) ---
individual_oas_file: "BC-MEDIOSPAGO-cuenta-origen-v1.yaml"
oas_schema_ref: "#/components/schemas/CuentaOrigen"

# --- Descubribilidad para IA (RAG + MCP) ---
ai_keywords: ["cuenta", "origen", "debito", "medios de pago", "transferencia"]
aliases: ["Cuenta Debitada", "Cuenta Origen de Fondos"]

created_date: "2026-06-23"
updated_date: "2026-06-23"
---

# Cuenta Origen

## Descripcion funcional

Representa la cuenta bancaria desde la cual se debitan los fondos en una
operacion de Medios de Pago (ej. una transferencia o un pago). Es el
Business Component base que identifica y valida la cuenta de origen
antes de ejecutar cualquier movimiento de dinero.

## Atributos

| Atributo | Tipo | Obligatorio | Descripcion |
|---|---|---|---|
| `numeroCuenta` | `string` | Si | Numero de cuenta bancaria origen, sin guiones ni espacios |
| `tipoCuenta` | `string` | Si | Tipo de cuenta (ahorros, corriente) — ver CS-MEDIOSPAGO-tipo-cuenta |
| `titular` | `string` | Si | Nombre completo del titular de la cuenta origen |
| `documentoTitular` | `string` | Si | Numero de documento de identidad del titular |
| `entidadFinanciera` | `string` | No | Codigo de la entidad financiera, si la cuenta es interbancaria |

## Standard alignment

No aplica — `source: custom`.

## Reglas de negocio

- La cuenta origen debe existir y estar activa en el momento de la operacion.
- El `documentoTitular` debe coincidir con el titular registrado en el core bancario.
- Si `entidadFinanciera` esta presente, la operacion se trata como interbancaria.

## Relaciones

| Tipo de relacion | Componente |
|---|---|
| Usado por (MC) | MC-MEDIOSPAGO-transferencia-v1 *(pendiente de crear)* |

## Branch lineage (si es Fork)

No aplica — `major_branch_strategy: n/a`.

## Machine-readable summary

```yaml
id: "BC-MEDIOSPAGO-cuenta-origen-v1"
domain_id: "DOM-MEDIOSPAGO"
consumed_by: []
ai_keywords: ["cuenta", "origen", "debito", "medios de pago", "transferencia"]
```

## Checklist de publicacion

- [x] El yaml individual (`individual_oas_file`) existe y coincide en nombre base con este `.md`.
- [x] `source` completo (`custom`, no requiere standard_alignment_strategy).
- [x] `owner_team_id_override` correcto (`null`, hereda de TEAM-HERMES via DOM-MEDIOSPAGO).
- [ ] `catalog.yaml` actualizado con esta entrada.
- [ ] No aplica branch_lineage (no es Fork).
