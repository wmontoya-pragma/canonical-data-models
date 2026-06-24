# Arquitectura del Repositorio de Gobierno de Datos Canónico

**Versión**: 1.0.0  
**Fecha**: 2026-06-16  
**Owner**: Oficina de Arquitectura Empresarial  
**Contacto**: arquitectura@banco.com

---

## 1. Propósito

Este documento define la arquitectura del repositorio canónico de gobierno de datos del banco. El repositorio es la **fuente de verdad única** para:

- Dominios canónicos y sus Business Components (BC).
- Message Components (MC) y Message Definitions (MD) usados en los OAS de las APIs.
- Schemas OAS 3.0 alineados con el modelo canónico.
- Políticas de gobernanza y guías de versionamiento.

El repositorio está diseñado para ser consumido tanto por **personas** (arquitectos, desarrolladores, analistas) como por **agentes IA** (asistentes de código, pipelines de validación, generadores de borradores).

---

## 2. Capacidades IA objetivo

El repositorio debe habilitar los siguientes casos de uso de IA:

| Capacidad | Descripción | Requiere |
| --------- | ----------- | -------- |
| **Descubrimiento semántico** | "¿Qué BC modela el concepto de cuota de crédito?" | Embeddings + keywords en front matter |
| **Validación de alineación** | "¿Este OAS está alineado con el BC canónico?" | Trazabilidad mc→bc en MD + schema refs |
| **Generación de borradores** | "Genera un borrador de BC para GarantíaCredito" | Plantillas + ejemplos en el repositorio |
| **Análisis de impacto** | "¿Qué MDs y OAS se rompen si BC-CC-001 sube MAJOR?" | Grafo de dependencias en machine-readable summaries |
| **Generación de OAS** | "Genera el OAS para la API de consulta de créditos" | MD + MC + BC + DataTypes como contexto |

---

## 3. Estrategia de consumo IA — Recomendación

Se recomienda una arquitectura de **dos capas complementarias**:

```
┌─────────────────────────────────────────────────────┐
│                   AGENTE / LLM                       │
└──────────────────┬──────────────────────────────────┘
                   │
       ┌───────────┴────────────┐
       │                        │
┌──────▼──────┐        ┌────────▼────────┐
│  MCP Server │        │   RAG / Search  │
│  (acceso    │        │  (embeddings    │
│  navegable  │        │   semánticos)   │
│  por ID)    │        │                 │
└──────┬──────┘        └────────┬────────┘
       │                        │
       └───────────┬────────────┘
                   │
     ┌─────────────▼─────────────┐
     │   REPOSITORIO GIT         │
     │   (md + yaml por dominio) │
     └───────────────────────────┘
```

### Capa 1 — MCP Server (acceso estructurado por ID)

Un MCP server que expone los artefactos del repositorio como **resources navegables**:

- `get_domain(domain_id)` → retorna el documento de dominio.
- `get_bc(bc_id, version?)` → retorna el BC con su changelog y versiones.
- `get_mc(mc_id, version?)` → retorna el MC con su trazabilidad.
- `get_md(md_id, version?)` → retorna el MD con sus MCs.
- `get_oas(domain_id, oas_file)` → retorna el OAS yaml completo.
- `get_impact(bc_id, version)` → retorna todos los MCs/MDs que consumen ese BC en esa versión.
- `list_components(domain_id, type?)` → lista BCs, MCs, MDs de un dominio.

**Ventaja**: el agente puede navegar el grafo de dependencias con precisión quirúrgica, sin necesidad de leer todos los documentos.

### Capa 2 — RAG semántico (descubrimiento por concepto)

Un pipeline de embeddings sobre los markdown, indexando especialmente:
- `title`, `summary`, `ai_keywords`, `aliases`, `definition` de cada artefacto.
- La sección `## Definition` y `## Semantic notes` de cada BC/MC.

**Ventaja**: el agente puede responder "¿qué modela el concepto de mora?" sin conocer el ID exacto.

### Cuándo usar cada capa

