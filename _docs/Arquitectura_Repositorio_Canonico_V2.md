# Arquitectura del Repositorio de Gobierno de Datos Canónico — V2

**Versión**: 2.0.0
**Fecha**: 2026-06-16
**Extiende a**: V1 (`v1/Arquitectura_Repositorio_Canonico.md`)
**Owner**: Oficina de Arquitectura Empresarial
**Contacto**: arquitectura@banco.com

---

## 0. Qué cambia respecto a V1

V1 asumía implícitamente: (a) todo componente es "Custom Banco", y (b) cada componente tiene una sola línea de versiones evolucionando hacia adelante (deprecar la anterior cuando sale la nueva). V2 levanta ambos supuestos.

| Aspecto | V1 | V2 |
| ------- | -- | -- |
| Origen del componente | Implícito: siempre Custom Banco | Explícito: **Custom Banco**, **ISO 20022**, o **BIAN**, declarado en ID, carpeta y front matter |
| Relación con estándares | No existía | BC custom puede **derivar de**, **mapear a**, o **alinear gap-fit con** un estándar — estrategia declarada explícitamente por componente |
| Líneas de versión MAJOR | Una sola línea: MAJOR anterior se deprecia cuando sale la nueva | Múltiples ramas MAJOR pueden coexistir **indefinidamente**, cada una con su propio owner, estado y ciclo de vida — no es solo "tiempo de migración", es gobierno paralelo legítimo |
| Estrategia de fork de versión | No aplicaba | El equipo productor declara, por componente, si una rama MAJOR nueva es "evolución" (mismo doc) o "fork" (ID hermano nuevo) |

**Compatibilidad**: todo lo de V1 sigue siendo válido como caso particular. Un componente con `source: Custom`, una sola rama MAJOR activa y sin relación con estándares es exactamente un componente V1. V2 no rompe V1; lo generaliza.

---

## 1. Multi-source: Custom Banco / ISO 20022 / BIAN

### 1.1 Qué es el "source"

El `source` identifica el origen normativo de un componente (BC, MC, MD, DataType, Code-set):

| Source | Código | Descripción | Quién lo gobierna |
| ------ | ------ | ----------- | ------------------ |
| **Custom Banco** | `CUS` | Modelo propio del banco, sin atarse a un estándar externo. | Comité de Arquitectura del dominio. |
| **ISO 20022** | `ISO` | Modelo derivado o alineado con un Message Definition de ISO 20022 (ej. `pacs.008`, `camt.053`). | Comité de Arquitectura Empresarial (custodiode la alineación al estándar). |
| **BIAN** | `BIAN` | Modelo derivado o alineado con un Service Domain / Business Object de BIAN. | Comité de Arquitectura Empresarial. |

Un mismo dominio de negocio (ej. Crédito de Consumo) puede tener componentes de los tres sources simultáneamente: un BC custom para el contrato de crédito local, un MC que se alinea a un Message Component de `pacs.008` para el desembolso interbancario, y un MD que implementa el patrón BIAN `Consumer Loan` Service Domain.

### 1.2 Cómo se relaciona un BC custom con un estándar (estrategias soportadas)

Se soportan **tres estrategias**, y cada componente custom que tenga relación con un estándar debe declarar explícitamente cuál aplica en su front matter (`standard_alignment_strategy`):

#### Estrategia A — Reference (referencia/extiende)

El BC custom es una entidad independiente que **referencia** al estándar como inspiración o trazabilidad, sin pretender equivalencia campo a campo. Útil cuando el estándar es solo un punto de partida conceptual.

```yaml
standard_alignment_strategy: "Reference"
standard_reference:
  source: ISO20022
  artifact: "pacs.008.001.08 / FIToFICstmrCdtTrf"
  relationship: "Inspirado en la estructura de transferencia crédito; no hay mapeo campo a campo exhaustivo."
```

#### Estrategia B — Mapping (entidades separadas + tabla de equivalencia)

El BC custom y el componente del estándar son **fichas independientes**, cada una con su propio documento completo. La relación vive en una tabla de mapeo (embebida + documento detallado si es complejo — ver sección 3).

```yaml
standard_alignment_strategy: "Mapping"
standard_reference:
  source: ISO20022
  artifact_id: "ISO-PACS-008-CdtTrfTxInf"
  mapping_doc: "../../_mappings/MAP-CUS-CC-001-ISO-PACS-008.md"
```

#### Estrategia C — Gap-fit (1 a 1 con extensiones documentadas)

El BC custom se basa **1 a 1** en el estándar; la mayoría de campos son idénticos, y el documento custom solo necesita declarar las **extensiones** (campos que el banco agrega) y los **gaps** (campos del estándar que el banco no usa).

```yaml
standard_alignment_strategy: "Gap-fit"
standard_reference:
  source: BIAN
  artifact_id: "BIAN-SD-ConsumerLoan-v12"
  base_version: "12.0.0"
  extensions: ["codigoPEP", "segurosCuota"]
  gaps: ["collateralAssessment"]  # campo del estándar que el banco no implementa
```

### 1.2-bis. Equipo Productor como entidad de gobierno (no el dominio)

V1 y la primera versión de V2 trataban implícitamente al **dominio** (`DOM-CREDITO-CONSUMO`) como la unidad de gobierno: el dominio tenía `owner_functional`, `owner_technical` y `approval_board` directamente en su front matter, como si cada dominio fuera autónomo y 1:1 con un equipo.

