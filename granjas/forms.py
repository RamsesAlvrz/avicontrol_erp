from django import forms
from .models import *

class GranjaForm(forms.ModelForm):
    class Meta:
        model = Granja
        fields = ['nombre', 'direccion', 'capacidad_total']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EquipamientoForm(forms.ModelForm):
    class Meta:
        model = Equipamiento
        fields = ['codigo', 'nombre', 'tipo', 'estado']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['razon_social', 'ruc', 'telefono', 'email']
        widgets = {
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class GalponForm(forms.ModelForm):
    class Meta:
        model = Galpon
        fields = ['granja', 'numero', 'tipo_galpon', 'capacidad']
        widgets = {
            'granja': forms.Select(attrs={'class': 'form-select'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_galpon': forms.Select(attrs={'class': 'form-select'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = ['galpon', 'codigo_lote', 'cantidad_inicial', 'fecha_ingreso', 'raza', 'estado']
        widgets = {
            'galpon': forms.Select(attrs={'class': 'form-select'}),
            'codigo_lote': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
class MateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = ['nombre', 'tipo_insumo', 'unidad_medida', 'stock_minimo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_insumo': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_medida': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FormulaAlimentoForm(forms.ModelForm):
    class Meta:
        model = FormulaAlimento
        fields = ['materia_prima', 'nombre_formula', 'etapa_nutricional', 'porcentaje_proteina']
        widgets = {
            'materia_prima': forms.Select(attrs={'class': 'form-select'}),
            'nombre_formula': forms.TextInput(attrs={'class': 'form-control'}),
            'etapa_nutricional': forms.TextInput(attrs={'class': 'form-control'}),
            'porcentaje_proteina': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class AlmacenAlimentoForm(forms.ModelForm):
    class Meta:
        model = AlmacenAlimento
        fields = ['formula', 'nombre_almacen', 'capacidad_kilos', 'stock_disponible']
        widgets = {
            'formula': forms.Select(attrs={'class': 'form-select'}),
            'nombre_almacen': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_kilos': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SuministroAlimentoForm(forms.ModelForm):
    class Meta:
        model = SuministroAlimento
        fields = ['almacen', 'lote', 'formula', 'cantidad_kg']
        widgets = {
            'almacen': forms.Select(attrs={'class': 'form-select'}),
            'lote': forms.Select(attrs={'class': 'form-select'}),
            'formula': forms.Select(attrs={'class': 'form-select'}),
            'cantidad_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class VacunaMedicamentoForm(forms.ModelForm):
    class Meta:
        model = VacunaMedicamento
        fields = ['nombre_comercial', 'principio_activo', 'via_administracion', 'dosis_recomendada']
        widgets = {
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'principio_activo': forms.TextInput(attrs={'class': 'form-control'}),
            'via_administracion': forms.TextInput(attrs={'class': 'form-control'}),
            'dosis_recomendada': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre_completo', 'colegiatura', 'especialidad', 'telefono']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'colegiatura': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PlanVacunacionLoteForm(forms.ModelForm):
    class Meta:
        model = PlanVacunacionLote
        fields = ['lote', 'vacuna', 'veterinario', 'dosis', 'fecha_programada', 'fecha_aplicada']
        widgets = {
            'lote': forms.Select(attrs={'class': 'form-select'}),
            'vacuna': forms.Select(attrs={'class': 'form-select'}),
            'veterinario': forms.Select(attrs={'class': 'form-select'}),
            'dosis': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_programada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_aplicada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ProduccionHuevoForm(forms.ModelForm):
    class Meta:
        model = ProduccionHuevo
        fields = ['categoria', 'fecha_cosecha', 'cantidad_jabas', 'observaciones']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'fecha_cosecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_jabas': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['razon_social', 'ruc_dni', 'direccion', 'telefono']
        widgets = {
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc_dni': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = ['placa', 'conductor', 'tipo_vehiculo', 'capacidad_carga_kg']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'conductor': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_vehiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_carga_kg': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class OrdenVentaForm(forms.ModelForm):
    class Meta:
        model = OrdenVenta
        fields = ['cliente', 'transporte', 'numero_comprobante', 'fecha_emision', 'monto_total', 'estado_entrega']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'transporte': forms.Select(attrs={'class': 'form-select'}),
            'numero_comprobante': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estado_entrega': forms.Select(attrs={'class': 'form-select'}),
        }

class DetalleFormulaForm(forms.ModelForm):
    class Meta:
        model = DetalleFormula
        fields = ['formula', 'materia_prima', 'porcentaje', 'kilos_por_tonelada']
        widgets = {
            'formula': forms.Select(attrs={'class': 'form-select'}),
            'materia_prima': forms.Select(attrs={'class': 'form-select'}),
            'porcentaje': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'kilos_por_tonelada': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['orden', 'produccion_huevo', 'lote', 'cantidad', 'precio_unitario', 'subtotal']
        widgets = {
            'orden': forms.Select(attrs={'class': 'form-select'}),
            'produccion_huevo': forms.Select(attrs={'class': 'form-select'}),
            'lote': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class MantenimientoEquipamientoForm(forms.ModelForm):
    class Meta:
        model = MantenimientoEquipamiento
        fields = ['equipamiento', 'tecnico', 'fecha_mantenimiento', 'descripcion_trabajo']
        widgets = {
            'equipamiento': forms.Select(attrs={'class': 'form-select'}),
            'tecnico': forms.Select(attrs={'class': 'form-select'}),
            'fecha_mantenimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion_trabajo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CompraMateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = CompraMateriaPrima
        fields = ['proveedor', 'materia_prima', 'fecha_compra', 'cantidad', 'precio_unitario', 'costo_total']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-select'}),
            'materia_prima': forms.Select(attrs={'class': 'form-select'}),
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'costo_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        # ============================================
# PARTE 2 - EJERCICIO 13: Formulario del modelo intermedio
# ============================================
class VisitaVeterinariaForm(forms.ModelForm):
    class Meta:
        model = VisitaVeterinaria
        fields = ['lote', 'veterinario', 'fecha_visita', 'diagnostico', 'estado_lote']
        widgets = {
            'fecha_visita': forms.DateInput(attrs={'type': 'date'}),
            'diagnostico': forms.Textarea(attrs={'rows': 3}),
        }