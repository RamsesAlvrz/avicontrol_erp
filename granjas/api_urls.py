
from rest_framework.routers import DefaultRouter
from .api_views import (
    EquipamientoViewSet,
    OrdenVentaViewSet,
    VeterinarioViewSet,
    LoteViewSet
)

router = DefaultRouter()

# Recursos de la Parte 1
router.register(
    'equipamientos',
    EquipamientoViewSet,
    basename='equipamiento'
)

router.register(
    'ordenes',
    OrdenVentaViewSet,
    basename='ordenventa'
)

# Recursos de la Parte 2
router.register(
    'veterinarios',
    VeterinarioViewSet,
    basename='veterinario'
)

router.register(
    'lotes',
    LoteViewSet,
    basename='lote'
)

urlpatterns = router.urls
