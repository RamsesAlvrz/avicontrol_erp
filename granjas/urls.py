from django.urls import path
from . import views

app_name = 'granjas'

urlpatterns = [
    # Granjas
    path('granjas/', views.granja_list, name='granja_list'),
    path('granjas/<int:pk>/', views.granja_detail, name='granja_detail'),
    path('granjas/crear/', views.granja_create, name='granja_create'),
    path('granjas/editar/<int:pk>/', views.granja_update, name='granja_update'),
    path('granjas/eliminar/<int:pk>/', views.granja_delete, name='granja_delete'),
    
    # Galpones
    path('galpones/', views.galpon_list, name='galpon_list'),
    path('galpones/crear/', views.galpon_create, name='galpon_create'),
    path('galpones/editar/<int:pk>/', views.galpon_update, name='galpon_update'),
    path('galpones/eliminar/<int:pk>/', views.galpon_delete, name='galpon_delete'),

    # Lotes
    path('lotes/', views.lote_list, name='lote_list'),
    path('lotes/crear/', views.lote_create, name='lote_create'),
    path('lotes/editar/<int:pk>/', views.lote_update, name='lote_update'),
    path('lotes/eliminar/<int:pk>/', views.lote_delete, name='lote_delete'),
    path('lotes/<int:pk>/', views.lote_detail, name='lote_detail'),

    # Equipamiento
    path('equipos/', views.equipamiento_list, name='equipamiento_list'),
    path('equipos/crear/', views.equipamiento_create, name='equipamiento_create'),
    path('equipos/editar/<int:pk>/', views.equipamiento_update, name='equipamiento_update'),
    path('equipos/eliminar/<int:pk>/', views.equipamiento_delete, name='equipamiento_delete'),

    # Proveedores
    path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('proveedores/crear/', views.proveedor_create, name='proveedor_create'),
    path('proveedores/editar/<int:pk>/', views.proveedor_update, name='proveedor_update'),
    path('proveedores/eliminar/<int:pk>/', views.proveedor_delete, name='proveedor_delete'),

    # Materia Prima
    path('materias-primas/', views.materiaprima_list, name='materiaprima_list'),
    path('materias-primas/crear/', views.materiaprima_create, name='materiaprima_create'),
    path('materias-primas/editar/<int:pk>/', views.materiaprima_update, name='materiaprima_update'),
    path('materias-primas/eliminar/<int:pk>/', views.materiaprima_delete, name='materiaprima_delete'),

    # Formulas de Alimento
    path('formulas/', views.formulaalimento_list, name='formulaalimento_list'),
    path('formulas/crear/', views.formulaalimento_create, name='formulaalimento_create'),
    path('formulas/editar/<int:pk>/', views.formulaalimento_update, name='formulaalimento_update'),
    path('formulas/eliminar/<int:pk>/', views.formulaalimento_delete, name='formulaalimento_delete'),

    # Almacén de Alimento
    path('almacenes-alimento/', views.almacenalimento_list, name='almacenalimento_list'),
    path('almacenes-alimento/crear/', views.almacenalimento_create, name='almacenalimento_create'),
    path('almacenes-alimento/editar/<int:pk>/', views.almacenalimento_update, name='almacenalimento_update'),
    path('almacenes-alimento/eliminar/<int:pk>/', views.almacenalimento_delete, name='almacenalimento_delete'),

    # Suministros de Alimento
    path('suministros-alimento/', views.suministroalimento_list, name='suministroalimento_list'),
    path('suministros-alimento/crear/', views.suministroalimento_create, name='suministroalimento_create'),
    path('suministros-alimento/editar/<int:pk>/', views.suministroalimento_update, name='suministroalimento_update'),
    path('suministros-alimento/eliminar/<int:pk>/', views.suministroalimento_delete, name='suministroalimento_delete'),

    # Vacunas y Medicamentos
    path('vacunas/', views.vacunamedicamento_list, name='vacunamedicamento_list'),
    path('vacunas/crear/', views.vacunamedicamento_create, name='vacunamedicamento_create'),
    path('vacunas/editar/<int:pk>/', views.vacunamedicamento_update, name='vacunamedicamento_update'),
    path('vacunas/eliminar/<int:pk>/', views.vacunamedicamento_delete, name='vacunamedicamento_delete'),

    # Veterinarios
    path('veterinarios/', views.veterinario_list, name='veterinario_list'),
    path('veterinarios/crear/', views.veterinario_create, name='veterinario_create'),
    path('veterinarios/editar/<int:pk>/', views.veterinario_update, name='veterinario_update'),
    path('veterinarios/eliminar/<int:pk>/', views.veterinario_delete, name='veterinario_delete'),

    # Plan de Vacunación
    path('planes-vacunacion/', views.planvacunacion_list, name='planvacunacion_list'),
    path('planes-vacunacion/crear/', views.planvacunacion_create, name='planvacunacion_create'),
    path('planes-vacunacion/editar/<int:pk>/', views.planvacunacion_update, name='planvacunacion_update'),
    path('planes-vacunacion/eliminar/<int:pk>/', views.planvacunacion_delete, name='planvacunacion_delete'),

    # Producción de Huevo
    path('produccion-huevo/', views.produccionhuevo_list, name='produccionhuevo_list'),
    path('produccion-huevo/crear/', views.produccionhuevo_create, name='produccionhuevo_create'),
    path('produccion-huevo/editar/<int:pk>/', views.produccionhuevo_update, name='produccionhuevo_update'),
    path('produccion-huevo/eliminar/<int:pk>/', views.produccionhuevo_delete, name='produccionhuevo_delete'),

    # Clientes
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),

    # Transporte
    path('transportes/', views.transporte_list, name='transporte_list'),
    path('transportes/crear/', views.transporte_create, name='transporte_create'),
    path('transportes/editar/<int:pk>/', views.transporte_update, name='transporte_update'),
    path('transportes/eliminar/<int:pk>/', views.transporte_delete, name='transporte_delete'),

    # Ordenes de Venta
    path('ordenes-venta/', views.ordenventa_list, name='ordenventa_list'),
    path('ordenes-venta/crear/', views.ordenventa_create, name='ordenventa_create'),
    path('ordenes-venta/editar/<int:pk>/', views.ordenventa_update, name='ordenventa_update'),
    path('ordenes-venta/eliminar/<int:pk>/', views.ordenventa_delete, name='ordenventa_delete'),

    # Detalles de Fórmula
    path('detalles-formula/', views.detalleformula_list, name='detalleformula_list'),
    path('detalles-formula/crear/', views.detalleformula_create, name='detalleformula_create'),
    path('detalles-formula/editar/<int:pk>/', views.detalleformula_update, name='detalleformula_update'),
    path('detalles-formula/eliminar/<int:pk>/', views.detalleformula_delete, name='detalleformula_delete'),

    # Detalles de Venta
    path('detalles-venta/', views.detalleventa_list, name='detalleventa_list'),
    path('detalles-venta/crear/', views.detalleventa_create, name='detalleventa_create'),
    path('detalles-venta/editar/<int:pk>/', views.detalleventa_update, name='detalleventa_update'),
    path('detalles-venta/eliminar/<int:pk>/', views.detalleventa_delete, name='detalleventa_delete'),

    # Mantenimiento Equipamiento
    path('mantenimientos/', views.mantenimientoequipamiento_list, name='mantenimientoequipamiento_list'),
    path('mantenimientos/crear/', views.mantenimientoequipamiento_create, name='mantenimientoequipamiento_create'),
    path('mantenimientos/editar/<int:pk>/', views.mantenimientoequipamiento_update, name='mantenimientoequipamiento_update'),
    path('mantenimientos/eliminar/<int:pk>/', views.mantenimientoequipamiento_delete, name='mantenimientoequipamiento_delete'),

    # Compras Materia Prima
    path('compras-materia-prima/', views.compramateriaprima_list, name='compramateriaprima_list'),
    path('compras-materia-prima/crear/', views.compramateriaprima_create, name='compramateriaprima_create'),
    path('compras-materia-prima/editar/<int:pk>/', views.compramateriaprima_update, name='compramateriaprima_update'),
    path('compras-materia-prima/eliminar/<int:pk>/', views.compramateriaprima_delete, name='compramateriaprima_delete'),
    # Visitas Veterinarias (CRUD del modelo intermedio)
    path('visitas/', views.visita_list, name='visita_list'),
    path('visitas/crear/', views.visita_create, name='visita_create'),
    path('visitas/editar/<int:pk>/', views.visita_update, name='visita_update'),
    path('visitas/eliminar/<int:pk>/', views.visita_delete, name='visita_delete'),
]