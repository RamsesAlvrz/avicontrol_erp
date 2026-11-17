# Avicontrol ERP - Sistema de Gestión Avícola Integral

## Integrantes del equipo
- Flores Valencia Jeanfranco Anderson
- Alvarez Contreras Ramses Mateo
- Guevara Garrido Piero Estefano
##  Descripción de la Problemática
En la industria avícola, la falta de centralización y digitalización en la gestión operativa, sanitaria y comercial genera pérdidas económicas sustanciales. Esta problemática surge debido a la falta de trazabilidad en los lotes de aves, un control ineficiente de las fórmulas y suministros de alimento, la ausencia de un seguimiento estricto a los planes de vacunación, y la desconexión entre la cosecha diaria de producto y los canales de distribución o venta. 

El uso de registros tradicionales en papel o hojas de cálculo aisladas impide supervisar en tiempo real la productividad de la granja, el stock de materias primas e insumos médicos, y la rentabilidad de las órdenes de venta y despacho.

##  Usuarios Involucrados
* **Administrador de Granja:** Supervisa la infraestructura global, gestiona las compras a proveedores, controla costos operacionales, administra clientes, transportes y órdenes de venta.
* **Supervisor de Galpón / Operador:** Responsable del monitoreo del equipamiento técnico, el registro de suministro de alimento por lote, el seguimiento del ciclo de vida de las aves y la recolección/clasificación de la producción diaria de huevo.
* **Veterinario / Especialista Sanitario:** Diseña las fórmulas nutricionales y programa/ejecuta los planes de vacunación y tratamiento profiláctico de los lotes.

##  Proceso a Mejorar
Automatizar y digitalizar de manera integral la cadena de valor avícola en una única plataforma web (`granjas`). El sistema abarca desde la infraestructura física (granjas, galpones y equipos) y la cadena de suministro (compras, fórmulas y almacenes), hasta la sanidad (vacunación y veterinarios), la producción (cosecha de huevo) y la comercialización (clientes, transporte y órdenes de venta).

##  Requisitos Funcionales Principales
* **Gestión de Infraestructura (CRUD):** Crear, listar, actualizar y eliminar Granjas, Galpones, Equipamiento y Lotes de aves.
* **Gestión Nutricional (CRUD):** Control de Materias Primas, Fórmulas de Alimento, Almacenes de Silos, Suministros y Compras.
* **Control Sanitario (CRUD):** Catálogo de Vacunas/Medicamentos, registro de Veterinarios, Mantenimiento de Equipos y ejecución de Planes de Vacunación.
* **Comercialización y Logística (CRUD):** Registro de Cosecha de Huevo, Clientes, Empresas de Transporte, Órdenes de Venta y sus correspondientes Detalles.

##  Arquitectura de la Aplicación Creada (`granjas`)
El sistema está construido en **Django 5** bajo una arquitectura limpia y centralizada en una sola aplicación denominada `granjas` para simplificar el despliegue.

### Módulos del Sistema (20 Entidades):
1. **Infraestructura e Inventario:** `Granja`, `Galpon`, `Lote`, `Equipamiento`, `Proveedor`.
2. **Nutrición e Insumos:** `MateriaPrima`, `FormulaAlimento`, `AlmacenAlimento`, `SuministroAlimento`, `CompraMateriaPrima`, `DetalleFormula`.
3. **Sanidad y Mantenimiento:** `VacunaMedicamento`, `Veterinario`, `PlanVacunacion`, `MantenimientoEquipamiento`.
4. **Producción, Logística y Ventas:** `ProduccionHuevo`, `Cliente`, `Transporte`, `OrdenVenta`, `DetalleVenta`.

##  Instrucciones de Ejecución
```bash
# 1. Clonar el repositorio
git clone https://github.com/RamsesAlvrz/avicontrol_erp

# 2. Entrar al directorio
cd avicontrol_erp

# 3. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Aplicar migraciones
python manage.py makemigrations granjas
python manage.py migrate

# 6. Levantar el servidor
python manage.py runserver
```
## Laboratorio 04 — Relaciones entre Modelos (OneToOne, ForeignKey, ManyToMany)

### Descripción
Se amplió el modelo de datos de AvicontrolERP (desarrollado en el Laboratorio 03) incorporando
los tres tipos de relación que ofrece Django ORM: uno a uno, uno a muchos y muchos a muchos
mediante un modelo intermedio explícito (through).

