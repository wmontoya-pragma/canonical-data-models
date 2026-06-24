---
title: "Ragnar (Equipo Productor)"
doc_type: "canonical-producer-team"
team_id: "TEAM-RAGNAR"
language: "es"
status: "Active"
date: "2026-06-23T00:00:00-05:00"
contact_email: "wmontoya@pragma.com.co"
last_review_date: "2026-06-24"
---

## Document status

- [x] Active
- [ ] Disbanded

## Artifact type

- [x] ProducerTeam

## Equipo Productor

Ragnar

## Summary

Equipo productor del dominio Credito de Consumo.

> Equipo de prueba de concepto (PoC). Roles y comite aun no formalizados
> con personal real; se documenta la estructura para validar el modelo
> de gobierno, no la composicion final del equipo.

## Governance

| Rol | Persona / Cargo | Responsabilidad |
|---|---|---|
| Chair / lider | Por definir | Autoridad final de aprobacion |
| Miembro tecnico | Por definir | Valida contratos de datos y OAS |
| Miembro de negocio | Por definir | Valida impacto y semantica funcional |

- **Frecuencia de reuniones**: Por definir
- **Mecanismo de votacion**: Por definir

## Approval requirements

| Tipo de cambio | Requiere | Timeline |
|---|---|---|
| Nuevo BC/MC/MD | Votacion del comite | Por definir |
| MINOR / PATCH | Auto-publicacion con notificacion posterior | Inmediato |
| Fork | Votacion del comite + aval de Arquitectura Empresarial | Por definir |

## Dominios bajo gobierno de este equipo

| domain_id | Desde | Documento de dominio |
|---|---|---|
| DOM-CREDITO-CONSUMO | 2026-06-23 | [dominios/DOM-CREDITO-CONSUMO/](../dominios/DOM-CREDITO-CONSUMO/) |

## Componentes gobernados (vista rapida)

> Aun sin componentes reales creados en este dominio.

| Componente | Tipo |
|---|---|
| — | — |

## Componentes con ownership especifico (overrides)

| component_id | domain_id contenedor | Owner por defecto del dominio | Motivo del override |
|---|---|---|---|
| — | — | — | — |

## Historial de cambios de ownership

| Fecha | Evento | Detalle |
|---|---|---|
| 2026-06-23 | Creacion del equipo | Constitucion de TEAM-RAGNAR para PoC del modelo canonico |

## Machine-readable summary

```yaml
team_id: "TEAM-RAGNAR"
status: "active"
governs_domains:
  - "DOM-CREDITO-CONSUMO"
governs_components_override: []
```