Esto no refleja la realidad organizacional: **un equipo productor puede ser responsable de varios dominios completos**. Por ejemplo, el equipo de Banca Personal puede gobernar tanto `DOM-CREDITO-CONSUMO` como `DOM-CUENTAS-AHORRO` y `DOM-SEGUROS-VOLUNTARIOS`. Tratar cada dominio como si tuviera gobierno propio e independiente duplica información (el mismo comité, los mismos emails, las mismas políticas de aprobación copiadas en N documentos de dominio) y hace imposible responder rápido "¿qué es responsabilidad de este equipo en todo el banco?" sin recorrer carpeta por carpeta.

**Corrección del modelo**: el **Equipo Productor** se convierte en una entidad de primera clase, con su propia ficha en `_teams/`, y es esa ficha la que centraliza comité, política de aprobación y contacto. El dominio (y, cuando aplica, un fork específico) simplemente **referencia** a su equipo productor mediante un `owner_team_id` — ya no define su propio gobierno de forma duplicada.

```
_teams/TEAM-BANCA-PERSONAL.md
  │  (gobierno centralizado: comité, políticas, contacto)
  │
  ├── owns → DOM-CREDITO-CONSUMO       (dominio completo)
  ├── owns → DOM-CUENTAS-AHORRO        (dominio completo)
  └── owns → DOM-SEGUROS-VOLUNTARIOS   (dominio completo)

_teams/TEAM-CONVENIOS-LIBRANZA.md
  │  (gobierno propio, distinto del anterior)
  │
  └── owns → BC-CUS-CC-001-v1          (NO un dominio completo — solo
                                         un fork específico dentro de
                                         DOM-CREDITO-CONSUMO; ver sección 2)
```

Esto también resuelve con elegancia el caso de Fork de la sección 2: cuando dijimos que `BC-CUS-CC-001-v1` tiene "gobierno propio, distinto del tronco", lo que realmente queremos decir es que su `owner_team_id` apunta a un equipo productor **distinto** al que gobierna el resto del dominio. Un Fork, en este modelo corregido, no es más que un componente cuyo `owner_team_id` se desvía del `owner_team_id` por defecto de su dominio contenedor.

**Regla de jerarquía de ownership** (de más general a más específico — el más específico siempre gana):

```
1. owner_team_id del Dominio           → aplica a TODOS sus componentes por defecto
2. owner_team_id_override en un componente individual → si existe, ANULA el del dominio
                                          (este es el mecanismo de Fork con gobierno propio)
```

Cualquier componente (BC, MC, MD, DT, CS) puede declarar `owner_team_id_override` en su front matter cuando su equipo dueño difiere del equipo dueño del dominio que lo contiene. Si no lo declara, hereda el del dominio.



```
canonico-banco/
│
├── _teams/                            ← NUEVO: fichas de Equipos Productores (entidad de gobierno real)
│   ├── TEAM-BANCA-PERSONAL.md         ← dueño de DOM-CREDITO-CONSUMO y otros dominios
│   ├── TEAM-CONVENIOS-LIBRANZA.md     ← dueño del fork BC-CUS-CC-001-v1 (gobierno independiente)
│   └── TEAM-PAGOS.md                  ← dueño de DOM-MEDIOS-PAGO
│
├── _canonical-standards/              ← Estándares externos vendorizados (solo lectura/referencia)
│   ├── iso20022/
│   │   ├── ISO-PACS-008-v08.md        ← Ficha del MD pacs.008.001.08 tal cual lo define ISO
│   │   ├── ISO-PACS-008-v10.md        ← Versión más reciente del mismo estándar
│   │   └── ISO-CAMT-053-v02.md
│   └── bian/
│       ├── BIAN-SD-ConsumerLoan-v11.md
│       └── BIAN-SD-ConsumerLoan-v12.md
│
├── _mappings/                         ← Documentos de mapeo detallado (estrategia B)
│   ├── MAP-CUS-CC-001-ISO-PACS-008.md
│   └── MAP-CUS-MP-002-BIAN-PaymentExecution.md
│
├── _datatypes/
├── _codesets/
├── _templates/
│
└── dominios/
    └── DOM-CREDITO-CONSUMO/               ← propiedad de TEAM-BANCA-PERSONAL (ver Dominio-*.md → owner_team)
        ├── Dominio-CreditoConsumo.md
        │
        ├── business-components/
        │   ├── BC-CUS-CC-001-CreditoConsumo.md          ← markdown del BC
        │   ├── BC-CUS-CC-001-CreditoConsumo.yaml         ← schema OAS individual del BC (mismo nombre base)
        │   ├── BC-CUS-CC-001-v1-CreditoConsumoLegacy.md  ← fork de rama MAJOR (ver sección 2)
        │   └── BC-CUS-CC-001-v1-CreditoConsumoLegacy.yaml
        │
        ├── message-components/
        │   ├── MC-CUS-CC-001-ResumenCreditoVigente.md
        │   └── MC-CUS-CC-001-ResumenCreditoVigente.yaml  ← schema OAS individual del MC
        │
        ├── message-definitions/
        │   ├── MD-CUS-CC-001-ConsultaCreditosClienteResponse.md
        │   └── MD-CUS-CC-001-ConsultaCreditosClienteResponse.yaml  ← fragmento OAS (paths + schema ensamblado)
        │
        └── oas/
            ├── oas-credito-consumo.yaml          ← OAS FINAL ensamblado — rama trunk
            └── oas-credito-consumo-legacy.yaml   ← OAS FINAL ensamblado — rama fork (BC-CUS-CC-001-v1)
```

