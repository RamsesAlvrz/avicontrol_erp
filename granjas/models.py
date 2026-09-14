from django.db import models

# ==========================================
# 1. MÓDULO PRINCIPAL DE LA GRANJA Y ESTRUCTURA
# ==========================================

class Granja(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Granja")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    capacidad_total = models.PositiveIntegerField(verbose_name="Capacidad Total (Aves)")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")

    # EJERCICIO 4: Relación Muchos a Muchos (N:M) con modelo intermedio
    proveedores = models.ManyToManyField(
        'Proveedor',
        through='ContratoProveedor',
        related_name='granjas'
    )

    class Meta:
        verbose_name = "Granja"
        verbose_name_plural = "Granjas"
        ordering = ['-id']

    def __str__(self):
        return self.nombre


# EJERCICIO 2: Relación Uno a Uno (1:1) — Ficha Complementaria
class LicenciaSanitaria(models.Model):
    granja = models.OneToOneField(
        Granja,
        on_delete=models.CASCADE,
        related_name='licencia_sanitaria',
        verbose_name="Granja"
    )
    codigo_resolucion = models.CharField(max_length=50, unique=True, verbose_name="Código de Resolución SENASA")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento")
    esta_vigente = models.BooleanField(default=True, verbose_name="¿Licencia Vigente?")

    class Meta:
        verbose_name = "Licencia Sanitaria"
        verbose_name_plural = "Licencias Sanitarias"

    def __str__(self):
        return f"Licencia {self.codigo_resolucion} - {self.granja.nombre}"


# EJERCICIO 3: Relación Uno a Muchos (1:N)
class InspeccionSanitaria(models.Model):
    granja = models.ForeignKey(
        Granja,
        on_delete=models.CASCADE,
        related_name='inspecciones',
        verbose_name="Granja"
    )
    fecha_inspeccion = models.DateField(verbose_name="Fecha de Inspección")
    resultado = models.CharField(max_length=50, verbose_name="Resultado (Aprobado/Observado)")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Inspección Sanitaria"
        verbose_name_plural = "Inspecciones Sanitarias"
        ordering = ['-fecha_inspeccion']

    def __str__(self):
        return f"Inspección {self.fecha_inspeccion} - {self.granja.nombre}"


class Equipamiento(models.Model):
    TIPO_CHOICES = [
        ('SENSOR', 'Sensor de Temperatura/Humedad'),
        ('COMEDERO', 'Comedero Automático'),
        ('EXTRACTOR', 'Extractor de Aire'),
    ]
    ESTADO_CHOICES = [
        ('OPERATIVO', 'Operativo'),
        ('MANTENIMIENTO', 'En Mantenimiento'),
    ]

    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código de Equipo")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo de Equipo")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='OPERATIVO', verbose_name="Estado")

    class Meta:
        verbose_name = "Equipamiento"
        verbose_name_plural = "Equipamientos"
        ordering = ['-id']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Proveedor(models.Model):
    razon_social = models.CharField(max_length=150, verbose_name="Razón Social")
    ruc = models.CharField(max_length=11, unique=True, verbose_name="RUC")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['-id']

    def __str__(self):
        return self.razon_social


# EJERCICIO 4: Modelo Intermedio para la relación N:M entre Granja y Proveedor
class ContratoProveedor(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('FINALIZADO', 'Finalizado'),
    ]

    granja = models.ForeignKey(Granja, on_delete=models.CASCADE, verbose_name="Granja")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, verbose_name="Proveedor")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    estado_contrato = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ACTIVO', verbose_name="Estado")

    class Meta:
        verbose_name = "Contrato de Proveedor"
        verbose_name_plural = "Contratos de Proveedores"

    def __str__(self):
        return f"{self.granja.nombre} - {self.proveedor.razon_social}"


class Galpon(models.Model):
    TIPO_GALPON = [
        ('AUTOMATICO', 'Climatizado / Automático'),
        ('MANUAL', 'Convencional / Manual'),
    ]

    granja = models.ForeignKey(Granja, on_delete=models.CASCADE, related_name='galpones', verbose_name="Granja")
    numero = models.CharField(max_length=20, verbose_name="Número/Código de Galpón")
    tipo_galpon = models.CharField(max_length=50, choices=TIPO_GALPON, verbose_name="Tipo de Galpón")
    capacidad = models.PositiveIntegerField(verbose_name="Capacidad de Aves")

    class Meta:
        verbose_name = "Galpón"
        verbose_name_plural = "Galpones"
        ordering = ['-id']

    def __str__(self):
        return f"Galpón {self.numero} ({self.granja.nombre})"