### Relaciones implementadas

**1. Uno a Uno (OneToOneField)**
- `PerfilSanitarioLote` → `Lote`
- Representa una ficha extendida que se genera tras la primera evaluación sanitaria de un lote
  (peso promedio, índice de mortalidad, conversión alimenticia, certificado sanitario).
- `on_delete=CASCADE`: si el lote se elimina, su perfil sanitario deja de tener sentido.

**2. Uno a Muchos (ForeignKey)** *(ya existente desde el Lab 03, documentada nuevamente)*
- `Galpon → Granja` (`related_name='galpones'`, `on_delete=CASCADE`)
- `Lote → Galpon` (`related_name='lotes'`, `on_delete=CASCADE`)
- Un galpón pertenece a una sola granja; un lote pertenece a un solo galpón. CASCADE porque
  las entidades hijas no tienen sentido de negocio sin su entidad padre.

**3. Muchos a Muchos con modelo intermedio (ManyToManyField + through)**
- `Lote ↔ Veterinario` a través de `VisitaVeterinaria`
- Un veterinario puede visitar muchos lotes, y un lote puede recibir visitas de distintos
  veterinarios especialistas a lo largo de su ciclo de vida.
- El modelo intermedio `VisitaVeterinaria` guarda `fecha_visita`, `diagnostico` y `estado_lote`:
  datos propios del evento de la visita, no de las entidades relacionadas.
- CRUD completo implementado en `/granjas/visitas/`.

### Entidades totales del modelo
20 entidades originales (Lab 03) + `PerfilSanitarioLote` + `VisitaVeterinaria` = **22 entidades**.

### Optimización de consultas
- `select_related()` para relaciones 1:1 y FK (evita consultas N+1 en relaciones de objeto único).
- `prefetch_related()` para relaciones inversas y N:M (evita duplicación de filas en JOINs de
  colecciones).

### Rutas principales agregadas
- `GET /granjas/lotes/<id>/` — Detalle de lote con perfil sanitario y visitas veterinarias.
- `GET /granjas/visitas/` — Listado de visitas veterinarias.
- `GET/POST /granjas/visitas/crear/` — Registrar visita.
- `GET/POST /granjas/visitas/editar/<id>/` — Editar visita.
- `GET/POST /granjas/visitas/eliminar/<id>/` — Eliminar visita.

## Laboratorio 05 — Django Admin (ModelAdmin, Inlines y personalización)

### Descripción
Se incorporó el Django Admin sobre el modelo de datos ya persistente y relacionado
(desarrollado en los Laboratorios 03 y 04), sin agregar Models ni relaciones nuevas.
El objetivo fue exponer y gestionar los datos existentes —incluyendo las relaciones
1:1, 1:N y N:M con through— directamente desde el panel administrativo de Django.

### Modelos registrados
Se registraron las 22 entidades del proyecto AvicontrolERP mediante `admin.site.register()`
y clases `ModelAdmin` personalizadas, ampliando el mínimo de 7 entidades exigido por el
enunciado (pensado originalmente para un solo estudiante), dado que el proyecto es
desarrollado por un equipo de 3 integrantes con 22 entidades en total.

### Personalización aplicada

**ModelAdmin con list_display, search_fields y list_filter:**
- `GranjaAdmin`: `list_display` (nombre, dirección, capacidad, fecha de registro),
  `search_fields` (nombre, dirección), `list_filter` (fecha_registro).
- `ProveedorAdmin`: `list_display` (razón social, RUC, teléfono, email),
  `search_fields` (razón social, RUC).
- `LoteAdmin`: `list_display` (código, galpón, raza, cantidad, estado, fecha),
  `search_fields` (código, raza), `list_filter` (estado, fecha_ingreso).
- `VeterinarioAdmin`: `list_display` (nombre, colegiatura, especialidad, teléfono),
  `search_fields` (nombre, colegiatura).
- `MateriaPrimaAdmin`: `list_display` (nombre, tipo, unidad, stock mínimo),
  `list_filter` (tipo_insumo).

**Inlines para exponer relaciones desde una sola pantalla:**
- `LicenciaSanitariaInline` (StackedInline) dentro de `GranjaAdmin` → relación 1:1.
- `InspeccionSanitariaInline` (TabularInline) dentro de `GranjaAdmin` → relación 1:N.
- `ContratoProveedorInline` (TabularInline) dentro de `GranjaAdmin` → relación N:M
  (modelo intermedio `ContratoProveedor`).
