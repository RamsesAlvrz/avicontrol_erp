from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# ==========================================
# VISTAS GRANJA (CRUD Y CONSULTAS OPTIMIZADAS)
# ==========================================
def granja_list(request):
    """
    Ejercicio 6: Optimización de relación 1:1 (LicenciaSanitaria) 
    utilizando select_related (realiza JOIN en la BD).
    """
    granjas = Granja.objects.select_related('licencia_sanitaria').all().order_by('-id')
    return render(request, 'granjas/granja_list.html', {'granjas': granjas})


def granja_detail(request, pk):
    """
    Ejercicio 6: Vista de detalle optimizada.
    - select_related: Carga la relación 1:1 (LicenciaSanitaria).
    - prefetch_related: Carga la relación 1:N (Inspecciones) y N:M (Contratos/Proveedores).
    """
    granja = get_object_or_404(
        Granja.objects.select_related('licencia_sanitaria').prefetch_related(
            'inspecciones',                      # Relación 1:N
            'contratoproveedor_set__proveedor'   # Relación N:M a través del modelo intermedio
        ),
        pk=pk
    )
    return render(request, 'granjas/granja_detail.html', {'granja': granja})


def granja_create(request):
    form = GranjaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:granja_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Granja'})


def granja_update(request, pk):
    granja = get_object_or_404(Granja, pk=pk)
    form = GranjaForm(request.POST or None, instance=granja)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:granja_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Granja'})


def granja_delete(request, pk):
    granja = get_object_or_404(Granja, pk=pk)
    if request.method == 'POST':
        granja.delete()
        return redirect('granjas:granja_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': granja, 'redirect_url': 'granjas:granja_list'})


# ==========================================
# VISTAS GALPON (CRUD - Relacionada 1:N)
# ==========================================
def galpon_list(request):
    galpones = Galpon.objects.select_related('granja').all().order_by('-id')
    return render(request, 'granjas/galpon_list.html', {'galpones': galpones})

def galpon_create(request):
    form = GalponForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:galpon_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Galpón'})

def galpon_update(request, pk):
    galpon = get_object_or_404(Galpon, pk=pk)
    form = GalponForm(request.POST or None, instance=galpon)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:galpon_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Galpón'})

def galpon_delete(request, pk):
    galpon = get_object_or_404(Galpon, pk=pk)
    if request.method == 'POST':
        galpon.delete()
        return redirect('granjas:galpon_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': galpon, 'redirect_url': 'granjas:galpon_list'})


# ==========================================
# VISTAS LOTE (CRUD - Relacionada 1:N)
# ==========================================
def lote_list(request):
    lotes = Lote.objects.select_related('galpon__granja').all().order_by('-id')
    return render(request, 'granjas/lote_list.html', {'lotes': lotes})

def lote_create(request):
    form = LoteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:lote_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Lote de Aves'})

def lote_update(request, pk):
    lote = get_object_or_404(Lote, pk=pk)
    form = LoteForm(request.POST or None, instance=lote)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:lote_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Lote'})

def lote_delete(request, pk):
    lote = get_object_or_404(Lote, pk=pk)
    if request.method == 'POST':
        lote.delete()
        return redirect('granjas:lote_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': lote, 'redirect_url': 'granjas:lote_list'})


# ==========================================
# VISTAS EQUIPAMIENTO Y PROVEEDOR (CRUD)
# ==========================================
def equipamiento_list(request):
    equipos = Equipamiento.objects.all().order_by('-id')
    return render(request, 'granjas/equipamiento_list.html', {'equipos': equipos})

def equipamiento_create(request):
    form = EquipamientoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:equipamiento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Equipamiento'})

def equipamiento_update(request, pk):
    equipo = get_object_or_404(Equipamiento, pk=pk)
    form = EquipamientoForm(request.POST or None, instance=equipo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:equipamiento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Equipamiento'})

def equipamiento_delete(request, pk):
    equipo = get_object_or_404(Equipamiento, pk=pk)
    if request.method == 'POST':
        equipo.delete()
        return redirect('granjas:equipamiento_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': equipo, 'redirect_url': 'granjas:equipamiento_list'})

def proveedor_list(request):
    proveedores = Proveedor.objects.all().order_by('-id')
    return render(request, 'granjas/proveedor_list.html', {'proveedores': proveedores})

def proveedor_create(request):
    form = ProveedorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:proveedor_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Proveedor'})

def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    form = ProveedorForm(request.POST or None, instance=proveedor)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:proveedor_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Proveedor'})

def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('granjas:proveedor_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': proveedor, 'redirect_url': 'granjas:proveedor_list'})