**Regla de carpeta**: `_canonical-standards/` contiene las fichas de los estándares **tal cual los publica el organismo** (ISO, BIAN) — son de solo lectura/referencia, no se editan salvo para registrar una nueva versión publicada por el estándar. Los componentes custom del banco siempre viven en `dominios/`, nunca en `_canonical-standards/`.

> **Nota sobre `_teams/` y `dominios/`** (ver sección 1.2-bis para el detalle completo): un equipo productor puede ser dueño de **varios** dominios. La carpeta sigue organizándose por dominio de negocio (`dominios/DOM-X/`), no por equipo — eso mantiene la navegación temática intuitiva. Pero el equipo productor es la entidad de **gobierno real**: cada `Dominio-*.md` declara su `owner_team_id` apuntando a una ficha en `_teams/`, y esa ficha es la que centraliza qué dominios, BCs y forks son responsabilidad de ese equipo, sin importar en qué carpeta temática vivan.

### 1.3-bis Modelo mixto de archivos OAS: individual junto al .md + ensamblado por dominio/rama

V2 adopta un modelo de **dos niveles** para los artefactos OAS, en vez de un único yaml consolidado por dominio (que era el modelo V1):

| Nivel | Quién lo tiene | Dónde vive | Propósito |
| ----- | -------------- | ---------- | --------- |
| **Individual** | BC, MC, DataType, Code-set | Junto a su propio `.md`, mismo nombre base | Aislamiento de cambios: modificar un BC solo toca su yaml, sin tocar el de otros componentes. Es la "pieza de Lego". |
| **Ensamblado** | MessageDefinition → OAS por dominio/rama | `message-definitions/MD-*.yaml` (fragmento) y `oas/oas-*.yaml` (documento OAS completo, publicable) | El MD es el contrato real que ve un consumidor de API; necesita verse completo en un solo lugar. Es "la caja armada". |

**Por qué este corte y no otro**: BC/MC/DT/CS son unidades de modelado que evolucionan a su propio ritmo y se benefician de archivos pequeños y aislados (menos conflictos de Git, blast radius de revisión acotado). El MD, en cambio, es el punto de ensamblaje natural de la jerarquía (`MD contiene MCs, MC referencia BCs`) y el contrato final que se publica; fragmentarlo en pedazos sueltos rompería la propiedad de poder leer un endpoint completo en un solo archivo.

**Flujo de construcción** (automatizado en CI/CD, ver sección 8 — Pipeline):

```
1. BC-CUS-CC-001-CreditoConsumo.yaml         (schema individual del BC)
2. MC-CUS-CC-001-ResumenCreditoVigente.yaml  (schema individual del MC, con $ref al BC anterior)
   │
   ▼ build (CI/CD resuelve $ref relativos y los re-ancla)
3. MD-CUS-CC-001-ConsultaCreditosClienteResponse.yaml  (fragmento: paths + schema final del MD)
   │
   ▼ build (CI/CD agrupa todos los MD de la misma rama del dominio)
4. oas/oas-credito-consumo.yaml              (OAS publicable, rama trunk)
   oas/oas-credito-consumo-legacy.yaml       (OAS publicable, rama fork)
```

**Regla de oro**: los yaml individuales (nivel 1) y los fragmentos de MD (nivel 2) **no se publican ni se exponen a consumidores externos** — son artefactos de construcción. Solo `oas/oas-*.yaml` es el contrato publicado. Esto es análogo a tener archivos fuente (`.ts`) y un bundle final (`.js`): ambos viven en el repo, pero solo uno se sirve.

### 1.4 Convención de ID con source embebido

```
BC-{SOURCE}-{DOMINIO}-{NNN}
MC-{SOURCE}-{DOMINIO}-{NNN}
MD-{SOURCE}-{DOMINIO}-{NNN}
DT-{SOURCE}-{DOMINIO}-{NNN}
CS-{SOURCE}-{DOMINIO}-{NNN}
```

| SOURCE | Significado | Ejemplo |
| ------ | ----------- | ------- |
| `CUS` | Custom Banco | `BC-CUS-CC-001` |
| `ISO` | ISO 20022 | `BC-ISO-PACS-002` (ficha de referencia del estándar) |
| `BIAN` | BIAN | `BC-BIAN-SD-001` (ficha de referencia del estándar) |

**Nota importante**: los componentes con `source: ISO` o `source: BIAN` que viven en `_canonical-standards/` representan la ficha **del estándar mismo** dentro del repositorio (para que agentes IA y personas puedan consultarlo sin salir del repo). Los componentes custom del banco casi siempre tendrán `source: CUS`, incluso cuando se alineen fuertemente a un estándar — el source describe el origen del documento, no si tiene relación con un estándar (esa relación se declara en `standard_alignment_strategy`, sección 1.2).

---

## 2. Multi-MAJOR con ciclo de vida independiente

### 2.1 El problema que resuelve