- `PerfilSanitarioLoteInline` (StackedInline) dentro de `LoteAdmin` → relación 1:1
  (investigación propia, Parte 2).
- `VisitaVeterinariaInline` (TabularInline) dentro de `LoteAdmin` → relación N:M
  (modelo intermedio `VisitaVeterinaria`, investigación propia, Parte 2).

### Qué resuelve el Admin y qué no
El Django Admin permite al personal técnico/administrativo autorizado (staff) crear,
editar y eliminar registros —incluyendo relaciones complejas— sin necesidad de escribir
Views ni Templates propios para cada operación CRUD. Sin embargo, no reemplaza la
interfaz orientada al usuario final: para presentar reportes, dashboards o formularios
adaptados al flujo de negocio (por ejemplo, un panel de trazabilidad de lotes para el
Administrador de Granja), sigue siendo necesario implementar Views y Templates
personalizados, tal como se hizo en los Laboratorios 03 y 04.

## Laboratorio 06 — Refactorización de Plantillas (Herencia, Filtros, Include y Seguridad XSS)

### Descripción
Se refactorizó la capa de presentación (Templates) del sistema `Avicontrol ERP` mediante el uso de la sintaxis avanzada del motor de plantillas de Django, logrando una arquitectura visual modular, mantenible y segura sin modificar las Views ni las URLs preexistentes.

### Aspectos Implementados
1. **Herencia de Plantillas (`{% extends %}` y `{% block %}`):**
   - Creación de la plantilla base `base.html` con estructura HTML5, Bootstrap 5 y barra de navegación superior categorizada por módulos.
   - Migración de las pantallas del CRUD (`granja_list.html`, `lote_list.html`, `proveedor_list.html`, etc.) para heredar de `base.html`.

2. **Filtros de Plantilla (Formatting):**
   - Aplicación de `|upper` para estandarizar nombres de entidades en mayúsculas (ej. `granja.nombre`).
   - Aplicación de `|floatformat:0` para formatear valores numéricos de capacidad.
   - Aplicación de `|default:"-"` para manejar valores nulos en campos como email.

3. **Reutilización de Componentes (`{% include %}`):**
   - Extracción de componentes repetidos al parcial `granjas/includes/_acciones_tabla.html` para renderizar dinámicamente los botones de acción (`Ver Detalle`, `Editar`, `Eliminar`) en los listados.

4. **Validación de Seguridad y Auto-escape XSS:**
   - Verificación del *auto-escaping* nativo de Django al probar la inyección de etiquetas `<script>` en formularios, confirmando la sanitización a entidades HTML (`&lt;script&gt;`) y previniendo ataques Cross-Site Scripting.

## Laboratorio 06 — Parte 2: Refactorización de Templates (investigación propia — Lote)

### Templates refactorizados
- **lote_list.html**: ya heredaba de `base.html` desde el Lab 04. Se agregó:
  - Filtro `upper` sobre `codigo_lote`.
  - Comentario `{% comment %}` documentando la plantilla (nombre, módulo, descripción,
    herencia, variables de contexto).
  - Reutilización del include `_acciones_tabla.html` para los botones de acción.
- **lote_detail.html**: ya heredaba de `base.html` desde el Lab 04 (muestra las relaciones
  1:1 y N:M de Lote). Se agregó:
  - Filtros `floatformat` (peso promedio, índice de mortalidad, conversión alimenticia) y
    `date` (fechas de evaluación e ingreso).
  - Comentario documentando la plantilla y los filtros aplicados al perfil sanitario.
  - Reemplazo de la tabla de visitas veterinarias por el include reutilizable
    `_visita_row.html`.

### Fragmento reutilizable (Ejercicio 11)
- **includes/_visita_row.html**: fila de tabla para una visita veterinaria (relación N:M vía
  el modelo intermedio `VisitaVeterinaria`), compartida entre `visita_list.html` (listado
  general, con columna de lote y acciones) y `lote_detail.html` (detalle de un lote, solo
  lectura). Parametrizado con `mostrar_lote` y `mostrar_acciones`, y encadena con el include
  `_acciones_tabla.html` ya existente en el proyecto para los botones Editar/Eliminar.