| Consulta del agente | Capa recomendada |
| ------------------- | ---------------- |
| "¿Qué BC modela la cuota de crédito?" | RAG (concepto libre) |
| "Dame el changelog de BC-CC-001" | MCP (ID conocido) |
| "¿Qué OAS se ven impactados si BC-CC-001 sube MAJOR?" | MCP (get_impact) |
| "Genera un borrador de MC para el endpoint de consulta de créditos" | RAG (contexto) + MCP (artefactos existentes) |
| "Valida si este OAS usa la versión correcta del BC canónico" | MCP (get_bc + get_oas) |

---

## 4. Estructura del repositorio

```
canonico-banco/
│
├── README.md                          ← Índice general del repositorio
├── GOVERNANCE.md                      ← Política de gobernanza global
├── VERSIONING.md                      ← Guía de versionamiento global
│
├── _catalog/                          ← Catálogo maestro (IA entry point)
│   ├── catalog.yaml                   ← Índice machine-readable de TODOS los artefactos
│   └── dependency-graph.yaml          ← Grafo de dependencias BC→MC→MD→OAS
│
├── _templates/                        ← Plantillas para nuevos artefactos
│   ├── Plantilla_Domain.md
│   ├── Plantilla_BusinessComponent.md
│   ├── Plantilla_BC_Generica.md
│   ├── Plantilla_MessageComponent.md
│   ├── Plantilla_MessageDefinition.md
│   ├── Plantilla_DataType.md
│   ├── Plantilla_CodeSet.md
│   └── oas-template-base.yaml         ← Esqueleto OAS 3.0 base para nuevos dominios
│
├── _datatypes/                        ← DataTypes compartidos entre dominios
│   ├── DT-COM-001-MonedaCOP.md
│   ├── DT-COM-002-FechaISO8601.md
│   └── datatypes-common.yaml          ← OAS components/schemas de DataTypes comunes
│
├── _codesets/                         ← Code-sets (listas de valores controlados) compartidos
│   ├── CS-COM-001-CodigoMonedaISO4217.md
│   ├── CS-COM-002-CodigoPaisISO3166.md
│   ├── CS-COM-003-TipoDocumentoIdentidad.md
│   └── codesets-common.yaml           ← OAS components/schemas (enum) de code-sets comunes
│
└── dominios/
    │
    ├── DOM-CREDITO-CONSUMO/
    │   ├── Dominio-CreditoConsumo.md              ← Índice del dominio (inventario + hipervínculos)
    │   ├── GOVERNANCE-CreditoConsumo.md            ← Política de gobernanza del dominio
    │   │
    │   ├── business-components/
    │   │   ├── BC-CC-001-CreditoConsumo.md
    │   │   ├── BC-CC-002-CuotaCredito.md
    │   │   ├── BC-CC-003-DesembolsoCredito.md
    │   │   └── BC-CC-004-SolicitudCredito.md
    │   │
    │   ├── message-components/
    │   │   ├── MC-CC-001-ResumenCreditoVigente.md
    │   │   ├── MC-CC-002-DetalleCreditoCompleto.md
    │   │   └── MC-CC-010-ProximaCuotaResumen.md
    │   │
    │   ├── message-definitions/
    │   │   ├── MD-CC-001-ConsultaCreditosClienteResponse.md
    │   │   ├── MD-CC-002-ConsultaCreditosClienteRequest.md
    │   │   └── MD-CC-003-ConsultaCreditoIndividualResponse.md
    │   │
    │   └── oas/
    │       ├── oas-credito-consumo.yaml            ← OAS principal del dominio
    │       └── oas-credito-consumo-internal.yaml   ← OAS para consumo interno (si aplica)
    │
    ├── DOM-MEDIOS-PAGO/
    │   ├── Dominio-MediosPago.md
    │   ├── business-components/
    │   │   └── BC-MP-002-TransaccionPago.md
    │   ├── message-components/
    │   ├── message-definitions/
    │   └── oas/
    │       └── oas-medios-pago.yaml
    │
    └── DOM-FILIALES-OFFSHORE/
        ├── Dominio-FilialesOffShore.md
        ├── business-components/
        ├── message-components/
        ├── message-definitions/
        └── oas/
```