En V1, cuando un BC sube de MAJOR (ej. 1.x → 2.x), la versión 1.x entra en `Deprecated` con una fecha de `Sunset`: es una transición temporal hacia la extinción. En V2 reconocemos que en banca esto no siempre es así: dos ramas MAJOR pueden coexistir **de forma permanente y legítima**, por ejemplo porque atienden a reguladores distintos, a productos con reglas de negocio que se bifurcaron de verdad, o porque un canal legado simplemente no va a migrar en el horizonte planeado.

### 2.2 Dos estrategias de branching MAJOR

El equipo productor declara, en el front matter del componente, qué estrategia aplica:

```yaml
major_branch_strategy: "Evolution"   # o "Fork"
```

#### Estrategia "Evolution" (default, comportamiento V1)

Un solo documento, un solo ID. Las versiones MAJOR anteriores se documentan en el changelog y eventualmente se deprecan y sunsetean. Es lo que ya existía en V1 — se mantiene como comportamiento por defecto.

#### Estrategia "Fork" (nuevo en V2)

Cuando una rama MAJOR se distancia lo suficiente como para merecer gobierno propio, el equipo productor la convierte en un **ID hermano**, con su propio documento, su propio owner, su propio estado de ciclo de vida — independiente del resto de ramas.

```
BC-CUS-CC-001          (rama tronco / v2.x.x en adelante — la "principal")
BC-CUS-CC-001-v1       (fork de la rama v1.x.x — congelada con gobierno propio)
```

Ambos documentos existen simultáneamente y de forma indefinida (no hay obligación de sunset). Se relacionan mediante un bloque `branch_lineage` en el front matter de cada uno:

```yaml
# En BC-CUS-CC-001-v1-CreditoConsumoLegacy.md
branch_lineage:
  forked_from: "BC-CUS-CC-001"
  fork_reason: "Producto de libranza legado con reglas regulatorias propias del convenio 2024; no se proyecta migración a v2.x.x en el corto/mediano plazo."
  fork_date: "2026-03-01"
  sibling_branches:
    - id: "BC-CUS-CC-001"
      version_range: "2.x.x+"
      relationship: "trunk"

# En BC-CUS-CC-001-CreditoConsumo.md (la rama principal)
branch_lineage:
  sibling_branches:
    - id: "BC-CUS-CC-001-v1"
      version_range: "1.x.x"
      relationship: "fork"
      fork_date: "2026-03-01"
      fork_reason: "Producto de libranza legado; ver doc del fork."
```

### 2.3 Gobierno independiente por rama (Fork)

Cada fork tiene su propio bloque de gobernanza completo — puede tener owner funcional, owner técnico, comité aprobador, e incluso política de versionamiento MINOR/PATCH **distintos** del tronco:

| Campo | BC-CUS-CC-001 (tronco) | BC-CUS-CC-001-v1 (fork) |
| ----- | ----------------------- | ------------------------- |
| `owner_functional` | Vicepresidencia de Banca Personal | Gerencia de Convenios y Libranza |
| `status` | Active | Active (¡no Deprecated! — gobierno propio, vigente indefinidamente) |
| `approval_board` | Comité de Arquitectura de Crédito | Comité de Convenios Libranza |
| `current_version` | 2.1.0 | 1.4.2 |
| Política de coexistencia | N/A (es el tronco) | No aplica sunset — declarado como "Permanent fork", revisión anual de vigencia |

### 2.4 Cuándo usar Evolution vs. Fork — guía de decisión

| Señal | Estrategia recomendada |
| ----- | ----------------------- |
| La MAJOR nueva es un superset/breaking change normal, con plan de migración y fecha de sunset razonable (<18 meses) | **Evolution** |
| Hay un compromiso contractual o regulatorio que ata a un grupo de consumidores a la versión antigua indefinidamente | **Fork** |
| Las reglas de negocio entre versiones se bifurcaron tanto que mantenerlas en un solo doc generaría confusión semántica | **Fork** |
| Un equipo distinto al productor original asume la responsabilidad de la versión antigua | **Fork** |
| Es incertidumbre temporal nada más ("todavía no sabemos cuándo migran") | **Evolution** (no fork solo por indecisión; el fork implica compromiso de gobierno separado) |

**Regla de oro**: el Fork no es un atajo para evitar deprecar algo. Es una declaración formal de que dos líneas de un mismo concepto de negocio van a coexistir con gobierno propio. Requiere aprobación del Comité de Arquitectura Empresarial, no solo del comité de dominio.

---

## 3. Documento de mapping (estrategia B de la sección 1.2)

Cuando la relación con un estándar es de tipo **Mapping**, se genera un documento dedicado en `_mappings/`. Convención de nombre: `MAP-{ID_COMPONENTE_CUSTOM}-{ID_COMPONENTE_ESTANDAR}.md`.

Este documento contiene:
- Identificación de ambos componentes (custom y estándar) con enlaces a sus fichas completas.
- Tabla de mapeo campo a campo con tipo de correspondencia (Equivalente / Renombrado / Calculado / Sin equivalencia).
- Versión de cada lado vigente al momento del mapeo (el mapeo mismo tiene versión propia, porque puede romperse si cualquiera de los dos lados cambia).
- Gaps explícitos en ambas direcciones.

El BC custom mantiene una **sección resumen** (no la tabla completa) que enlaza a este documento — así la ficha del BC no se infla, pero la trazabilidad es de un clic.