### Seguridad verificada (Ejercicio 12)
Se confirmó que Django escapa automáticamente caracteres especiales (`<script>`) ingresados
en el campo `diagnostico` del formulario de Visita Veterinaria, tanto en `visita_list.html`
como en `lote_detail.html`, previniendo ataques XSS sin configuración adicional.

### Flujo CRUD verificado (Ejercicio 13)
Se confirmó que las operaciones de crear, listar, editar y eliminar sobre Lote y Visita
Veterinaria siguen funcionando exactamente igual después de la refactorización de sus
Templates.

## Laboratorio 07 — Parte 1: ORM Avanzado (Transacciones, Agregación, QuerySets y Optimización)

### Descripción
Se implementó lógica avanzada de base de datos en la aplicación `granjas`, aplicando transacciones atómicas, expresiones de actualización atómica, consultas analíticas con agregación/anotación, QuerySets personalizados y optimización de consultas ORM.

### Aspectos Implementados

1. **Integridad de Datos y Modelo Intermedio (Ejercicios 1 y 2):**
   - Incorporación del campo numérico `cupos_disponibles` en `Proveedor`.
   - Ampliación del modelo intermedio `ContratoProveedor` con los atributos `cantidad_entregas_mensuales` y `monto_unitario`.
   - Exposición en Django Admin mediante `ProveedorAdmin` y `ContratoProveedorAdmin` visualizando atributos clave en `list_display`.

2. **Operaciones Transaccionales Atómicas (Ejercicio 3):**
   - Registro de contratos bajo `@transaction.atomic` y `with transaction.atomic()`.
   - Uso de expresiones `F()` para el decremento atómico seguro (`proveedor.cupos_disponibles = F('cupos_disponibles') - 1`) evitando condiciones de carrera (*race conditions*).
   - Verificación de políticas de negocio: cancelaciones mediante *rollback* automático ante falta de cupos disponibles.

3. **Consultas de Agregación Global (Ejercicio 4):**
   - Uso de `aggregate()` junto a `Sum` y `ExpressionWrapper` para calcular el valor monetario total de la cartera de contratos (`cantidad_entregas_mensuales * monto_unitario`).
   - Retorno de un diccionario escalar resumido en lugar de un `QuerySet`.

4. **Consultas de Agregación Agrupada (Ejercicio 5):**
   - **Por objeto:** `annotate(total_contratos=Count('contratoproveedor'))` sobre `Proveedor`.
   - **Por grupo:** `values('estado_contrato').annotate(cantidad=Count('id'))` sobre `ContratoProveedor`.

5. **Página de Reporte General (Ejercicio 6):**
   - Creación de la ruta `/granjas/reporte/` desplegando los resultados de `aggregate()` (con filtro `|floatformat:2`) y `annotate()` en tablas Bootstrap preparadas para decisiones gerenciales.

6. **Encapsulamiento de Reglas en QuerySet Personalizado (Ejercicio 7):**
   - Creación de `GranjaQuerySet` heredando de `models.QuerySet`, definiendo métodos de filtrado reusables: `con_licencia_vigente()` y `registradas_este_mes()`.
   - Asignación al modelo con `objects = GranjaQuerySet.as_manager()`.
   - Reutilización de `Granja.objects.con_licencia_vigente()` para filtrar dinámicamente las opciones en `ContratoProveedorForm`.

7. **Medición y Optimización del Problema N+1 (Ejercicio 8):**
   - Medición de llamadas SQL mediante `len(connection.queries)`.
   - Optimización de la vista `/granjas/contratos/` pasando de $N+1$ consultas separadas a **1 sola consulta JOIN** utilizando `select_related('granja', 'proveedor')`.

### Rutas Agregadas en Laboratorio 07 - Parte 1
- `GET /granjas/reporte/` — Reporte analítico con totales globales y métricas agrupadas.
- `GET /granjas/contratos/` — Listado optimizado de contratos de proveedores.
- `GET/POST /granjas/contratos/registrar/` — Formulario de registro con transacción atómica y validación de cupos.

---

## Laboratorio 07 — Parte 2: ORM Avanzado en la Investigación Propia (Módulo de Ventas)

### Descripción
Se desarrolló e integró de manera modular la lógica avanzada del ORM de Django sobre el subdominio de **Ventas y Comercialización** (`OrdenVenta`, `DetalleVenta`, `Cliente`, `Transporte` y `ProduccionHuevo`), asegurando la independencia total del módulo respecto al trabajo de los demás integrantes.

