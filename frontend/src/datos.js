// ==========================================================
// DATOS ESCRITOS A MANO (misma forma que devuelve la API de la Semana 8)
// Todavía no se consume la API: eso se hace en la Semana 12.
// ==========================================================

// ---------- PARTE 1: módulo compartido ----------

// GET /api/equipamientos/
export const equipamientosData = [
  { id: 1, codigo: 'SEN-001', nombre: 'Sensor de Temperatura Galpón 1', tipo: 'SENSOR', estado: 'OPERATIVO' },
  { id: 2, codigo: 'COM-014', nombre: 'Comedero Automático Línea A', tipo: 'COMEDERO', estado: 'OPERATIVO' },
  { id: 3, codigo: 'EXT-007', nombre: 'Extractor de Aire Norte', tipo: 'EXTRACTOR', estado: 'MANTENIMIENTO' },
]

// GET /api/ordenes/  (OrdenVenta con cliente y detalles anidados, relación 1:N)
export const ordenesData = [
  {
    id: 1,
    numero_comprobante: 'F001-000125',
    fecha_emision: '2026-09-10',
    monto_total: '1250.00',
    estado_entrega: 'ENTREGADO',
    cliente: { id: 1, razon_social: 'Distribuidora Santa Rosa SAC' },
    detalles: [
      { id: 11, cantidad: 100, precio_unitario: '7.50', subtotal: '750.00' },
      { id: 12, cantidad: 50, precio_unitario: '10.00', subtotal: '500.00' },
    ],
  },
  {
    id: 2,
    numero_comprobante: 'F001-000126',
    fecha_emision: '2026-09-12',
    monto_total: '480.00',
    estado_entrega: 'PENDIENTE',
    cliente: { id: 2, razon_social: 'Bodega El Granjero' },
    detalles: [{ id: 13, cantidad: 60, precio_unitario: '8.00', subtotal: '480.00' }],
  },
]

// ---------- PARTE 2: investigación propia ----------

// Entidad: Veterinario
export const veterinariosData = [
  { id: 1, nombre_completo: 'Dr. Carlos Mendoza', colegiatura: 'CMVP-4589', especialidad: 'Epidemiología Avícola', telefono: '987654321' },
  { id: 2, nombre_completo: 'Dra. Ana Gutiérrez', colegiatura: 'CMVP-6120', especialidad: 'Nutrición y Patología', telefono: '912345678' },
]

// Relación 1:1: PerfilSanitarioLote
export const perfilesSanitariosData = [
  { id: 1, lote_codigo: 'LOT-2026-A', peso_promedio_gr: '1850.40', indice_mortalidad: '2.10', certificado_sanitario: true },
  { id: 2, lote_codigo: 'LOT-2026-B', peso_promedio_gr: '1620.00', indice_mortalidad: '6.80', certificado_sanitario: false },
  { id: 3, lote_codigo: 'LOT-2026-C', peso_promedio_gr: '1910.15', indice_mortalidad: '1.50', certificado_sanitario: true },
]

// Modelo intermedio N:M (through): VisitaVeterinaria, agrupado por veterinario
export const historialVisitasData = [
  {
    id: 1,
    veterinario: 'Dr. Carlos Mendoza',
    visitas: [
      { id: 201, lote_codigo: 'LOT-2026-A', fecha: '2026-03-01', diagnostico: 'Aves con excelente ganancia de peso.', estado: 'SALUDABLE' },
      { id: 202, lote_codigo: 'LOT-2026-B', fecha: '2026-03-05', diagnostico: 'Cuadro respiratorio leve detectado.', estado: 'OBSERVACION' },
    ],
  },
  {
    id: 2,
    veterinario: 'Dra. Ana Gutiérrez',
    visitas: [
      { id: 203, lote_codigo: 'LOT-2026-C', fecha: '2026-03-08', diagnostico: 'Control de rutina conforme.', estado: 'SALUDABLE' },
    ],
  },
]