---

## 4. Impacto en plantillas existentes

| Plantilla | Cambio requerido en V2 | Estado |
| --------- | ------------------------ | ------ |
| `Plantilla_BC_Generica.md` | Agregar bloque `source`, `standard_alignment_strategy`, `standard_reference`, `major_branch_strategy`, `branch_lineage` al front matter y nueva sección `## Standard alignment` | ✅ `v2/Plantilla_BC_Generica_V2.md` |
| `Plantilla_MessageComponent.md` | Mismo tratamiento que BC, más declaración explícita de **qué rama** del BC/MC origen consume cada MC | ✅ `v2/Plantilla_MessageComponent_V2.md` |
| `Plantilla_CodeSet.md` | Mismo tratamiento; el caso típico de Fork aquí es "lista completa del estándar" vs. "subconjunto operativo habilitado por el banco" | ✅ `v2/Plantilla_CodeSet_V2.md` |
| Nuevo: `Plantilla_StandardReference.md` | Para fichar un componente ISO 20022 o BIAN tal cual, en `_canonical-standards/` | ✅ `v2/Plantilla_StandardReference_V2.md` |
| Nuevo: `Plantilla_Mapping.md` | Para el documento de mapeo campo a campo en `_mappings/` | ✅ `v2/Plantilla_Mapping_V2.md` |
| `_catalog/catalog.yaml` | Agregar `source`, `standard_alignment_strategy` y `branch_lineage` a cada entrada | ✅ `v2/_catalog_catalog_V2.yaml` |
| `_catalog/dependency-graph.yaml` | Agregar grafo de `forked_from` / `sibling_branches` además del grafo de consumo BC→MC→MD | ✅ `v2/_catalog_dependency-graph_V2.yaml` |
| `oas-template-base.yaml` | `x-canonical-metadata` debe incluir `source` y, si aplica, `branch_id` | ✅ `v2/oas-template-base_V2.yaml` |
| **Nuevo (cambio de modelo de archivos)**: cada `.md` de BC/MC/DT/CS debe tener su yaml individual hermano (mismo nombre base) | Agregar campo `individual_oas_file` al front matter y actualizar la convención de `oas_schema_ref` para apuntar al yaml individual en vez de al consolidado | ✅ Propagado a BC, MC y CodeSet — ver sección 1.3-bis y 6-bis |
| **Nuevo**: `Plantilla_MessageDefinition.md` | Formaliza el "ensamblaje": MD = paths + schema final, con su propio yaml fragmento (`assembled_fragment_file`) y registro de en qué OAS termina publicado (`published_in_oas`) | ✅ `v2/Plantilla_MessageDefinition_V2.md` |
| **Nuevo**: pipeline de build OAS (BC/MC/DT/CS individuales → MD ensamblado → OAS por dominio/rama) | Documentar el proceso de CI/CD que resuelve `$ref` y produce el OAS publicable | ✅ Sección 1.3-bis y 6-ter (este documento) |
| **Nuevo**: bundling/dereferencing para gateways autocontenidos (APIConnect) | Etapa de build que produce `oas/dist/*.bundled.yaml`, sin `$ref` externos | ✅ Sección 6-quater (este documento) |
| **Nuevo**: `Plantilla_ProducerTeam.md` | Formaliza al Equipo Productor como entidad de gobierno real (no el dominio); reemplaza `owner_functional`/`approval_board` sueltos en BC/MC/CS/MD por `owner_team_id` / `owner_team_id_override` que apuntan a una ficha en `_teams/` | ✅ `v2/Plantilla_ProducerTeam_V2.md` — propagado a `Plantilla_BC_Generica_V2.md`, `Plantilla_MessageComponent_V2.md`, `Plantilla_CodeSet_V2.md`, `Plantilla_MessageDefinition_V2.md`, `catalog.yaml` y `dependency-graph.yaml` (grafo 4: `governance_graph` + `resolved_ownership_index`) |

**Estado V2: completo.** Las 13 plantillas/artefactos identificados en la sección 4 están actualizados a V2: multi-source, multi-branch, modelo mixto de archivos OAS (individual + ensamblado + bundled), y gobierno real por Equipo Productor (independiente de la organización temática por dominio).

Estas actualizaciones se generan a continuación como artefactos V2 independientes (no se sobreescriben los de V1).

---

## 6-bis. El modelo mixto también aplica a DataTypes y Code-sets

En V1, `_datatypes/` y `_codesets/` tenían un único yaml consolidado (`datatypes-common.yaml`, `codesets-common.yaml`) — el mismo patrón "todo junto" que V1 usaba para los dominios. Por coherencia con la decisión de la sección 1.3-bis, V2 aplica el mismo criterio aquí: **cada DataType y cada Code-set individual tiene su propio yaml**, junto a su markdown.

```
_datatypes/
├── DT-CUS-COM-001-MonedaCOP.md
├── DT-CUS-COM-001-MonedaCOP.yaml          ← NUEVO en V2: individual, no consolidado
├── DT-CUS-COM-002-FechaISO8601.md
├── DT-CUS-COM-002-FechaISO8601.yaml
└── _datatypes-index.yaml                   ← índice liviano (solo lista de $ref), reemplaza al consolidado

_codesets/
├── CS-ISO-COM-001-CodigoMonedaISO4217.md
├── CS-ISO-COM-001-CodigoMonedaISO4217.yaml ← NUEVO en V2: individual
├── CS-ISO-COM-002-CodigoPaisISO3166.md
├── CS-ISO-COM-002-CodigoPaisISO3166.yaml
└── _codesets-index.yaml                     ← índice liviano
```