### Aspectos Implementados

1. **Operaciones Transaccionales Atómicas en Ventas (Ejercicio 10):**
   - Registro atómico de ventas mediante `@transaction.atomic` en la vista `ordenventa_registrar`.
   - Garantiza que la creación de la cabecera `OrdenVenta` y la inserción de sus ítems `DetalleVenta` se ejecuten en un solo bloque transaccional. En caso de fallar algún ítem, la BD ejecuta un *rollback* integral, evitando órdenes de venta huérfanas.

2. **Reportes e Indicadores de Negocio con Agregación (Ejercicio 11):**
   - Construcción de un panel de reportes comercial en `/granjas/reporte-ventas/` (`reporte_ventas_view`).
   - **Métricas Globales (`aggregate`):** Suma del monto facturado global y promedio por orden de venta:
     ```python
     OrdenVenta.objects.aggregate(
         monto_total_acumulado=Sum('monto_total'),
         promedio_por_venta=Avg('monto_total')
     )
     ```
   - **Métricas Agrupadas (`values` + `annotate`):** Agrupación por cliente para obtener la facturación acumulada y el número total de transacciones:
     ```python
     OrdenVenta.objects.values('cliente__razon_social').annotate(
         total_facturado=Sum('monto_total'),
         cantidad_ordenes=Count('id')
     ).order_by('-total_facturado')
     ```

3. **QuerySet Personalizado Encadenable (Ejercicio 12):**
   - Definición de la clase `OrdenVentaQuerySet` (heredando de `models.QuerySet`) vinculada al modelo con `objects = OrdenVentaQuerySet.as_manager()`.
   - **Métodos implementados:**
     - `.entregadas()`: Filtra registros con `estado_entrega='ENTREGADO'`.
     - `.del_mes()`: Filtra registros emitidos en el mes y año actual (`fecha_emision`).
   - **Uso encadenado en vistas:**
     - `ordenventa_list`: `OrdenVenta.objects.entregadas().del_mes().count()`
     - `reporte_ventas_view`: `OrdenVenta.objects.entregadas().del_mes().aggregate(total=Sum('monto_total'))`

4. **Medición y Optimización de Consultas SQL N+1 (Ejercicio 13):**
   - **Diagnóstico:** El listado `/granjas/detalles-venta/` (`detalleventa_list`) ejecutaba $1 + (2 \times N)$ consultas SQL al acceder iterativamente a los objetos `orden` y `produccion_huevo` de cada detalle en la plantilla (11 consultas para 5 registros).
   - **Solución:** Aplicación de `select_related('orden', 'produccion_huevo')` para realizar un `JOIN` automático a nivel de base de datos.
   - **Resultado:** Reducción del volumen de consultas de **11 consultas a 1 sola consulta SQL**, optimizando el tiempo de respuesta a orden constante $O(1)$.

### Rutas Agregadas en Laboratorio 07 - Parte 2
- `GET /granjas/reporte-ventas/` — Pantalla de reportes comerciales y métricas del subdominio de ventas.
- `GET /granjas/detalles-venta/` — Listado optimizado de detalles de ventas ($O(1)$ consulta SQL).
- `GET/POST /granjas/ordenes-venta/registrar/` — Registro completo de orden y detalles con transacción atómica.

# Laboratorio 08 — Implementación de API REST

## Descripción

En el Laboratorio 08 se implementó una API REST utilizando Django REST Framework en el proyecto Avicontrol ERP. El desarrollo se dividió en dos partes: la primera enfocada en los modelos trabajados durante las semanas anteriores y la segunda en los modelos de la investigación propia.

## Parte 1 — Implementación de API REST

Se desarrollaron serializers, vistas y rutas para exponer información de los modelos Equipamiento y OrdenVenta.

**Funcionalidades implementadas:**

- ModelSerializer para transformar los datos de los modelos.
- Validación personalizada del código de equipamiento.
- ModelViewSet para gestionar equipamientos mediante operaciones CRUD.
- ReadOnlyModelViewSet para consultar órdenes de venta.
- Relaciones anidadas para visualizar información del cliente y los detalles de las órdenes.
- Optimización de consultas mediante select_related y prefetch_related.
- Búsqueda y ordenamiento de equipamientos.
- Filtrado de órdenes y acción personalizada para consultar órdenes entregadas.

