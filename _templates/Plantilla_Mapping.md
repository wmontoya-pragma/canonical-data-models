---
# ============================================================
# Plantilla_Mapping.md — V2
# ============================================================
# Documento de mapeo campo a campo entre un componente custom del
# banco y un componente de estándar (ISO20022/BIAN). Se usa cuando
# standard_alignment_strategy: mapping en el BC/MC/MD/CS de origen.
# Vive en _mappings/.

id: "MAP-{{dominio}}-{{nombre}}"
name: "Mapeo {{Componente custom}} <-> {{Componente estándar}}"
type: "mapping"
domain_id: "DOM-{{DOMINIO}}"
status: "draft"

custom_component_id: "{{BC-XXX / MC-XXX / MD-XXX / CS-XXX}}"
standard_reference_id: "{{STD-iso20022-XXX / STD-bian-XXX}}"

mapping_completeness: "partial"   # full | partial
gap_fit_notes: null                 # si hay campos del custom sin equivalente en el estándar, o viceversa

ai_keywords: []
aliases: []

created_date: "{{YYYY-MM-DD}}"
updated_date: "{{YYYY-MM-DD}}"
---

# Mapeo {{Componente custom}} ↔ {{Componente estándar}}

## Resumen

{{Por qué se requiere este mapeo y en qué contexto de negocio aplica.}}

## Mapeo campo a campo

| Campo custom (banco) | Campo estándar | Tipo de transformación | Notas |
|---|---|---|---|
| `{{campo_custom}}` | `{{campo_estandar}}` | directo / conversión / concatenación / sin equivalente | {{nota}} |

## Campos sin equivalente (gap)

> Campos del banco que NO existen en el estándar, o campos del
> estándar que el banco no usa.

| Campo | Lado | Justificación |
|---|---|---|
| `{{campo}}` | custom / estándar | {{por qué no hay equivalente}} |

## Reglas de transformación

```
{{Pseudocódigo o reglas explícitas de transformación, si aplica.}}
```

## Relaciones

| Componente custom | Componente estándar | Estrategia |
|---|---|---|
| {{BC-XXX}} | {{STD-iso20022-XXX}} | mapping |

## Checklist de publicación

- [ ] Todos los campos del componente custom están mapeados o explícitamente marcados como gap.
- [ ] `mapping_completeness` refleja la realidad (`full` solo si no hay gaps).
- [ ] Reglas de transformación verificadas con al menos un caso de prueba.
- [ ] Referenciado desde el front matter del componente custom (`standard_reference`).
