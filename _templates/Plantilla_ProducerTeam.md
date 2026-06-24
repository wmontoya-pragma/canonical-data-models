---
title: "{{NombreEquipoProductor}} (Equipo Productor)"
doc_type: "canonical-producer-team"
team_id: "TEAM-{{CODIGO_EQUIPO}}"
language: "es"
status: "{{Active/Disbanded}}"
date: "{{YYYY-MM-DDTHH:mm:ss-05:00}}"
contact_email: "{{email-equipo@banco.com}}"
last_review_date: "{{YYYY-MM-DD}}"
---

## Document status

- [ ] Active
- [ ] Disbanded

## Artifact type

- [x] ProducerTeam

## Equipo Productor

{{NombreEquipoProductor}}

## Summary

{{Descripcion breve del alcance y responsabilidad del equipo}}

> **Que es esta ficha**: es la entidad de **gobierno real** del repositorio.
> A diferencia de un dominio (agrupacion tematica de negocio), un Equipo
> Productor es quien efectivamente aprueba, gobierna y responde por un
> conjunto de dominios y/o componentes especificos, sin importar en
> cuantas carpetas tematicas esten distribuidos.

## Governance

| Rol | Persona / Cargo | Responsabilidad |
|---|---|---|
| Chair / lider | {{nombre}} | Autoridad final de aprobacion |
| Miembro tecnico | {{nombre}} | Valida contratos de datos y OAS |
| Miembro de negocio | {{nombre}} | Valida impacto y semantica funcional |
| Miembro de cumplimiento (si aplica) | {{nombre}} | Valida cumplimiento regulatorio |

- **Frecuencia de reuniones**: {{ej: quincenal}}
- **Mecanismo de votacion**: {{unanimidad / mayoria simple / consenso}}

## Approval requirements

| Tipo de cambio | Requiere | Timeline |
|---|---|---|
| Nuevo BC/MC/MD | Votacion del comite | {{ej: 5 dias habiles}} |
| MINOR / PATCH | Auto-publicacion con notificacion posterior | Inmediato |
| Fork (nueva rama MAJOR independiente) | Votacion del comite + aval de Arquitectura Empresarial | {{ej: 10 dias habiles}} |

## Dominios bajo gobierno de este equipo

| domain_id | Desde | Documento de dominio |
|---|---|---|
| {{DOM-XXX}} | {{YYYY-MM-DD}} | {{link}} |

## Componentes con ownership especifico (overrides)

> Componentes individuales que este equipo gobierna DENTRO de un dominio
> que en general pertenece a otro equipo (caso tipico: Fork).

| component_id | domain_id contenedor | Owner por defecto del dominio | Motivo del override |
|---|---|---|---|
| {{BC-XXX-v2}} | {{DOM-XXX}} | {{TEAM-YYY}} | {{ej: Fork con gobierno independiente}} |

## Historial de cambios de ownership

| Fecha | Evento | Detalle |
|---|---|---|
| {{YYYY-MM-DD}} | {{Adquisicion de dominio / Fork recibido / Disolucion}} | {{detalle}} |

## Machine-readable summary

```yaml
team_id: "TEAM-{{CODIGO_EQUIPO}}"
status: "active"
governs_domains: []
governs_components_override: []
```

## Checklist de publicacion

- [ ] Las tablas "Dominios bajo gobierno" y "Componentes con override" coinciden con lo declarado en el front matter de cada dominio/componente (`owner_team_id` / `owner_team_id_override`).
- [ ] Comite definido con al menos Chair + miembro tecnico.
- [ ] `contact_email` valido y monitoreado.