**Endpoints principales:**

| Endpoint | Descripción |
|---|---|
| `/api/equipamientos/` | Listar y registrar equipamientos |
| `/api/equipamientos/{id}/` | Consultar, actualizar o eliminar un equipamiento |
| `/api/ordenes/` | Consultar órdenes de venta |
| `/api/ordenes/entregadas/` | Consultar órdenes entregadas |

## Parte 2 — API REST de la investigación propia

Se implementaron recursos adicionales correspondientes a los modelos de la investigación del proyecto Avicontrol ERP.

**Funcionalidades implementadas:**

- Creación de ModelSerializers para Veterinario, Lote y PerfilSanitarioLote.
- Validación personalizada del campo colegiatura de Veterinario.
- Implementación de ModelViewSets para Veterinario y Lote.
- Registro de rutas mediante DefaultRouter.
- Creación de LoteQuerySet con métodos para consultar lotes en crecimiento y finalizados.
- Pruebas de validación mediante el shell de Django.
- Pruebas de operaciones CRUD y respuestas HTTP.

**Endpoints principales:**

| Endpoint | Descripción |
|---|---|
| `/api/veterinarios/` | Listar y registrar veterinarios |
| `/api/veterinarios/{id}/` | Consultar, actualizar o eliminar veterinarios |
| `/api/lotes/` | Listar y registrar lotes |
| `/api/lotes/{id}/` | Consultar, actualizar o eliminar lotes |

## Pruebas de la API

Se realizaron pruebas para verificar los siguientes códigos HTTP:

| Código | Significado |
|---|---|
| 200 OK | Consulta exitosa |
| 201 Created | Registro creado correctamente |
| 400 Bad Request | Datos inválidos |
| 404 Not Found | Recurso no encontrado |
| 204 No Content | Registro eliminado correctamente |

## Instalación y ejecución

1. Instalar las dependencias del proyecto:

   `pip install -r requirements.txt`

2. Aplicar las migraciones:

   `python manage.py migrate`

3. Iniciar el servidor:

   `python manage.py runserver`

4. Acceder a la API REST:

   `http://127.0.0.1:8000/api/`

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- Git y GitHub

# Laboratorio 09 — Desarrollo de Interfaz de Usuario con React y Vite

## Descripción

En el Laboratorio 09 se desarrolló la capa de presentación del cliente (Frontend SPA) utilizando **React** y **Vite** dentro de la carpeta `/frontend`. Se migró la visualización de datos desde el renderizado en servidor (SSR con Django Templates) hacia una arquitectura interactiva en el navegador, aplicando JSX, componentes funcionales, renderizado condicional, manejo de colecciones y estilos CSS modulares.

---

## Parte 1 — Conceptos Fundamentales de React y Vite

Se construyó la interfaz base del sistema **AviControl ERP** explorando las características principales del motor de renderizado de React:

**Aspectos Implementados:**
- **Configuración del Proyecto Frontend:** Creación de la estructura en la carpeta `frontend/` mediante Vite + React, configurando la ejecución en entorno de desarrollo local.
- **Expresiones en JSX:** Incorporación de lógica JavaScript dentro del marcado JSX mediante llaves `{ }`, ejecutando variables de entorno, constantes numéricas y la función de cálculo del IGV/total con formateo a dos decimales (`.toFixed(2)`).
- **Renderizado de Colecciones (`map` y `key`):** Transformación de arreglos de datos en elementos de interfaz utilizando `.map()`, asignando a cada nodo un identificador único en la propiedad `key={item.id}` para optimizar la reconciliación del Virtual DOM.
- **Renderizado Condicional:** Evaluación de reglas de negocio en la vista usando:
  - *Early Return*: Retorno inmediato de mensaje alternativo para arreglos vacíos (`if (!equipos || equipos.length === 0)`).
  - *Operador Ternario (`? :`)*: Conmutación de etiquetas visuales (`badge-ok` vs `badge-warn`) según el estado operativo.
  - *Operador Lógico AND (`&&`)*: Muestreo de alertas urgentes únicamente al cumplirse condiciones críticas.
