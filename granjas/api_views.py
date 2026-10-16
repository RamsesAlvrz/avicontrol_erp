
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Equipamiento, OrdenVenta, Veterinario, Lote
from .serializers import (
    EquipamientoSerializer,
    OrdenVentaSerializer,
    VeterinarioSerializer,
    LoteSerializer
)


# ViewSet de Equipamiento
class EquipamientoViewSet(viewsets.ModelViewSet):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer

    # Busqueda y ordenamiento
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    search_fields = ['codigo', 'nombre', 'tipo']
    ordering_fields = ['id', 'codigo', 'nombre']
    ordering = ['id']


# ViewSet de OrdenVenta
class OrdenVentaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrdenVentaSerializer

    def get_queryset(self):
        queryset = OrdenVenta.objects.select_related(
            'cliente'
        ).prefetch_related(
            'detalles'
        )

        # Filtrar por estado de entrega
        estado = self.request.query_params.get('estado')

        if estado:
            queryset = queryset.filter(
                estado_entrega=estado
            )

        return queryset

    # Accion personalizada
    @action(detail=False, methods=['get'])
    def entregadas(self, request):
        queryset = self.get_queryset().entregadas()

        serializer = self.get_serializer(
            queryset,
            many=True
        )

        return Response(serializer.data)


# ==========================================
# LABORATORIO 08 - PARTE 2 - EJERCICIO 11
# ==========================================

# API CRUD de Veterinarios
class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer


# API CRUD de Lotes
class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
