from django.contrib import admin
from .models import (
    Granja, LicenciaSanitaria, InspeccionSanitaria, Proveedor, ContratoProveedor,
    Galpon, Lote, Equipamiento, MateriaPrima, FormulaAlimento, AlmacenAlimento,
    SuministroAlimento, VacunaMedicamento, Veterinario, PlanVacunacionLote,
    ProduccionHuevo, Cliente, Transporte, OrdenVenta, DetalleFormula,
    DetalleVenta, MantenimientoEquipamiento, CompraMateriaPrima,
    PerfilSanitarioLote, VisitaVeterinaria
)

# ===================================================================
# INLINES PARA LA ENTIDAD GRANJA
# ===================================================================

# Ejercicio 6: Inline 1:1 (StackedInline)
class LicenciaSanitariaInline(admin.StackedInline):
    model = LicenciaSanitaria
    extra = 1

# Ejercicio 7: Inline 1:N (TabularInline)
class InspeccionSanitariaInline(admin.TabularInline):
    model = InspeccionSanitaria
    extra = 1

# Ejercicio 7: Inline N:M mediante Modelo Intermedio (TabularInline)
class ContratoProveedorInline(admin.TabularInline):
    model = ContratoProveedor
    extra = 1


# ===================================================================
# CONFIGURACIÓN PRINCIPAL DE MODELADMIN
# ===================================================================

@admin.register(Granja)
class GranjaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'capacidad_total', 'fecha_registro')
    search_fields = ('nombre', 'direccion')
    list_filter = ('fecha_registro',)
    # Registro de los 3 inlines (1:1, 1:N y N:M)
    inlines = [LicenciaSanitariaInline, InspeccionSanitariaInline, ContratoProveedorInline]

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('razon_social', 'ruc', 'telefono', 'email')
    search_fields = ('razon_social', 'ruc')

# ============================================
# LAB 5 - PARTE 2: Personalización sobre la investigación propia (Lote)
# ============================================

# Ejercicio 11: Inline 1:1 (StackedInline) — PerfilSanitarioLote
class PerfilSanitarioLoteInline(admin.StackedInline):
    model = PerfilSanitarioLote
    extra = 1

# Ejercicio 12: Inline N:M con through (TabularInline) — VisitaVeterinaria
class VisitaVeterinariaInline(admin.TabularInline):
    model = VisitaVeterinaria
    extra = 1

# Ejercicio 10: ModelAdmin para Lote, con list_display, search_fields, list_filter
@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('codigo_lote', 'galpon', 'raza', 'cantidad_inicial', 'estado', 'fecha_ingreso')
    search_fields = ('codigo_lote', 'raza')
    list_filter = ('estado', 'fecha_ingreso')
    inlines = [PerfilSanitarioLoteInline, VisitaVeterinariaInline]

# ModelAdmin adicional #2 (para cumplir "mínimo 3 con ModelAdmin")
@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'colegiatura', 'especialidad', 'telefono')
    search_fields = ('nombre_completo', 'colegiatura')

# ModelAdmin adicional #3
@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_insumo', 'unidad_medida', 'stock_minimo')
    list_filter = ('tipo_insumo',)
# ===================================================================
# REGISTRO SIMPLE DEL RESTO DE MODELOS
# ===================================================================
admin.site.register(LicenciaSanitaria)
admin.site.register(InspeccionSanitaria)
admin.site.register(ContratoProveedor)
admin.site.register(Galpon)
admin.site.register(Equipamiento)
admin.site.register(FormulaAlimento)
admin.site.register(AlmacenAlimento)
admin.site.register(SuministroAlimento)
admin.site.register(VacunaMedicamento)
admin.site.register(PlanVacunacionLote)
admin.site.register(ProduccionHuevo)
admin.site.register(Cliente)
admin.site.register(Transporte)
admin.site.register(OrdenVenta)
admin.site.register(DetalleFormula)
admin.site.register(DetalleVenta)
admin.site.register(MantenimientoEquipamiento)
admin.site.register(CompraMateriaPrima)