# ==========================================
# VISTAS NUTRICIÓN Y ALMACÉN (CRUD)
# ==========================================
def materiaprima_list(request):
    materias = MateriaPrima.objects.all().order_by('-id')
    return render(request, 'granjas/materiaprima_list.html', {'materias': materias})

def materiaprima_create(request):
    form = MateriaPrimaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:materiaprima_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Materia Prima'})

def materiaprima_update(request, pk):
    materia = get_object_or_404(MateriaPrima, pk=pk)
    form = MateriaPrimaForm(request.POST or None, instance=materia)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:materiaprima_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Materia Prima'})

def materiaprima_delete(request, pk):
    materia = get_object_or_404(MateriaPrima, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('granjas:materiaprima_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': materia, 'redirect_url': 'granjas:materiaprima_list'})


def formulaalimento_list(request):
    formulas = FormulaAlimento.objects.select_related('materia_prima').all().order_by('-id')
    return render(request, 'granjas/formulaalimento_list.html', {'formulas': formulas})

def formulaalimento_create(request):
    form = FormulaAlimentoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:formulaalimento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Fórmula de Alimento'})

def formulaalimento_update(request, pk):
    formula = get_object_or_404(FormulaAlimento, pk=pk)
    form = FormulaAlimentoForm(request.POST or None, instance=formula)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:formulaalimento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Fórmula de Alimento'})

def formulaalimento_delete(request, pk):
    formula = get_object_or_404(FormulaAlimento, pk=pk)
    if request.method == 'POST':
        formula.delete()
        return redirect('granjas:formulaalimento_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': formula, 'redirect_url': 'granjas:formulaalimento_list'})


def almacenalimento_list(request):
    almacenes = AlmacenAlimento.objects.select_related('formula').all().order_by('-id')
    return render(request, 'granjas/almacenalimento_list.html', {'almacenes': almacenes})

def almacenalimento_create(request):
    form = AlmacenAlimentoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:almacenalimento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Almacén de Alimento'})

def almacenalimento_update(request, pk):
    almacen = get_object_or_404(AlmacenAlimento, pk=pk)
    form = AlmacenAlimentoForm(request.POST or None, instance=almacen)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:almacenalimento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Almacén de Alimento'})

def almacenalimento_delete(request, pk):
    almacen = get_object_or_404(AlmacenAlimento, pk=pk)
    if request.method == 'POST':
        almacen.delete()
        return redirect('granjas:almacenalimento_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': almacen, 'redirect_url': 'granjas:almacenalimento_list'})


def suministroalimento_list(request):
    suministros = SuministroAlimento.objects.select_related('almacen', 'lote', 'formula').all().order_by('-id')
    return render(request, 'granjas/suministroalimento_list.html', {'suministros': suministros})

def suministroalimento_create(request):
    form = SuministroAlimentoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:suministroalimento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Suministro de Alimento'})

def suministroalimento_update(request, pk):
    suministro = get_object_or_404(SuministroAlimento, pk=pk)
    form = SuministroAlimentoForm(request.POST or None, instance=suministro)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:suministroalimento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Suministro'})

def suministroalimento_delete(request, pk):
    suministro = get_object_or_404(SuministroAlimento, pk=pk)
    if request.method == 'POST':
        suministro.delete()
        return redirect('granjas:suministroalimento_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': suministro, 'redirect_url': 'granjas:suministroalimento_list'})


# ==========================================
# VISTAS SANIDAD Y VETERINARIO (CRUD)
# ==========================================
def vacunamedicamento_list(request):
    vacunas = VacunaMedicamento.objects.all().order_by('-id')
    return render(request, 'granjas/vacunamedicamento_list.html', {'vacunas': vacunas})

def vacunamedicamento_create(request):
    form = VacunaMedicamentoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:vacunamedicamento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Vacuna / Medicamento'})

def vacunamedicamento_update(request, pk):
    vacuna = get_object_or_404(VacunaMedicamento, pk=pk)
    form = VacunaMedicamentoForm(request.POST or None, instance=vacuna)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:vacunamedicamento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Vacuna / Medicamento'})

def vacunamedicamento_delete(request, pk):
    vacuna = get_object_or_404(VacunaMedicamento, pk=pk)
    if request.method == 'POST':
        vacuna.delete()
        return redirect('granjas:vacunamedicamento_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': vacuna, 'redirect_url': 'granjas:vacunamedicamento_list'})


def veterinario_list(request):
    veterinarios = Veterinario.objects.all().order_by('-id')
    return render(request, 'granjas/veterinario_list.html', {'veterinarios': veterinarios})

