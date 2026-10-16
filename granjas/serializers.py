
from rest_framework import serializers
from .models import Equipamiento


class EquipamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamiento
        fields = ['id', 'codigo', 'nombre', 'tipo', 'estado']

    def validate_codigo(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "El código debe tener al menos 3 caracteres."
            )
        return value

    
# Serializers para las ordenes de venta
from .models import OrdenVenta, DetalleVenta, Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'razon_social']


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = [
            'id',
            'cantidad',
            'precio_unitario',
            'subtotal'
        ]


class OrdenVentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    detalles = DetalleVentaSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = OrdenVenta
        fields = [
            'id',
            'numero_comprobante',
            'fecha_emision',
            'monto_total',
            'estado_entrega',
            'cliente',
            'detalles'
        ]


# ==========================================
# LABORATORIO 08 - PARTE 2 - EJERCICIO 10
# ==========================================

from .models import Veterinario, Lote, PerfilSanitarioLote


# Serializer de Veterinario con validacion
class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = [
            'id',
            'nombre_completo',
            'colegiatura',
            'especialidad',
            'telefono'
        ]

    def validate_colegiatura(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "La colegiatura debe tener al menos 5 caracteres."
            )
        return value


# Serializer de Lote
class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = [
            'id',
            'galpon',
            'codigo_lote',
            'cantidad_inicial',
            'fecha_ingreso',
            'raza',
            'estado'
        ]


# Serializer de Perfil Sanitario
class PerfilSanitarioLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilSanitarioLote
        fields = [
            'id',
            'lote',
            'peso_promedio_gr',
            'indice_mortalidad',
            'conversion_alimenticia',
            'certificado_sanitario',
            'fecha_evaluacion'
        ]
