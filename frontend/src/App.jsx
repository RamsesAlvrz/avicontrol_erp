import './App.css'

// ==========================================
// DATOS DE LA INVESTIGACIÓN PROPIA (Semana 8)
// ==========================================

// Entidad 1: Veterinario
const veterinariosData = [
  { id: 1, nombre_completo: "Dr. Carlos Mendoza", colegiatura: "CMVP-4589", especialidad: "Epidemiología Avícola", telefono: "987654321" },
  { id: 2, nombre_completo: "Dra. Ana Gutiérrez", colegiatura: "CMVP-6120", especialidad: "Nutrición y Patología", telefono: "912345678" }
];

// Entidad 2: PerfilSanitarioLote (Relación 1:1)
const perfilesSanitariosData = [
  { id: 1, lote_codigo: "LOT-2026-A", peso_promedio_gr: "1850.40", indice_mortalidad: "2.10", certificado_sanitario: true },
  { id: 2, lote_codigo: "LOT-2026-B", peso_promedio_gr: "1620.00", indice_mortalidad: "6.80", certificado_sanitario: false },
  { id: 3, lote_codigo: "LOT-2026-C", peso_promedio_gr: "1910.15", indice_mortalidad: "1.50", certificado_sanitario: true }
];

// Modelo Intermedio N:M through: VisitaVeterinaria (Listas anidadas)
const historialVisitasData = [
  {
    id: 1,
    veterinario: "Dr. Carlos Mendoza",
    visitas: [
      { id: 201, lote_codigo: "LOT-2026-A", fecha: "2026-03-01", diagnostico: "Aves con excelente ganancia de peso.", estado: "SALUDABLE" },
      { id: 202, lote_codigo: "LOT-2026-B", fecha: "2026-03-05", diagnostico: "Cuadro respiratorio leve detectado.", estado: "OBSERVACION" }
    ]
  },
  {
    id: 2,
    veterinario: "Dra. Ana Gutiérrez",
    visitas: [
      { id: 203, lote_codigo: "LOT-2026-C", fecha: "2026-03-08", diagnostico: "Control de rutina conforme.", estado: "SALUDABLE" }
    ]
  }
];

// ==========================================
// COMPONENTES DE LA INVESTIGACIÓN PROPIA
// ==========================================

// EJERCICIO 10: Listado de Veterinarios
export function ListaVeterinarios({ veterinarios = veterinariosData }) {
  if (!veterinarios || veterinarios.length === 0) {
    return <p className="mensaje-vacio">No hay médicos veterinarios registrados.</p>;
  }

  return (
    <div className="modulo-seccion">
      <h2>Directorio de Médicos Veterinarios (Entidad 1)</h2>
      <div className="grid-cards">
        {veterinarios.map((vet) => (
          <div key={vet.id} className="card-item">
            <h3>{vet.nombre_completo}</h3>
            <p><strong>Colegiatura:</strong> {vet.colegiatura}</p>
            <p><strong>Especialidad:</strong> {vet.especialidad}</p>
            <p><strong>Teléfono:</strong> {vet.telefono}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

// EJERCICIO 11: Perfiles Sanitarios con Renderizado Condicional y Estilos
export function ListaPerfilesSanitarios({ perfiles = perfilesSanitariosData }) {
  if (!perfiles || perfiles.length === 0) {
    return <p className="mensaje-vacio">No existen perfiles sanitarios evaluados.</p>;
  }

  return (
    <div className="modulo-seccion">
      <h2>Evaluación de Perfiles Sanitarios de Lotes (Entidad 2)</h2>
      <div className="grid-cards">
        {perfiles.map((perfil) => {
          const mortalidadNum = Number(perfil.indice_mortalidad);
          
          return (
            <div 
              key={perfil.id} 
              className="card-item"
              // Uso de style={{ }} dinámico exigido en la investigación
              style={{ borderTop: perfil.certificado_sanitario ? '5px solid #2e7d32' : '5px solid #c62828' }}
            >
              <h3>Lote: {perfil.lote_codigo}</h3>
              <p>Peso Promedio: {Number(perfil.peso_promedio_gr).toFixed(2)} g</p>
              <p>Mortalidad: <strong>{mortalidadNum.toFixed(2)}%</strong></p>
              
              {/* Condicional Ternario */}
              <p>
                Certificación SENASA: {perfil.certificado_sanitario ? (
                  <span className="badge-ok">VIGENTE</span>
                ) : (
                  <span className="badge-warn">PENDIENTE</span>
                )}
              </p>

              {/* Condicional && para Alerta de Mortalidad Crítica */}
              {mortalidadNum > 5.0 && (
                <div className="alerta-urgente">
                  ⚠ ALERTA SANITARIA: Índice de mortalidad crítico (&gt; 5%). Requiere inspección urgente.
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

// EJERCICIO 12: Relación Anidada y Conteo Calculado
export function ReporteVisitasAnidadas({ historial = historialVisitasData }) {
  return (
    <div className="modulo-seccion">
      <h2 style={{ color: '#0288d1', borderBottom: '2px solid #0288d1', paddingBottom: '6px' }}>
        Historial de Visitas Veterinarias (Relación N:M through Anidada)
      </h2>
      {historial.map((item) => (
        <div key={item.id} className="card-anidada">
          <h3>Especialista Responsable: {item.veterinario}</h3>
          {/* Conteo total calculado dinámicamente en JavaScript */}
          <p>Total de Atenciones Realizadas: <strong>{item.visitas.length} atenciones</strong></p>
          
          <h5>Listado de Lotes Atendidos:</h5>
          <ul>
            {/* map() anidado para recorrer las visitas del veterinario */}
            {item.visitas.map((visita) => (
              <li key={visita.id} className="item-visita">
                <strong>[{visita.fecha}]</strong> Lote: {visita.lote_codigo} — Estado: <em>{visita.estado}</em>
                <br />
                <span>Diagnóstico: {visita.diagnostico}</span>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

// Componente Principal
function App() {
  const tituloModulo = "Módulo de Sanidad y Control Veterinario";
  const totalLotes = perfilesSanitariosData.length;

  return (
    <div className="contenedor-principal">
      <header className="encabezado-app">
        <h1>AviControl ERP — {tituloModulo}</h1>
        <p>Lotes monitoreados en tiempo real: <strong>{totalLotes}</strong></p>
      </header>

      {/* Ejercicio 10 */}
      <ListaVeterinarios veterinarios={veterinariosData} />

      {/* Ejercicio 11 */}
      <ListaPerfilesSanitarios perfiles={perfilesSanitariosData} />

      {/* Ejercicio 12 */}
      <ReporteVisitasAnidadas historial={historialVisitasData} />
    </div>
  )
}

export default App