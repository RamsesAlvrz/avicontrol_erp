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