### Reglas de estructura

| Regla | Detalle |
| ----- | ------- |
| **Un directorio por dominio** | Agrupa todos los artefactos del equipo productor en un solo lugar. |
| **md y yaml juntos por dominio** | El OAS vive junto a los MDs y MCs que lo definen; se versiona en el mismo commit. |
| **`_catalog/` como entry point IA** | Los agentes no necesitan conocer la estructura de carpetas; el catálogo les da el mapa completo. |
| **`_datatypes/` compartido** | Los DataTypes comunes no pertenecen a ningún dominio; viven en un directorio global. |
| **`_templates/` versionadas** | Las plantillas son artefactos del repositorio, no documentos externos. |

---

## 5. El catálogo maestro (`_catalog/catalog.yaml`)

Este es el **entry point principal para agentes IA**. Contiene el índice machine-readable de todos los artefactos del repositorio, con sus rutas relativas, versiones y relaciones.

```yaml
# _catalog/catalog.yaml
# Generado automáticamente por CI/CD al hacer merge a main.
# NO editar manualmente.

catalog_version: "1.0.0"
generated_at: "2026-06-16T09:00:00-05:00"
repository: "https://github.com/banco/canonico-banco"

domains:
  - id: DOM-CREDITO-CONSUMO
    name: "Crédito de Consumo"
    status: Registered
    doc: "dominios/DOM-CREDITO-CONSUMO/Dominio-CreditoConsumo.md"
    governance: "dominios/DOM-CREDITO-CONSUMO/GOVERNANCE-CreditoConsumo.md"
    owner_team: "arquitectura-credito@banco.com"
    business_components:
      - id: BC-CC-001
        name: CreditoConsumo
        current_version: "2.1.0"
        status: Active
        doc: "dominios/DOM-CREDITO-CONSUMO/business-components/BC-CC-001-CreditoConsumo.md"
        oas_schema_ref: "dominios/DOM-CREDITO-CONSUMO/oas/oas-credito-consumo.yaml#/components/schemas/CreditoConsumo"
        keywords: [credito, prestamo, saldo, amortizacion, tasa]
        aliases: [Prestamo, ConsumerLoan, CreditoLibreInversion]
      - id: BC-CC-002
        name: CuotaCredito
        current_version: "1.3.0"
        status: Active
        doc: "dominios/DOM-CREDITO-CONSUMO/business-components/BC-CC-002-CuotaCredito.md"
        oas_schema_ref: "dominios/DOM-CREDITO-CONSUMO/oas/oas-credito-consumo.yaml#/components/schemas/CuotaCredito"
        keywords: [cuota, amortizacion, mora, instalment]
        aliases: [InstalmentPayment, PagoProgramado]
    message_components:
      - id: MC-CC-001
        name: ResumenCreditoVigente
        current_version: "1.1.0"
        status: Active
        doc: "dominios/DOM-CREDITO-CONSUMO/message-components/MC-CC-001-ResumenCreditoVigente.md"
        oas_schema_ref: "dominios/DOM-CREDITO-CONSUMO/oas/oas-credito-consumo.yaml#/components/schemas/ResumenCreditoVigente"
        consumes_bc:
          - id: BC-CC-001
            version: "2.1.0"
          - id: BC-CC-002
            version: "1.3.0"
        consumes_mc:
          - id: MC-CC-010
            version: "1.0.0"
    message_definitions:
      - id: MD-CC-001
        name: ConsultaCreditosClienteResponse
        current_version: "1.1.0"
        status: Active
        role: response
        doc: "dominios/DOM-CREDITO-CONSUMO/message-definitions/MD-CC-001-ConsultaCreditosClienteResponse.md"
        oas_file: "dominios/DOM-CREDITO-CONSUMO/oas/oas-credito-consumo.yaml"
        consumes_mc:
          - id: MC-CC-001
            version: "1.1.0"
    oas_files:
      - file: "dominios/DOM-CREDITO-CONSUMO/oas/oas-credito-consumo.yaml"
        version: "1.2.0"
        status: Active
```

---

## 6. El grafo de dependencias (`_catalog/dependency-graph.yaml`)