- **Estructuras Anidadas (Relación 1:N):** Despliegue de cabeceras (`OrdenVenta`) e ítems asociados (`DetalleVenta`) combinando métodos `.map()` anidados y calculando montos totales dinámicos mediante `.reduce()`.
- **Estilizado y Compilación:** Aplicación de clases CSS en `App.css`, uso de estilos dinámicos en línea (`style={{ }}`) y auditoría de código mediante `npm run lint` y `npm run build`.

---

## Parte 2 — Interfaz de la Investigación Propia (Módulo Sanitario)

Se implementó la interfaz del **Módulo de Sanidad y Control Veterinario** reflejando las entidades y relaciones trabajadas en las semanas previas del proyecto (`Veterinario`, `PerfilSanitarioLote` y `VisitaVeterinaria`).

**Componentes Desarrollados:**

| Componente | Entidades / Lógica Representada | Funcionalidad Clave |
| :--- | :--- | :--- |
| `ListaVeterinarios` | `Veterinario` | Listado del directorio de especialistas con tarjeta de datos y claves únicas por colegiatura. |
| `ListaPerfilesSanitarios` | `PerfilSanitarioLote` (Relación 1:1) | Renderizado de estado sanitario con bordes dinámicos (`style={{ }}`), verificación de certificado SENASA y alerta de mortalidad crítica (> 5.0%). |
| `ReporteVisitasAnidadas` | `VisitaVeterinaria` (N:M *through*) | Despliegue anidado de atenciones clínicas agrupadas por médico responsable con conteo dinámico (`visitas.length`). |

**Aspectos Destacados:**
- **Separación de Responsabilidades:** Integración limpia de componentes en `App.jsx` manteniendo la modularidad del código.
- **Validación de Consola:** Ausencia total de errores o advertencias en las herramientas de desarrollador (`F12`), garantizando el uso correcto del atributo `key`.
- **Control de Versiones y Distribución:** Exclusión de `node_modules/` y la carpeta de compilación `dist/` en `.gitignore`.

---

## Ejecución del Frontend

1. **Ingresar al directorio del frontend e instalar dependencias:**
   ```bash
   cd frontend
   npm install
---

# Laboratorio 11 — Comunicación entre componentes (React)

## Descripción

Se aplicó la comunicación entre componentes de React: **los datos bajan del padre al hijo por props** y **los avisos suben del hijo al padre con funciones recibidas por props**. Cuando varios hermanos necesitan el mismo dato, el estado se **eleva** al padre común y los valores calculables (totales, conteos, promedios) se obtienen como **datos derivados**, sin `useState`. Se usó `useEffect` con arreglo de dependencias y función de limpieza.

La app (`frontend/`) tiene una barra de navegación con tres vistas: **Panel de Lotes** (Parte 2), **Práctica Cafetería** (Parte 1) y **Laboratorio 10**.

## Parte 1 — Mini catálogo con carrito (`frontend/src/practica`)

| Componente | Rol |
| :--- | :--- |
| `Practica` | Padre. Guarda `carrito`, `busqueda` y `ultimoAgregado`; define `agregarAlCarrito`, `quitarDelCarrito` y `vaciarCarrito` (con `map`, `filter` y spread, sin `push`/`splice`). |
| `Buscador` | Campo controlado (`valor`, `onCambiar`). |
| `Catalogo` / `ProductoCard` | Listado con `map()` y `key`; botón **Agregar** (desactivado si `stock === 0`) que llama a `onAgregar(producto)`. |
| `Carrito` | Hermano de `Catalogo`: líneas, **Quitar** (`onQuitar(id)`), **Vaciar carrito** (`onVaciar`), total y unidades con `reduce()`, `useEffect` que actualiza `document.title`. |
| `Aviso` | Muestra `Agregado: <nombre>` y se oculta a los 3 s (`setTimeout` + `clearTimeout` en la limpieza). |

## Parte 2 — Panel administrativo: Gestión de Lotes (`frontend/src/components`)

Pantalla de gestión de la entidad **`Lote`**, con datos de ejemplo escritos a mano con la forma de `GET /api/lotes/` (Semana 8).

| Componente | Rol | Props que recibe |
| :--- | :--- | :--- |
| `PanelLotes` | Padre y único dueño del estado (`lotes`, `busqueda`, `filtroEstado`, `aviso`). `useEffect` → título `Lotes (N) — AviControl ERP`. | — |
| `ResumenLotes` | Hermano del listado. Datos derivados: total de lotes, total de aves, en crecimiento / finalizados, promedio de aves por lote. | `lotes` |
| `BuscadorLotes` | Filtro controlado por código o raza + selector de estado. | `valor`, `onCambiar`, `estado`, `onCambiarEstado` |
| `ListaLotes` | Tabla; mensaje cuando no hay resultados. | `lotes`, `onEliminar`, `onCambiarEstado` |
| `LoteFila` | Una fila con botones **Finalizar/Reactivar** y **Eliminar** que avisan al padre con el `id`. | `lote`, `onEliminar`, `onCambiarEstado` |
| `LoteForm` | Alta controlada. Valida campos obligatorios, `codigo_lote` único y `cantidad_inicial` entera > 0; envía el registro con `onGuardar` y limpia los campos. | `codigosExistentes`, `onGuardar` |
| `AvisoPanel` | Aviso de confirmación que desaparece a los 3 s, con limpieza del temporizador. | `mensaje`, `onCerrar` |

**Verificación:** consola del navegador sin advertencias; `npm run lint` (oxlint) y `npm run build` terminan sin errores; `node_modules/` y `dist/` siguen excluidos por `.gitignore`.


## Laboratorio 12 — Ajax y servicios web (React + Django REST Framework)

### Objetivo y arquitectura
Se conectó el frontend React (Vite, puerto 5173) con la API Django REST Framework (puerto 8000) mediante Axios. Django consulta y valida los datos con ViewSets, serializers y ORM; React muestra los resultados y actualiza la interfaz sin recargar toda la página.

### Puesta en marcha (Windows, dos terminales)
**Terminal 1 — Django (desde la raíz del repositorio):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Si el entorno virtual ya existe y las dependencias están instaladas, omita los pasos correspondientes.

**Terminal 2 — React:**
```powershell
cd frontend
npm install
npm run dev
```
Abrir `http://localhost:5173/`. Para verificar la API, abrir `http://127.0.0.1:8000/api/equipamientos/` o `http://127.0.0.1:8000/api/lotes/`.

