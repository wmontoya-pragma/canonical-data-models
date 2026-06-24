# canonical-data-models (General)
Repositorio canónico de Business Components, Message Components y APIs del banco. Documenta origen normativo, versionamiento multi-rama con gobierno por equipo productor, y genera contratos OAS 3.0 — diseñado para ser IA-friendly.

# Canonical Data Models — Modelo de Gobierno de Datos Canónico (V2)

> **Repositorio de prueba de concepto (PoC)** para el modelo de gobierno de
> artefactos canónicos de datos del banco. Implementa la arquitectura V2:
> multi-fuente (Custom / ISO 20022 / BIAN), branch strategies (Evolution /
> Fork) y gobierno por Equipo Productor.

---

## 1. ¿Qué es este repositorio?

Un framework reutilizable y AI-ready para documentar y publicar artefactos
canónicos de datos — Business Components, Message Components, Message
Definitions, DataTypes y Code-sets — cada uno como un par `.md` (documentación
legible por humanos) + `.yml`/`.yaml` (schema OpenAPI consumible por máquinas),
con trazabilidad completa hacia los estándares ISO 20022 y BIAN cuando aplica.

El objetivo final (fuera del alcance de esta PoC) es que un equipo de 10+
analistas pueda contribuir bajo gobierno real (CODEOWNERS, comités de
aprobación por Equipo Productor) y que agentes de IA puedan navegar y generar
artefactos de forma autónoma.

---

## 2. Arquitectura del modelo (V2)

### 2.1 Capas de composición

```
StandardReference (ISO 20022 / BIAN)
        ▲
        │ (gap-fit / mapping / reference)
        │
   Business Component (BC) ──► BC, DataType, CodeSet, StandardReference
        ▲
        │ composed_from
        │
  Message Component (MC) ──► MC, BC (opcional), DataType, CodeSet
        ▲
        │ composed_from
        │
 Message Definition (MD) ──► MC, DataType
        ▲
        │ ensamblado en
        │
      OAS de dominio (paths + $ref) ──► bundle autocontenido (oas/dist/*.bundled.yaml)
```

**Reglas de composición vigentes:**

| Capa | Puede referenciar |
|---|---|
| **MD** | 1+ MC, 1+ DataType |
| **MC** | 1+ MC, **0+ BC (opcional)**, 1+ DataType, 1+ CodeSet |
| **BC** | 1+ BC, 1+ DataType, 1+ CodeSet, y/o 1+ StandardReference |

> **Regla de prioridad MC → CodeSet**: cuando un campo de un CodeSet (ej.
> moneda) podría resolverse vía un BC o directamente desde un MC, se prioriza
> la referencia directa MC → CodeSet, evitando pasar innecesariamente por un BC.

### 2.2 Alineación a estándares (BC/MC/CS con `source != custom`)

| Estrategia | Cuándo se usa |
|---|---|
| **Reference** | El estándar es solo inspiración conceptual, sin equivalencia campo a campo. |
| **Mapping** | Entidades independientes (custom y estándar), con tabla de equivalencia en `_mappings/`. |
| **Gap-fit** | El componente custom es 1:1 con el estándar, documentando solo extensiones y gaps. |

### 2.3 Branch strategies (versiones MAJOR)

| Estrategia | Significado |
|---|---|
| **Evolution** | Ciclo de deprecación estándar: v2 sucede a v1 en el mismo linaje de gobierno. |
| **Fork** | Gobierno paralelo permanente; v2 puede tener un Equipo Productor distinto al de v1 (`owner_team_id_override`). |

### 2.4 Gobierno por Equipo Productor (no por dominio)

El dominio (`DOM-MEDIOSPAGO`, `DOM-CREDITO-CONSUMO`) es una agrupación
temática de negocio. El **Equipo Productor** (`_teams/TEAM-XXX.md`) es quien
real y formalmente gobierna y aprueba cambios — relación muchos-a-muchos,
con `owner_team_id_override` a nivel de componente individual para casos
de Fork con dueño distinto al del dominio contenedor.

### 2.5 Convención de archivos

- **`.md`**: documentación legible (descripción funcional, reglas de negocio,
  relaciones — con hipervínculos relativos a otros artefactos), front matter
  YAML con metadata estructurada para navegación de agentes IA.