`_datatypes-index.yaml` y `_codesets-index.yaml` **no son el yaml consolidado de V1** — son archivos livianos que solo contienen un mapa `id → ruta relativa`, para que cualquier BC/MC que necesite referenciar un DataType o Code-set sepa a qué archivo individual apuntar sin tener que listar el directorio:

```yaml
# _datatypes/_datatypes-index.yaml
DT-CUS-COM-001: "./DT-CUS-COM-001-MonedaCOP.yaml"
DT-CUS-COM-002: "./DT-CUS-COM-002-FechaISO8601.yaml"
```

La referencia desde un BC cambia en consecuencia:

```yaml
# Antes (V1, consolidado):
moneda:
  $ref: '../../../_codesets/codesets-common.yaml#/components/schemas/CodigoMonedaISO4217'

# Ahora (V2, individual):
moneda:
  $ref: '../../../_codesets/CS-ISO-COM-001-CodigoMonedaISO4217.yaml#/components/schemas/CodigoMonedaISO4217'
```

---

## 6-ter. Pipeline de build del OAS (BC/MC/DT/CS individuales → MD ensamblado → OAS publicable)

Este pipeline es una extensión del pipeline CI/CD de la sección 8 (que se mantiene igual en su estructura general). El paso nuevo en V2 es la etapa de **build/ensamblaje**, que ocurre después de la validación y antes de la publicación:

```
Pull Request (cambio en un BC-CUS-CC-001-CreditoConsumo.yaml)
  │
  ├── [pipeline existente, sección 8: lint, trazabilidad, detección de tipo de cambio]
  │
  └── Merge a main
        │
        ├── ETAPA DE BUILD (nueva en V2):
        │   │
        │   ├── 1. Identificar qué MDs consumen (directa o transitivamente)
        │   │      el BC/MC/DT/CS modificado (consultar dependency-graph.yaml)
        │   │
        │   ├── 2. Para cada MD afectado: resolver sus $ref a los yaml
        │   │      individuales de BC/MC/DT/CS y regenerar el fragmento
        │   │      MD-*.yaml con el schema final ensamblado
        │   │
        │   ├── 3. Para cada OAS de dominio/rama afectado: regenerar
        │   │      oas/oas-*.yaml agrupando todos sus MD fragments
        │   │      + paths + security + responses estándar
        │   │      (este archivo AÚN tiene $ref entre sus propios
        │   │      components/schemas — es el documento "fuente
        │   │      ensamblada", versionado en Git, legible en diffs)
        │   │
        │   ├── 4. BUNDLING / DEREFERENCING (nuevo — ver 6-quater):
        │   │      tomar oas/oas-*.yaml y producir
        │   │      oas/dist/oas-*.bundled.yaml: un documento ÚNICO,
        │   │      sin ningún $ref a archivos externos. Los $ref
        │   │      externos (a _codesets/, _datatypes/, a otros
        │   │      MD/MC) se inlinean dentro de #/components/schemas
        │   │      del mismo archivo. Los $ref INTERNOS resultantes
        │   │      (#/components/schemas/X) se conservan — son
        │   │      válidos para APIConnect.
        │   │
        │   └── 5. spectral lint sobre oas/dist/oas-*.bundled.yaml
        │          (el artefacto que realmente se va a desplegar,
        │          no el fuente con $ref externos)
        │
        ├── Regenerar _catalog/catalog.yaml
        ├── Regenerar _catalog/dependency-graph.yaml
        ├── Actualizar índice RAG (embeddings)
        └── Notificar MCP server (invalidar caché de artefactos modificados)
```

**Regla de oro del build**: hay **tres niveles** de artefacto OAS, no dos:

| Nivel | Archivo | $ref permitidos | Quién lo edita | Quién lo consume |
| ----- | ------- | ------------------ | -------------- | -------------------- |
| 1. Fuente individual | `BC-*.yaml`, `MC-*.yaml`, `DT-*.yaml`, `CS-*.yaml` | externos (entre ellos) | Equipo productor (vía PR) | El build (etapa 2-3) |
| 2. Ensamblado (fuente legible) | `oas/oas-*.yaml` | externos (a `_codesets/`, `_datatypes/`) | **Nadie** — generado por build | Revisores humanos (diff legible en PR), el build (etapa 4) |
| 3. Bundled (publicable) | `oas/dist/oas-*.bundled.yaml` | solo internos (`#/components/schemas/X`) | **Nadie** — generado por build | **APIConnect** (o cualquier gateway que requiera autocontención) |

Ninguno de los tres niveles se edita a mano más allá del nivel 1 (los yaml individuales de BC/MC/DT/CS, que sí son fuente real). Los niveles 2 y 3 son derivados — exactamente como código fuente vs. bundle minificado en un proyecto frontend.

---

## 6-quater. Bundling para gateways autocontenidos (APIConnect y similares)

### El problema