class Lote(models.Model):
    ESTADO_LOTE = [
        ('CRECIMIENTO', 'En Crecimiento'),
        ('FINALIZADO', 'Procesado / Finalizado'),
    ]

    galpon = models.ForeignKey(Galpon, on_delete=models.CASCADE, related_name='lotes', verbose_name="Galpón")
    codigo_lote = models.CharField(max_length=30, unique=True, verbose_name="Código de Lote")
    cantidad_inicial = models.PositiveIntegerField(verbose_name="Cantidad Inicial de Aves")
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    raza = models.CharField(max_length=50, verbose_name="Raza")
    estado = models.CharField(max_length=20, choices=ESTADO_LOTE, default='CRECIMIENTO', verbose_name="Estado")
    veterinarios = models.ManyToManyField(
        'Veterinario',
        through='VisitaVeterinaria',
        related_name='lotes_atendidos',
        verbose_name="Veterinarios que atendieron"
    )

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"
        ordering = ['-id']

    def __str__(self):
        return f"Lote {self.codigo_lote} - {self.raza}"


# ==========================================
# 2. MÓDULO DE ALIMENTACIÓN Y CONSUMO
# ==========================================

class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Insumo")
    tipo_insumo = models.CharField(max_length=50, verbose_name="Tipo de Insumo")
    unidad_medida = models.CharField(max_length=20, default='Kg', verbose_name="Unidad de Medida")
    stock_minimo = models.PositiveIntegerField(default=100, verbose_name="Stock Mínimo")

    class Meta:
        verbose_name = "Materia Prima"
        verbose_name_plural = "Materias Primas"
        ordering = ['-id']

    def __str__(self):
        return self.nombre


class FormulaAlimento(models.Model):
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, related_name='formulas', verbose_name="Materia Prima Principal")
    nombre_formula = models.CharField(max_length=100, verbose_name="Nombre de la Fórmula")
    etapa_nutricional = models.CharField(max_length=50, verbose_name="Etapa Nutricional")
    porcentaje_proteina = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Porcentaje de Proteína (%)")

    class Meta:
        verbose_name = "Fórmula de Alimento"
        verbose_name_plural = "Fórmulas de Alimentos"
        ordering = ['-id']

    def __str__(self):
        return self.nombre_formula


class AlmacenAlimento(models.Model):
    formula = models.ForeignKey(FormulaAlimento, on_delete=models.PROTECT, related_name='almacenes', verbose_name="Fórmula Contenida")
    nombre_almacen = models.CharField(max_length=100, verbose_name="Nombre del Almacén / Silo")
    capacidad_kilos = models.PositiveIntegerField(verbose_name="Capacidad Total (Kg)")
    stock_disponible = models.PositiveIntegerField(verbose_name="Stock Disponible (Kg)")

    class Meta:
        verbose_name = "Almacén de Alimento"
        verbose_name_plural = "Almacenes de Alimento"
        ordering = ['-id']

    def __str__(self):
        return f"{self.nombre_almacen} - {self.formula.nombre_formula}"


class SuministroAlimento(models.Model):
    almacen = models.ForeignKey(AlmacenAlimento, on_delete=models.PROTECT, related_name='suministros', verbose_name="Almacén de Origen")
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='suministros_alimento', verbose_name="Lote Destino")
    formula = models.ForeignKey(FormulaAlimento, on_delete=models.PROTECT, verbose_name="Fórmula Suministrada")
    fecha_suministro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de Suministro")
    cantidad_kg = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cantidad Suministrada (Kg)")

    class Meta:
        verbose_name = "Suministro de Alimento"
        verbose_name_plural = "Suministros de Alimentos"
        ordering = ['-id']


# ==========================================
# 3. MÓDULO SANITARIO Y VETERINARIO
# ==========================================

class VacunaMedicamento(models.Model):
    nombre_comercial = models.CharField(max_length=100, verbose_name="Nombre Comercial")
    principio_activo = models.CharField(max_length=100, verbose_name="Principio Activo")
    via_administracion = models.CharField(max_length=50, verbose_name="Vía de Administración")
    dosis_recomendada = models.CharField(max_length=50, verbose_name="Dosis Recomendada")

    class Meta:
        verbose_name = "Vacuna / Medicamento"
        verbose_name_plural = "Vacunas y Medicamentos"
        ordering = ['-id']

    def __str__(self):
        return self.nombre_comercial


