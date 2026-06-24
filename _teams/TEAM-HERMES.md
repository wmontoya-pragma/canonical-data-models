---
title: "Hermes (Equipo Productor)"
doc_type: "canonical-producer-team"
team_id: "TEAM-HERMES"
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

Hermes

## Summary

Equipo productor del dominio Medios de Pago. Nombrado en honor al dios
griego del comercio, los intercambios y los mensajeros: el dominio se
documenta como mensajes de transaccion (Message Components/Definitions)
que viajan entre sistemas, en linea con ISO 20022 como estandar de
mensajeria de pagos.

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
| DOM-MEDIOSPAGO | 2026-06-23 | [dominios/DOM-MEDIOSPAGO/](../dominios/DOM-MEDIOSPAGO/) |

## Componentes gobernados (vista rapida)

> Lista de navegacion directa a los artefactos reales bajo este equipo.
> La fuente de verdad de ownership sigue siendo `owner_team_id`/`owner_team_id_override`
> en cada componente y `_catalog/dependency-graph.yaml`.

| Componente | Tipo |
|---|---|
| [BC-MEDIOSPAGO-cuenta-origen-v1](../dominios/DOM-MEDIOSPAGO/business-components/BC-MEDIOSPAGO-cuenta-origen-v1.md) | Business Component |
| [BC-MEDIOSPAGO-cuenta-identificacion-v1](../dominios/DOM-MEDIOSPAGO/business-components/BC-MEDIOSPAGO-cuenta-identificacion-v1.md) | Business Component |
| [BC-MEDIOSPAGO-cuenta-identificacion-v2](../dominios/DOM-MEDIOSPAGO/business-components/BC-MEDIOSPAGO-cuenta-identificacion-v2.md) | Business Component |
| [MC-MEDIOSPAGO-identificacion-cuenta-v1](../dominios/DOM-MEDIOSPAGO/message-components/MC-MEDIOSPAGO-identificacion-cuenta-v1.md) | Message Component |
| [MC-MEDIOSPAGO-saldos-cuenta-v1](../dominios/DOM-MEDIOSPAGO/message-components/MC-MEDIOSPAGO-saldos-cuenta-v1.md) | Message Component |
| [MD-MEDIOSPAGO-consultar-cuenta-v1](../dominios/DOM-MEDIOSPAGO/message-definitions/MD-MEDIOSPAGO-consultar-cuenta-v1.md) | Message Definition |

## Componentes con ownership especifico (overrides)

| component_id | domain_id contenedor | Owner por defecto del dominio | Motivo del override |
|---|---|---|---|
| — | — | — | — |

## Historial de cambios de ownership

| Fecha | Evento | Detalle |
|---|---|---|
| 2026-06-23 | Creacion del equipo | Constitucion de TEAM-HERMES para PoC del modelo canonico |

## Machine-readable summary

```yaml
team_id: "TEAM-HERMES"
status: "active"
governs_domains:
  - "DOM-MEDIOSPAGO"
governs_components_override: []
```