Permite que un agente responda en O(1) la pregunta: **"¿qué se rompe si cambio X?"**

```yaml
# _catalog/dependency-graph.yaml
# Generado automáticamente por CI/CD.

dependency_graph:

  BC-CC-001:
    version: "2.1.0"
    consumed_by_mc:
      - id: MC-CC-001
        version: "1.1.0"
        field_usage: [idCredito, tipoCredito, estadoCredito, saldoCapital, tasaEfectivaAnual, fechaVencimiento]
      - id: MC-CC-002
        version: "1.0.0"
        field_usage: [idCredito, idCliente, montoDesembolsado, tasaEfectivaAnual, plazoMeses, estadoCredito, fechaDesembolso, fechaVencimiento, saldoCapital, numeroCuotas]
    impact_surface:
      message_components: [MC-CC-001, MC-CC-002]
      message_definitions: [MD-CC-001, MD-CC-002, MD-CC-003, MD-APP-007]
      oas_files: [oas-credito-consumo.yaml, oas-app-movil.yaml]

  BC-CC-002:
    version: "1.3.0"
    consumed_by_mc:
      - id: MC-CC-010
        version: "1.0.0"
        field_usage: [idCuota, numeroCuota, valorCuota, fechaVencimientoCuota, estadoCuota]
    impact_surface:
      message_components: [MC-CC-010, MC-CC-001]
      message_definitions: [MD-CC-001, MD-CC-003]
      oas_files: [oas-credito-consumo.yaml]

  MC-CC-001:
    version: "1.1.0"
    consumed_by_md:
      - id: MD-CC-001
        version: "1.1.0"
      - id: MD-CC-003
        version: "1.0.0"
      - id: MD-APP-007
        version: "2.0.0"
    impact_surface:
      message_definitions: [MD-CC-001, MD-CC-003, MD-APP-007]
      oas_files: [oas-credito-consumo.yaml, oas-app-movil.yaml]
```

---

## 7. Convenciones IA-friendly en los markdown

Para que los agentes puedan procesar los documentos de forma confiable, **todos los artefactos deben cumplir**:

### 7.1 Front matter obligatorio (YAML)

Todo documento debe tener front matter YAML con los campos que permiten indexación:

```yaml
---
doc_type: "canonical-business-component"   # tipo exacto del artefacto
bc_id / mc_id / md_id: "XX-YY-NNN"        # ID estable y único
domain_id: "DOM-NOMBRE"                    # dominio al que pertenece
version: "X.Y.Z"                           # versión semántica actual
status: "Active"                           # estado del ciclo de vida
ai_keywords: [keyword1, keyword2]          # términos de búsqueda controlados
---
```

### 7.2 Sección `## Machine-readable summary` obligatoria

Cada BC, MC y MD debe tener un bloque YAML al final con su resumen estructurado. Este bloque es el que el pipeline de CI/CD usa para generar el `catalog.yaml` y el `dependency-graph.yaml` automáticamente.

```yaml
# En BC:
business_component_id: BC-CC-001
composed_from: ...

# En MC:
message_component_id: MC-CC-001
composed_from:
  business_components: [...]
  message_components: [...]

# En MD:
message_definition_id: MD-CC-001
composed_from:
  message_components: [...]
```

### 7.3 IDs estables y predecibles

| Tipo | Patrón | Ejemplo |
| ---- | ------ | ------- |
| Dominio | `DOM-NOMBRE-SUBDOMINIO` | `DOM-CREDITO-CONSUMO` |
| Business Component | `BC-XX-NNN` | `BC-CC-001` |
| Message Component | `MC-XX-NNN` | `MC-CC-001` |
| Message Definition | `MD-XX-NNN` | `MD-CC-001` |
| DataType | `DT-XX-NNN` | `DT-COM-001` |

Las siglas `XX` corresponden a las iniciales del dominio y son consistentes en todos los artefactos del mismo dominio.

### 7.4 Aliases y keywords controlados

Cada artefacto debe tener:
- `ai_keywords`: términos técnicos y de negocio en español e inglés.
- `aliases`: nombres alternativos con los que el concepto se conoce en otros sistemas o áreas.

