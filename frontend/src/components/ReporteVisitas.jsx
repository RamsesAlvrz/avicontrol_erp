import VisitaItem from './VisitaItem'

// Relación N:M con modelo intermedio: cada veterinario contiene sus visitas.
function ReporteVisitas({ historial }) {
  return (
    <div>
      {historial.map((item) => (
        <div key={item.id} className="card-anidada">
          <h3>Especialista: {item.veterinario}</h3>
          <p>Total de atenciones: <strong>{item.visitas.length}</strong></p>
          <ul>
            {item.visitas.map((visita) => (
              <VisitaItem
                key={visita.id}
                fecha={visita.fecha}
                lote={visita.lote_codigo}
                estado={visita.estado}
                diagnostico={visita.diagnostico}
              />
            ))}
          </ul>
        </div>
      ))}
    </div>
  )
}

export default ReporteVisitas