APIConnect (igual que Apigee, Kong o AWS API Gateway) **no resuelve `$ref` a archivos externos** al momento de importar/publicar un OAS. Solo acepta:
- Un único documento YAML/JSON.
- `$ref` permitidos: únicamente internos, del tipo `#/components/schemas/NombreSchema`.
- `$ref` externos (`../../_codesets/CS-XXX.yaml#/...`, `./MC-XXX.yaml#/...`) → **rechazados o ignorados silenciosamente**, dependiendo de la versión del gateway. Esto es el riesgo real: en el peor caso, no falla la importación pero el schema queda incompleto en producción.

Esto entra en tensión directa con el modelo de archivos individuales que diseñamos (BC/MC/DT/CS con su propio yaml, referenciados por `$ref` entre ellos) — pero **no invalida el modelo**; solo significa que ese modelo describe el nivel 1 y 2 (fuente y ensamblado), y necesita un paso más para llegar al nivel 3 (publicable).

### La solución: bundling automático

El **bundling** (también llamado "dereferencing" o "inlining") es un paso estándar de tooling OpenAPI que toma un documento con `$ref` externos y produce un documento equivalente donde:
1. Cada `$ref` externo se reemplaza por una copia del schema referenciado, insertada dentro de `#/components/schemas/` del mismo archivo.
2. Las referencias que antes apuntaban afuera ahora apuntan internamente al schema recién insertado (`$ref: '#/components/schemas/CodigoMonedaISO4217'`).
3. Si el mismo schema externo es referenciado por múltiples lugares, se inserta **una sola vez** y todos apuntan al mismo `$ref` interno (evita duplicación).

**Herramientas recomendadas** (cualquiera resuelve esto sin necesidad de escribir lógica propia):

| Herramienta | Tipo | Comando típico |
| ------------ | ---- | ---------------- |
| `@redocly/cli` | CLI Node.js | `redocly bundle oas/oas-credito-consumo.yaml -o oas/dist/oas-credito-consumo.bundled.yaml` |
| `swagger-cli` | CLI Node.js | `swagger-cli bundle oas/oas-credito-consumo.yaml -o oas/dist/oas-credito-consumo.bundled.yaml --dereference` |
| `openapi-generator` | CLI Java | tiene modo `bundle` equivalente |

Cualquiera de estas se integra como un solo paso en el pipeline CI/CD (etapa 4 de la sección 6-ter), sin necesidad de mantenerlo a mano.

### Ejemplo concreto: antes y después del bundling

**Antes (`oas/oas-credito-consumo.yaml`, nivel 2 — fuente ensamblada, con `$ref` externos)**:

```yaml
components:
  schemas:
    CreditoConsumo:
      type: object
      properties:
        moneda:
          $ref: '../../../_codesets/CS-ISO-COM-001-CodigoMonedaISO4217.yaml#/components/schemas/CodigoMonedaISO4217'
        montoDesembolsado:
          $ref: '../../../_datatypes/DT-CUS-COM-003-MontoCOP.yaml#/components/schemas/MontoCOP'
```

**Después (`oas/dist/oas-credito-consumo.bundled.yaml`, nivel 3 — publicable en APIConnect)**:

```yaml
components:
  schemas:
    CreditoConsumo:
      type: object
      properties:
        moneda:
          $ref: '#/components/schemas/CodigoMonedaISO4217'      # ahora interno
        montoDesembolsado:
          $ref: '#/components/schemas/MontoCOP'                  # ahora interno

    # Inyectado por el bundler — copia del schema antes externo
    CodigoMonedaISO4217:
      type: string
      enum: [COP, USD, EUR, MXN, PEN]
      description: "Código de moneda según ISO 4217. Code-set: CS-ISO-COM-001."

    # Inyectado por el bundler — copia del schema antes externo
    MontoCOP:
      type: number
      minimum: 0
      description: "Monto expresado en pesos colombianos."
```

El documento resultante es 100% autocontenido: un solo archivo, todos los `$ref` resuelven dentro de sí mismo, exactamente lo que APIConnect requiere.

### Qué se pierde y qué se gana con el bundling

| Aspecto | `oas/oas-*.yaml` (ensamblado) | `oas/dist/oas-*.bundled.yaml` (publicable) |
| ------- | -------------------------------- | ------------------------------------------- |
| Trazabilidad a BC/MC/CS/DT origen | Visible vía path del `$ref` | Se pierde el path, pero `x-canonical-metadata` (con `artifact_id`) se conserva dentro de cada schema inyectado — la trazabilidad sigue intacta para agentes IA, solo cambia el mecanismo |
| Legibilidad en diff de PR | Alta (cambios pequeños y localizados) | Baja (un cambio en un Code-set se ve duplicado en cada OAS que lo usa) — por eso este archivo NO se versiona como objetivo de revisión humana, solo como artefacto de despliegue |
| Tamaño de archivo | Pequeño | Más grande (todo inline) |
| Compatible con APIConnect | ❌ No | ✅ Sí |

**Regla de oro**: los revisores humanos revisan PRs sobre el nivel 1 (yaml individuales) y leen el nivel 2 (`oas/oas-*.yaml`) para tener contexto del documento completo. **Nadie revisa el nivel 3** línea por línea — es un artefacto de build, se valida automáticamente (spectral + smoke test de import contra un APIConnect de sandbox) y se despliega.

### Dónde vive el artefacto bundled