Estos campos son los que alimentan el índice RAG y permiten al agente encontrar el BC correcto cuando el usuario usa un término no canónico.

### 7.5 Hipervínculos relativos en el repositorio

Todos los enlaces entre documentos deben ser **rutas relativas** para que funcionen tanto en el navegador de GitHub como en el MCP server:

```markdown
<!-- Correcto -->
[Ver BC](../../business-components/BC-CC-001-CreditoConsumo.md)

<!-- Incorrecto (URL absoluta; se rompe si cambia el host) -->
[Ver BC](https://arquitectura.interna/canonical/entities/credito-consumo)
```

### 7.6 Code-sets como artefactos de primera clase

Un **code-set** es una lista de valores controlados y gobernados (ej. códigos ISO de moneda, países, tipos de documento) que se referencia desde múltiples BC, MC y dominios. Se diferencia de un `enum` definido inline en un BC porque:

| | Enum inline en un BC | Code-set independiente |
| - | --------------------- | ----------------------- |
| Gobierno | Lo gobierna el dueño del BC | Lo gobierna un owner centralizado (ej. estándares ISO) |
| Reutilización | Solo dentro de ese BC | Referenciado por múltiples BC/MC de distintos dominios |
| Cambios | Cambia con la versión del BC | Tiene su propio ciclo de vida y versión |
| Ejemplo | `estadoCredito: enum=VIGENTE,EN_MORA,...` (específico del negocio de crédito) | `codigoMoneda: ref a CS-COM-001` (estándar ISO 4217, válido en todo el banco) |

**Regla práctica**: si un valor enumerado es un estándar externo (ISO, regulatorio) o se repite en más de un dominio, debe modelarse como code-set en `_codesets/`, nunca redefinirse inline en cada BC.

Cada code-set sigue una plantilla propia (`Plantilla_CodeSet.md`) con: lista de valores, fuente normativa (ej. ISO 4217), versión, y la tabla de "Used in" para saber qué BC/MC lo referencian — igual que con DataTypes.

---

## 7-bis. Code-sets compartidos (`_codesets/`)

Al igual que los DataTypes, los Code-sets viven en un directorio global porque pertenecen al lenguaje común del banco, no a un dominio de negocio específico.

```
_codesets/
├── CS-COM-001-CodigoMonedaISO4217.md
├── CS-COM-002-CodigoPaisISO3166.md
├── CS-COM-003-TipoDocumentoIdentidad.md
└── codesets-common.yaml
```

**Ejemplo de referencia desde un BC**:

```markdown
| moneda | string | [1..1] | Yes | No | Código de moneda. | COP | ref=CS-COM-001 |
```

En el OAS, el code-set se materializa como un `$ref` a un schema de tipo `string` con `enum`, definido una sola vez en `codesets-common.yaml`:

```yaml
# codesets-common.yaml
components:
  schemas:
    CodigoMonedaISO4217:
      type: string
      enum: [COP, USD, EUR, MXN, PEN]
      description: "Código de moneda según ISO 4217. Code-set: CS-COM-001."
```

Y cada BC/MC del dominio lo referencia sin redefinirlo:

```yaml
moneda:
  $ref: '../../../_codesets/codesets-common.yaml#/components/schemas/CodigoMonedaISO4217'
```

**Ventaja para agentes IA**: cuando un agente genera un OAS nuevo y necesita un campo de moneda, país o tipo de documento, primero debe consultar `_codesets/` antes de inventar un enum propio. Esto evita que existan 6 definiciones distintas de "código de moneda" en 6 dominios diferentes.

---

## 8. Pipeline CI/CD del repositorio