- **`.yml`** (sibling, mismo nombre base): **Schema Object "pelado"** en la
  raíz (sin envoltorio `components: schemas:`), para ser `$ref`-eable
  directamente desde otros archivos OAS.
- **`.yaml`** (extensión distinta, solo en `oas/dist/`): el bundle OAS final,
  autocontenido, generado con `redocly bundle` — sin `$ref` externos,
  requisito de despliegue en IBM APIConnect.

---

## 3. Estructura del repositorio

```
canonical-data-models/
├── _canonical-standards/        # Fichas de estándares externos (ISO 20022, BIAN) — solo lectura
│   ├── bian/
│   └── iso20022/
├── _codesets/                   # Code-sets compartidos entre dominios
├── _datatypes/                  # DataTypes compartidos entre dominios
├── _mappings/                   # Documentos de mapeo (estrategia Mapping)
├── _templates/                  # Plantillas versionadas (BC, MC, MD, CS, StandardReference,
│                                 # Mapping, ProducerTeam, OAS base)
├── _teams/                      # Fichas de Equipo Productor (TEAM-HERMES, TEAM-RAGNAR)
├── _catalog/                    # catalog.yaml + dependency-graph.yaml (machine-readable)
├── .github/
│   ├── CODEOWNERS
│   └── pull_request_template.md
└── dominios/
    ├── DOM-MEDIOSPAGO/          # Equipo Productor: TEAM-HERMES
    │   ├── business-components/
    │   ├── message-components/
    │   ├── message-definitions/
    │   └── oas/
    │       └── dist/            # Bundles autocontenidos (publicación final)
    └── DOM-CREDITO-CONSUMO/     # Equipo Productor: TEAM-RAGNAR (estructura creada, sin contenido aún)
```

---

## 4. Flujo de trabajo (trunk-based)

1. `git checkout -b feature/lo-que-vayas-a-hacer` desde `main` actualizado.
2. Crear/editar artefactos siguiendo las plantillas de `_templates/`.
3. Commit + push de la rama.
4. Pull Request hacia `main` (plantilla de PR con checklist incluida).
5. **Squash and merge** — la rama se borra automáticamente.

`main` está protegida: requiere PR (no se permite push directo), historial
lineal, y resolución de conversaciones antes de mergear.

---

## 5. Alcance de esta PoC

Esta prueba de concepto valida que el **modelo y el flujo de gobierno
funcionan de extremo a extremo**, con herramientas reales, antes de
escalarlo a un equipo de 10+ analistas. Específicamente:

- ✅ Que la estructura de carpetas V2 sea viable y completa.
- ✅ Que el flujo trunk-based (rama → PR → squash merge) sea ejecutable en
  GitHub, incluyendo branch protection.
- ✅ Que `CODEOWNERS` se pueda configurar correctamente (sintaxis, branch
  protection, repo público requerido en plan Free).
- ✅ Que las plantillas documentales cubran todos los tipos de artefacto.
- ✅ Que el modelo de archivos (`.md` + `.yml` sibling "pelado") sea
  **realmente referenciable** por herramientas de bundling reales (Redocly),
  generando un OAS autocontenido válido para APIConnect.
- ✅ Que las reglas de composición entre capas (BC/MC/MD/DataType/CodeSet)
  sean coherentes con un caso de negocio real (modelo de Cuentas).
- ✅ Que el gobierno por Equipo Productor sea documentable y enlazable.

**Fuera de alcance de esta PoC** (documentado como pendiente, no resuelto):

- Automatización vía CI (validación y generación de catálogo en cada PR).
- Validación real de asignación automática de reviewer por CODEOWNERS con
  un segundo usuario distinto del autor del PR.
- Comités de aprobación reales (personas asignadas, mecanismos de votación).
- Creación de GitHub Teams reales (`@somospragma-genia/hermes`, etc.) para
  reemplazar el placeholder `@wmontoya-pragma` en CODEOWNERS.
- Contenido de negocio exhaustivo (solo se modeló el caso de Cuentas /
  Medios de Pago como ejemplo demostrativo).

---

## 6. Estado de ejecución (hasta el momento)

### ✅ Completado y validado