class Veterinario(models.Model):
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    colegiatura = models.CharField(max_length=50, unique=True, verbose_name="Número de Colegiatura")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")

    class Meta:
        verbose_name = "Veterinario"
        verbose_name_plural = "Veterinarios"
        ordering = ['-id']

    def __str__(self):
        return self.nombre_completo


class PlanVacunacionLote(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='planes_vacunacion', verbose_name="Lote")
    vacuna = models.ForeignKey(VacunaMedicamento, on_delete=models.PROTECT, verbose_name="Vacuna / Medicamento")
    veterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Veterinario Responsable")
    dosis = models.CharField(max_length=50, verbose_name="Dosis Aplicada")
    fecha_programada = models.DateField(verbose_name="Fecha Programada")
    fecha_aplicada = models.DateField(null=True, blank=True, verbose_name="Fecha de Aplicación")

    class Meta:
        verbose_name = "Plan de Vacunación"
        verbose_name_plural = "Planes de Vacunación"
        ordering = ['-id']


# ==========================================
# 4. MÓDULO DE PRODUCCIÓN Y VENTAS
# ==========================================

class ProduccionHuevo(models.Model):
    CATEGORIAS = [
        ('EXTRA', 'Extra'),
        ('GRANDE', 'Grande'),
        ('MEDIANO', 'Mediano'),
        ('ROTO', 'Roto / Mermas'),
    ]

    categoria = models.CharField(max_length=50, choices=CATEGORIAS, verbose_name="Categoría de Huevo")
    fecha_cosecha = models.DateField(verbose_name="Fecha de Cosecha")
    cantidad_jabas = models.PositiveIntegerField(verbose_name="Cantidad de Jabas")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Producción de Huevo"
        verbose_name_plural = "Producciones de Huevo"
        ordering = ['-id']

    def __str__(self):
        return f"{self.categoria} ({self.fecha_cosecha})"


class Cliente(models.Model):
    razon_social = models.CharField(max_length=150, verbose_name="Razón Social / Nombre")
    ruc_dni = models.CharField(max_length=20, unique=True, verbose_name="RUC / DNI")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-id']

    def __str__(self):
        return self.razon_social


class Transporte(models.Model):
    placa = models.CharField(max_length=15, unique=True, verbose_name="Placa del Vehículo")
    conductor = models.CharField(max_length=100, verbose_name="Nombre del Conductor")
    tipo_vehiculo = models.CharField(max_length=50, verbose_name="Tipo de Vehículo")
    capacidad_carga_kg = models.PositiveIntegerField(verbose_name="Capacidad de Carga (Kg)")

    class Meta:
        verbose_name = "Transporte"
        verbose_name_plural = "Transportes"
        ordering = ['-id']

    def __str__(self):
        return f"{self.placa} - {self.conductor}"