```
Pull Request (nuevo artefacto o nueva versión)
  │
  ├── Lint de front matter
  │   └── Valida campos obligatorios, formato de IDs, SemVer correcto
  │
  ├── Validación de trazabilidad
  │   └── Verifica que los BC/MC/DT referenciados en "composed_from" existen en el repo
  │
  ├── Validación OAS
  │   └── spectral lint sobre el yaml (alineación con schemas canónicos)
  │
  ├── Detección de tipo de cambio
  │   └── ¿Es MAJOR/MINOR/PATCH? ¿Requiere aprobación del comité?
  │
  └── Merge a main
        │
        ├── Regenerar _catalog/catalog.yaml
        ├── Regenerar _catalog/dependency-graph.yaml
        ├── Actualizar índice RAG (embeddings)
        └── Notificar MCP server (invalidar caché de artefactos modificados)
```

---

## 9. Convenciones para que la IA genere OAS correctamente

Cuando un agente genera un OAS nuevo a partir del repositorio, debe seguir este orden de contexto:

```
1. Copiar _templates/oas-template-base.yaml como punto de partida.
   → Nunca generar un OAS desde cero; siempre parte de la base estandarizada.
2. Leer el Dominio → entender el scope y los BCs disponibles.
3. Leer los BCs relevantes → entender los atributos canónicos.
4. Leer los MCs existentes → reutilizar proyecciones ya definidas si aplica.
5. Leer los MDs existentes → entender el patrón de request/response del dominio.
6. Revisar _codesets/ y _datatypes/ → reutilizar code-sets y datatypes comunes vía $ref.
7. Leer un OAS existente del dominio (si existe) → respetar el estilo, naming y estructura.
8. Generar el nuevo OAS → usando $ref a schemas existentes donde sea posible.
```

**Regla de oro para el agente**: nunca definir un schema en el OAS sin verificar primero si existe un BC, MC, DataType o Code-set canónico que ya lo modele. Si existe → usar `$ref`. Si no existe → proponer un nuevo artefacto (BC/MC/DT/CS) y documentarlo antes o junto con el OAS.

### 9.1 El template OAS base (`_templates/oas-template-base.yaml`)

Es el esqueleto que todo OAS nuevo del repositorio debe usar como punto de partida. Estandariza:

- Estructura `info`, `servers`, `security` y `tags` con la convención del banco.
- Bloque `x-canonical-metadata` (extensión propia) que enlaza cada schema del OAS con su BC/MC/DT/CS de origen — esto es lo que permite validar alineación automáticamente.
- Respuestas de error estándar (`4xx`/`5xx`) reutilizables en todas las APIs.
- Convención de naming de `operationId`, paths y parámetros.

Ningún OAS de dominio debe definir su propio formato de error o de seguridad; deben heredarse del template base.

---

## 10. Checklist de repositorio saludable

### Por artefacto
- [ ] Front matter completo con todos los campos obligatorios.
- [ ] `## Machine-readable summary` presente y actualizado.
- [ ] `ai_keywords` y `aliases` definidos.
- [ ] Hipervínculos relativos (no URLs absolutas).
- [ ] ID estable asignado siguiendo el patrón del dominio.
- [ ] Versión SemVer correcta según el tipo de cambio.

### Por dominio
- [ ] `Dominio-NombreDominio.md` con inventario e hipervínculos a todos los artefactos.
- [ ] Todos los BCs tienen su OAS schema ref apuntando al yaml del dominio.
- [ ] Todos los MCs tienen la tabla `Field traceability table` completa.
- [ ] Todos los MDs tienen la tabla `Used in OAS` actualizada.
- [ ] El OAS yaml fue generado a partir de `_templates/oas-template-base.yaml` (no desde cero).
- [ ] Los campos que correspondan a code-sets usan `$ref` a `_codesets/codesets-common.yaml`, no enums inline duplicados.
- [ ] El OAS yaml valida sin errores con spectral.

### Por repositorio
- [ ] `_catalog/catalog.yaml` generado y actualizado (no editar manualmente).
- [ ] `_catalog/dependency-graph.yaml` generado y actualizado.
- [ ] `_codesets/` sin duplicados: cada código estándar (moneda, país, tipo de documento) definido una sola vez.
- [ ] `_templates/oas-template-base.yaml` vigente y usado como base por todos los OAS de dominio.
- [ ] Pipeline CI/CD corriendo en cada PR.
- [ ] Índice RAG actualizado tras cada merge a main.
- [ ] MCP server con caché invalidada para artefactos modificados.
