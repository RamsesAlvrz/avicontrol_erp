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