```
dominios/DOM-CREDITO-CONSUMO/
└── oas/
    ├── oas-credito-consumo.yaml              ← nivel 2, en Git, fuente de verdad legible
    ├── oas-credito-consumo-legacy.yaml       ← nivel 2, rama fork
    └── dist/                                  ← nivel 3, GENERADO, no se edita
        ├── oas-credito-consumo.bundled.yaml      ← esto se sube a APIConnect (rama trunk)
        └── oas-credito-consumo-legacy.bundled.yaml  ← esto se sube a APIConnect (rama fork)
```

`oas/dist/` puede o no versionarse en Git según la política del equipo de DevOps (algunos prefieren regenerarlo siempre en el pipeline de despliegue y no commitearlo; otros prefieren commitearlo para tener un artefacto inmutable por release). Ambas opciones son válidas dentro de este modelo — lo único no negociable es que **nunca se edita a mano**.

---

## 5. Checklist adicional V2 (complementa el checklist V1)

### Por componente con relación a estándar
- [ ] `standard_alignment_strategy` declarada (Reference / Mapping / Gap-fit).
- [ ] Si es Mapping: documento en `_mappings/` existe y está enlazado.
- [ ] Si es Gap-fit: `extensions` y `gaps` documentados explícitamente.
- [ ] El estándar referenciado existe como ficha en `_canonical-standards/` (o se crea si es la primera vez que se usa).

### Por componente con múltiples ramas MAJOR
- [ ] `major_branch_strategy` declarada (Evolution / Fork) para cada transición MAJOR.
- [ ] Si es Fork: `branch_lineage` completo en ambos documentos (tronco y fork).
- [ ] Si es Fork: gobierno propio declarado (owner, comité, política de coexistencia) y aprobado por Comité de Arquitectura Empresarial.
- [ ] El catálogo (`catalog.yaml`) refleja todas las ramas activas, no solo la "current_version" del tronco.

### Por gobierno vía Equipo Productor (nuevo en V2)
- [ ] Todo dominio (`Dominio-*.md`) declara `owner_team_id` apuntando a una ficha real en `_teams/`. NUNCA un email o nombre de área suelto.
- [ ] Ningún BC/MC/CS/MD repite `owner_functional`/`owner_technical`/`approval_board` en su propio front matter — esa información vive UNA sola vez en la ficha del equipo.
- [ ] Si un componente individual tiene gobierno distinto al de su dominio contenedor (típicamente un Fork): declara `owner_team_id_override`, NUNCA campos de gobierno sueltos.
- [ ] Cada ficha en `_teams/` tiene sus tablas "Dominios bajo gobierno" y "Componentes con ownership específico" sincronizadas en ambas direcciones con `catalog.yaml` (lo que el equipo dice que gobierna = lo que el dominio/componente dice que lo gobierna).
- [ ] Code-sets/DataTypes con `domain_id: GLOBAL` declaran `owner_team_id` directo (no pueden heredar de un dominio que no tienen).
- [ ] `dependency-graph.yaml` tiene `resolved_ownership_index` actualizado: cada component_id y domain_id resuelve a exactamente un `team_id`, sin ambigüedad.
- [ ] Antes de aprobar cualquier cambio, se resuelve el comité correcto consultando `resolved_owner_team_id` — nunca asumiendo que "el comité del dominio" es automáticamente el correcto (puede estar overrideado).

### Por modelo mixto de archivos OAS (nuevo en V2)
- [ ] Todo `.md` de BC/MC/DataType/Code-set tiene su yaml individual hermano (mismo nombre base, misma carpeta).
- [ ] El campo `individual_oas_file` en el front matter coincide con el nombre real del archivo.
- [ ] Ningún yaml individual de BC/MC/DT/CS se referencia directamente desde fuera del repositorio (son fuente de build, no contrato publicado).
- [ ] Todo MD tiene su `assembled_fragment_file` generado y su tabla `Composed from` actualizada con la rama exacta de cada MC consumido.
- [ ] `oas/oas-*.yaml` nunca se edita a mano; cualquier edición manual detectada se sobreescribe en el siguiente build.
- [ ] Si el dominio tiene componentes con Fork: existen archivos OAS publicados separados por rama, nunca mezclados en un solo archivo.
- [ ] `_datatypes-index.yaml` y `_codesets-index.yaml` están sincronizados con los archivos individuales reales (sin entradas huérfanas ni faltantes).

### Por despliegue en gateways autocontenidos (APIConnect y similares — nuevo en V2)
- [ ] El pipeline genera `oas/dist/oas-*.bundled.yaml` para cada `oas/oas-*.yaml` publicado (uno por rama si aplica Fork).
- [ ] El archivo bundled no contiene ningún `$ref` a rutas externas (`../`, `./otro-archivo.yaml`); solo `$ref` internos (`#/components/schemas/...`).
- [ ] spectral lint corre sobre el archivo **bundled**, no sobre el ensamblado con `$ref` externos.
- [ ] Existe un smoke test de import contra un ambiente sandbox de APIConnect antes de publicar a producción.
- [ ] El archivo bundled conserva `x-canonical-metadata` en cada schema inyectado, para no perder trazabilidad aunque se haya perdido el path del `$ref` original.
- [ ] Nadie edita manualmente `oas/dist/*.bundled.yaml`; cualquier fix se hace en el nivel 1 (yaml individual) y se vuelve a generar.