### Configuración CORS y Axios
- `config/settings.py` incluye `corsheaders` y `corsheaders.middleware.CorsMiddleware`; `CORS_ALLOWED_ORIGINS` permite `http://localhost:5173` y `http://127.0.0.1:5173` durante el desarrollo.
- `frontend/src/api.js` centraliza la instancia de Axios con la URL base `http://127.0.0.1:8000/api`.
- El backend y el frontend deben permanecer ejecutándose al mismo tiempo.

### Endpoints utilizados
| Recurso | Métodos | URL |
| --- | --- | --- |
| Equipamientos (práctica, Parte 1) | GET, POST | `/api/equipamientos/` |
| Equipamiento individual | GET, PATCH, DELETE | `/api/equipamientos/{id}/` |
| Lotes (panel, Parte 2) | GET, POST | `/api/lotes/` |
| Lote individual | GET, PATCH, DELETE | `/api/lotes/{id}/` |

**Búsqueda y filtros:**
- `GET /api/equipamientos/?search=C-003` busca por código, nombre o tipo.
- `GET /api/lotes/?search=002` busca por código o raza.
- `GET /api/lotes/?estado=FINALIZADO` filtra por estado.
- `GET /api/lotes/?search=002&estado=FINALIZADO` combina ambos filtros.

### Funcionalidades y respuestas HTTP
- GET lista los datos desde Django; POST crea registros (`201 Created`).
- PATCH actualiza registros (`200 OK`) y DELETE los elimina con confirmación previa (`204 No Content`).
- Los serializers validan los campos; los datos inválidos devuelven `400 Bad Request` y el formulario muestra el mensaje.
- La interfaz contempla carga, error de conexión y listas vacías.
- En el panel, `PanelLotes.jsx` administra el estado; los componentes hijos reciben datos y funciones mediante props.

### Verificación
```powershell
cd frontend
npm run lint
npm run build
```
En la verificación local del Laboratorio 12 se obtuvo **0 errores y 0 advertencias** en lint y una compilación de producción correcta. No se deben subir `frontend/node_modules/` ni `frontend/dist/` a Git.

### Nota de seguridad
Esta integración se probó en entorno de desarrollo local. Antes de usarla en producción se deben configurar autenticación, permisos por usuario, protección de credenciales, CORS restringido y `DEBUG=False`.