def veterinario_create(request):
    form = VeterinarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:veterinario_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Veterinario'})

def veterinario_update(request, pk):
    vet = get_object_or_404(Veterinario, pk=pk)
    form = VeterinarioForm(request.POST or None, instance=vet)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:veterinario_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Veterinario'})

def veterinario_delete(request, pk):
    vet = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        vet.delete()
        return redirect('granjas:veterinario_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': vet, 'redirect_url': 'granjas:veterinario_list'})


def planvacunacion_list(request):
    planes = PlanVacunacionLote.objects.select_related('lote', 'vacuna', 'veterinario').all().order_by('-id')
    return render(request, 'granjas/planvacunacion_list.html', {'planes': planes})

def planvacunacion_create(request):
    form = PlanVacunacionLoteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:planvacunacion_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Plan de Vacunación'})

def planvacunacion_update(request, pk):
    plan = get_object_or_404(PlanVacunacionLote, pk=pk)
    form = PlanVacunacionLoteForm(request.POST or None, instance=plan)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:planvacunacion_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Plan de Vacunación'})

def planvacunacion_delete(request, pk):
    plan = get_object_or_404(PlanVacunacionLote, pk=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('granjas:planvacunacion_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': plan, 'redirect_url': 'granjas:planvacunacion_list'})


# ==========================================
# VISTAS PRODUCCIÓN Y VENTAS (CRUD)
# ==========================================
def produccionhuevo_list(request):
    producciones = ProduccionHuevo.objects.all().order_by('-id')
    return render(request, 'granjas/produccionhuevo_list.html', {'producciones': producciones})

def produccionhuevo_create(request):
    form = ProduccionHuevoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:produccionhuevo_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Cosecha de Huevo'})

def produccionhuevo_update(request, pk):
    produccion = get_object_or_404(ProduccionHuevo, pk=pk)
    form = ProduccionHuevoForm(request.POST or None, instance=produccion)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:produccionhuevo_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Cosecha de Huevo'})

def produccionhuevo_delete(request, pk):
    produccion = get_object_or_404(ProduccionHuevo, pk=pk)
    if request.method == 'POST':
        produccion.delete()
        return redirect('granjas:produccionhuevo_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': produccion, 'redirect_url': 'granjas:produccionhuevo_list'})


def cliente_list(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, 'granjas/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:cliente_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Cliente'})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:cliente_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Cliente'})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('granjas:cliente_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': cliente, 'redirect_url': 'granjas:cliente_list'})


def transporte_list(request):
    transportes = Transporte.objects.all().order_by('-id')
    return render(request, 'granjas/transporte_list.html', {'transportes': transportes})

def transporte_create(request):
    form = TransporteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:transporte_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Transporte'})

def transporte_update(request, pk):
    transporte = get_object_or_404(Transporte, pk=pk)
    form = TransporteForm(request.POST or None, instance=transporte)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:transporte_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Transporte'})

def transporte_delete(request, pk):
    transporte = get_object_or_404(Transporte, pk=pk)
    if request.method == 'POST':
        transporte.delete()
        return redirect('granjas:transporte_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': transporte, 'redirect_url': 'granjas:transporte_list'})


def ordenventa_list(request):
    ordenes = OrdenVenta.objects.select_related('cliente', 'transporte').all().order_by('-id')
    return render(request, 'granjas/ordenventa_list.html', {'ordenes': ordenes})

def ordenventa_create(request):
    form = OrdenVentaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:ordenventa_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Orden de Venta'})

def ordenventa_update(request, pk):
    orden = get_object_or_404(OrdenVenta, pk=pk)
    form = OrdenVentaForm(request.POST or None, instance=orden)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:ordenventa_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Orden de Venta'})

def ordenventa_delete(request, pk):
    orden = get_object_or_404(OrdenVenta, pk=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('granjas:ordenventa_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': orden, 'redirect_url': 'granjas:ordenventa_list'})


# ==========================================
# VISTAS TABLAS DE DETALLE Y COMPRAS (CRUD)
# ==========================================
def detalleformula_list(request):
    detalles = DetalleFormula.objects.select_related('formula', 'materia_prima').all().order_by('-id')
    return render(request, 'granjas/detalleformula_list.html', {'detalles': detalles})

def detalleformula_create(request):
    form = DetalleFormulaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:detalleformula_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Detalle de Fórmula'})

def detalleformula_update(request, pk):
    detalle = get_object_or_404(DetalleFormula, pk=pk)
    form = DetalleFormulaForm(request.POST or None, instance=detalle)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:detalleformula_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Detalle de Fórmula'})