| Área | Detalle |
|---|---|
| Estructura de carpetas V2 | Completa, en `main` |
| Flujo trunk-based | Validado en 10 PRs reales (squash merge, borrado automático de rama) |
| Branch protection | PR obligatorio, historial lineal, conversaciones resueltas |
| CODEOWNERS | Configurado, sintácticamente válido, repo público para habilitarlo |
| Plantillas documentales | BC, MC, MD, CS, StandardReference, Mapping, ProducerTeam, OAS base — las 8 en `_templates/` |
| Fichas de Equipo Productor | `TEAM-HERMES` (DOM-MEDIOSPAGO), `TEAM-RAGNAR` (DOM-CREDITO-CONSUMO) |
| Modelo de archivos `.md` + `.yml` sibling | Validado con `openapi-spec-validator` y `redocly bundle` — bundle 100% autocontenido, 0 `$ref` externos |
| Caso de negocio real (Cuentas) | 2 StandardReference, 2 CodeSet, 3 DataType, 2 BC (v1 Evolution → v2), 2 MC (uno con BC, otro sin BC + CodeSet directo), 1 MD, OAS + bundle generados y validados |
| Reglas de composición ampliadas | CodeSet permitido en BC y MC; BC opcional en MC — codificadas en `scripts/validate_canonical_model.py` (generado, aún no subido al repo) |
| `_catalog/catalog.yaml` y `dependency-graph.yaml` | Poblados con los 11 componentes reales del modelo de cuentas |
| Hipervínculos entre artefactos `.md` | Agregados y verificados programáticamente (0 enlaces rotos) en los 14 documentos reales |

### ⏳ Pendiente / hallazgos documentados (no bloqueantes para la PoC)

1. **Branch protection — approvals en 0** (Opción A, mientras se trabaja en
   solitario). Subir a 1 y activar "Require review from Code Owners" cuando
   se sumen los analistas reales.
2. **CODEOWNERS — asignación automática nunca validada end-to-end.** GitHub
   no asigna como reviewer al mismo usuario que abre el PR; falta un segundo
   usuario real (o cuenta de prueba) para confirmarlo.
3. **`oas_schema_ref` vs. nombre real generado por el bundler.** El front
   matter declara un alias legible (ej. `CuentaOrigen`), pero `redocly
   bundle` nombra el schema final según el archivo fuente (ej.
   `BC-MEDIOSPAGO-cuenta-origen-v1`). Falta decidir convención definitiva.
4. **CI no integrado al repositorio.** El script de validación de reglas de
   composición y el workflow de GitHub Actions ya existen, pero aún no se
   han subido — la validación y actualización del catálogo siguen siendo
   manuales en esta fase.
5. **PR `analizar-escenario` abierto sin mergear**, con la corrección del
   yaml de `BC-MEDIOSPAGO-cuenta-origen-v1` (schema "pelado") y la primera
   validación de bundling — pendiente de decisión para integrarlo a `main`.
6. **Comités de aprobación y GitHub Teams reales** no creados — las fichas
   de equipo documentan la estructura de gobierno, pero los roles siguen
   marcados como "Por definir".

---

## 7. Cómo crear un nuevo artefacto (guía rápida)

1. Verifica en `_catalog/catalog.yaml` si el componente que necesitas ya existe.
2. Si falta algo, créalo en orden ascendente de capa: DataType/CodeSet →
   Business Component → Message Component → Message Definition, usando la
   plantilla correspondiente en `_templates/`.
3. Cada `.md` necesita su `.yml` sibling con el schema "pelado" en la raíz.
4. Agrega hipervínculos relativos en las tablas de "Relaciones"/"Composed
   from" hacia los componentes reales que referencia.
5. Crea o actualiza el OAS de dominio (`dominios/{DOM}/oas/*.yaml`)
   referenciando los Message Components vía `$ref`.
6. Genera el bundle: `redocly bundle <oas>.yaml -o dist/<oas>.bundled.yaml`.
7. Actualiza `_catalog/catalog.yaml` y `_catalog/dependency-graph.yaml` con
   el componente nuevo.
8. Abre el PR siguiendo el flujo trunk-based descrito en la sección 4.

---

## 8. Herramientas usadas en esta PoC

- **IDE**: Kiro (VS Code-based)
- **GitHub**: autenticación vía OAuth Device Code flow
- **Bundling/validación**: [Redocly CLI](https://redocly.com/docs/cli) (`redocly bundle`), `openapi-spec-validator`
- **Estándares de referencia**: ISO 20022, BIAN
- **Versionado**: SemVer (MAJOR.MINOR.PATCH)