class OrdenVenta(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_TRANSITO', 'En Tránsito'),
        ('ENTREGADO', 'Entregado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='ordenes_venta', verbose_name="Cliente")
    transporte = models.ForeignKey(Transporte, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Unidad de Transporte")
    numero_comprobante = models.CharField(max_length=50, unique=True, verbose_name="Número de Comprobante")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión")
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto Total ($)")
    estado_entrega = models.CharField(max_length=50, choices=ESTADOS, default='PENDIENTE', verbose_name="Estado de Entrega")

    class Meta:
        verbose_name = "Orden de Venta"
        verbose_name_plural = "Órdenes de Venta"
        ordering = ['-id']

    def __str__(self):
        return f"Orden #{self.numero_comprobante} - {self.cliente.razon_social}"


# ==========================================
# 5. OTRAS TABLAS INTERMEDIAS
# ==========================================

class DetalleFormula(models.Model):
    formula = models.ForeignKey(FormulaAlimento, on_delete=models.CASCADE, related_name='detalles', verbose_name="Fórmula")
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, verbose_name="Materia Prima")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Porcentaje (%)")
    kilos_por_tonelada = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Kg por Tonelada")

    class Meta:
        verbose_name = "Detalle de Fórmula"
        verbose_name_plural = "Detalles de Fórmulas"


class DetalleVenta(models.Model):
    orden = models.ForeignKey(OrdenVenta, on_delete=models.CASCADE, related_name='detalles', verbose_name="Orden de Venta")
    produccion_huevo = models.ForeignKey(ProduccionHuevo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Producción de Huevo")
    lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Lote de Aves")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio Unitario")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Ventas"


class MantenimientoEquipamiento(models.Model):
    equipamiento = models.ForeignKey(Equipamiento, on_delete=models.CASCADE, related_name='mantenimientos', verbose_name="Equipo")
    tecnico = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Técnico / Encargado")
    fecha_mantenimiento = models.DateField(verbose_name="Fecha de Mantenimiento")
    descripcion_trabajo = models.TextField(verbose_name="Descripción del Trabajo")

    class Meta:
        verbose_name = "Mantenimiento de Equipamiento"
        verbose_name_plural = "Mantenimientos de Equipamiento"
        ordering = ['-id']


class CompraMateriaPrima(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, related_name='compras_materia_prima', verbose_name="Proveedor")
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, verbose_name="Materia Prima")
    fecha_compra = models.DateField(verbose_name="Fecha de Compra")
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad Comprada")
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio Unitario")
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Total")

    class Meta:
        verbose_name = "Compra de Materia Prima"
        verbose_name_plural = "Compras de Materias Primas"
        ordering = ['-id']

# ============================================
# PARTE 2 - EJERCICIO 10: Relación 1:1
# ============================================
class PerfilSanitarioLote(models.Model):
    """
    Ficha complementaria del Lote: no son 'más campos' del Lote porque
    este perfil solo se genera tras la primera evaluación sanitaria
    (puede no existir aún si el lote acaba de ingresar), y agrupa
    indicadores de desempeño que pertenecen a un módulo distinto
    (control sanitario) del que gestiona el ciclo de vida del lote.
    """
    lote = models.OneToOneField(
        Lote,
        on_delete=models.CASCADE,
        related_name='perfil_sanitario',
        verbose_name="Lote"
    )
    peso_promedio_gr = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Peso Promedio (g)"
    )
    indice_mortalidad = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Índice de Mortalidad (%)"
    )
    conversion_alimenticia = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Índice de Conversión Alimenticia"
    )
    certificado_sanitario = models.BooleanField(
        default=False, verbose_name="¿Cuenta con Certificado Sanitario?"
    )
    fecha_evaluacion = models.DateField(
        auto_now_add=True, verbose_name="Fecha de Evaluación"
    )

    class Meta:
        verbose_name = "Perfil Sanitario de Lote"
        verbose_name_plural = "Perfiles Sanitarios de Lote"

    def __str__(self):
        return f"Perfil Sanitario - {self.lote.codigo_lote}"


# ============================================
# PARTE 2 - EJERCICIO 10: Relación N:M con through
# ============================================
class VisitaVeterinaria(models.Model):
    """
    Modelo intermedio entre Lote y Veterinario: un veterinario visita
    muchos lotes a lo largo del tiempo, y un lote puede ser visitado
    por distintos veterinarios (especialistas). La relación en sí
    necesita guardar la fecha de la visita y el diagnóstico emitido,
    datos que no pertenecen ni al Lote ni al Veterinario individualmente,
    sino al evento de la visita.
    """
    ESTADO_CHOICES = [
        ('SALUDABLE', 'Saludable'),
        ('OBSERVACION', 'En Observación'),
        ('CRITICO', 'Crítico'),
    ]

    lote = models.ForeignKey(
        Lote, on_delete=models.CASCADE,
        related_name='visitas_veterinarias', verbose_name="Lote"
    )
    veterinario = models.ForeignKey(
        Veterinario, on_delete=models.PROTECT,
        related_name='visitas_realizadas', verbose_name="Veterinario"
    )
    fecha_visita = models.DateField(verbose_name="Fecha de Visita")
    diagnostico = models.TextField(verbose_name="Diagnóstico")
    estado_lote = models.CharField(
        max_length=20, choices=ESTADO_CHOICES,
        default='SALUDABLE', verbose_name="Estado del Lote"
    )

    class Meta:
        verbose_name = "Visita Veterinaria"
        verbose_name_plural = "Visitas Veterinarias"
        ordering = ['-fecha_visita']

    def __str__(self):
        return f"Visita {self.fecha_visita} - {self.lote.codigo_lote} ({self.veterinario.nombre_completo})"