def detalleformula_delete(request, pk):
    detalle = get_object_or_404(DetalleFormula, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('granjas:detalleformula_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': detalle, 'redirect_url': 'granjas:detalleformula_list'})


def detalleventa_list(request):
    detalles = DetalleVenta.objects.select_related('orden', 'produccion_huevo', 'lote').all().order_by('-id')
    return render(request, 'granjas/detalleventa_list.html', {'detalles': detalles})

def detalleventa_create(request):
    form = DetalleVentaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:detalleventa_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Detalle de Venta'})

def detalleventa_update(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    form = DetalleVentaForm(request.POST or None, instance=detalle)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:detalleventa_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Detalle de Venta'})

def detalleventa_delete(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('granjas:detalleventa_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': detalle, 'redirect_url': 'granjas:detalleventa_list'})


def mantenimientoequipamiento_list(request):
    mantenimientos = MantenimientoEquipamiento.objects.select_related('equipamiento', 'tecnico').all().order_by('-id')
    return render(request, 'granjas/mantenimientoequipamiento_list.html', {'mantenimientos': mantenimientos})

def mantenimientoequipamiento_create(request):
    form = MantenimientoEquipamientoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:mantenimientoequipamiento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Mantenimiento de Equipo'})

def mantenimientoequipamiento_update(request, pk):
    mantenimiento = get_object_or_404(MantenimientoEquipamiento, pk=pk)
    form = MantenimientoEquipamientoForm(request.POST or None, instance=mantenimiento)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:mantenimientoequipamiento_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Mantenimiento'})

def mantenimientoequipamiento_delete(request, pk):
    mantenimiento = get_object_or_404(MantenimientoEquipamiento, pk=pk)
    if request.method == 'POST':
        mantenimiento.delete()
        return redirect('granjas:mantenimientoequipamiento_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': mantenimiento, 'redirect_url': 'granjas:mantenimientoequipamiento_list'})


def compramateriaprima_list(request):
    compras = CompraMateriaPrima.objects.select_related('proveedor', 'materia_prima').all().order_by('-id')
    return render(request, 'granjas/compramateriaprima_list.html', {'compras': compras})

def compramateriaprima_create(request):
    form = CompraMateriaPrimaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:compramateriaprima_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Compra de Materia Prima'})

def compramateriaprima_update(request, pk):
    compra = get_object_or_404(CompraMateriaPrima, pk=pk)
    form = CompraMateriaPrimaForm(request.POST or None, instance=compra)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:compramateriaprima_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Compra'})

def compramateriaprima_delete(request, pk):
    compra = get_object_or_404(CompraMateriaPrima, pk=pk)
    if request.method == 'POST':
        compra.delete()
        return redirect('granjas:compramateriaprima_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': compra, 'redirect_url': 'granjas:compramateriaprima_list'})
# ============================================
# PARTE 2 - EJERCICIO 12: Vista de detalle de Lote con relaciones
# ============================================
def lote_detail(request, pk):
    """
    - select_related('perfil_sanitario'): resuelve la relación 1:1 en el mismo JOIN.
    - prefetch_related: trae las visitas veterinarias (N:M a través de VisitaVeterinaria)
      y también el galpón (para mostrar contexto) en consultas optimizadas.
    """
    lote = get_object_or_404(
        Lote.objects.select_related('perfil_sanitario', 'galpon').prefetch_related(
            'visitas_veterinarias__veterinario'
        ),
        pk=pk
    )
    return render(request, 'granjas/lote_detail.html', {'lote': lote})
# ============================================
# PARTE 2 - EJERCICIO 13: CRUD de VisitaVeterinaria (modelo intermedio)
# ============================================
def visita_list(request):
    visitas = VisitaVeterinaria.objects.select_related('lote', 'veterinario').order_by('-fecha_visita')
    return render(request, 'granjas/visita_list.html', {'visitas': visitas})

def visita_create(request):
    form = VisitaVeterinariaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:visita_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Registrar Visita Veterinaria'})

def visita_update(request, pk):
    visita = get_object_or_404(VisitaVeterinaria, pk=pk)
    form = VisitaVeterinariaForm(request.POST or None, instance=visita)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('granjas:visita_list')
    return render(request, 'granjas/generic_form.html', {'form': form, 'titulo': 'Actualizar Visita Veterinaria'})

def visita_delete(request, pk):
    visita = get_object_or_404(VisitaVeterinaria, pk=pk)
    if request.method == 'POST':
        visita.delete()
        return redirect('granjas:visita_list')
    return render(request, 'granjas/generic_confirm_delete.html', {'objeto': visita, 'redirect_url': 'granjas:visita_list'})