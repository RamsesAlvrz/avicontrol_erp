// Hermano del listado: todo lo que muestra se DERIVA de la prop "lotes" (sin useState).
function ResumenLotes({ lotes }) {
  const totalLotes = lotes.length
  const totalAves = lotes.reduce((suma, l) => suma + l.cantidad_inicial, 0)
  const enCrecimiento = lotes.filter((l) => l.estado === 'CRECIMIENTO').length
  const finalizados = totalLotes - enCrecimiento
  const promedioAves = totalLotes === 0 ? 0 : totalAves / totalLotes

  return (
    <section className="resumen-panel">
      <div className="resumen-item">
        <span className="resumen-valor">{totalLotes}</span>
        <span>Lotes registrados</span>
      </div>
      <div className="resumen-item">
        <span className="resumen-valor">{totalAves.toLocaleString('es-PE')}</span>
        <span>Aves en total</span>
      </div>
      <div className="resumen-item">
        <span className="resumen-valor">{enCrecimiento} / {finalizados}</span>
        <span>En crecimiento / Finalizados</span>
      </div>
      <div className="resumen-item">
        <span className="resumen-valor">{promedioAves.toFixed(2)}</span>
        <span>Promedio de aves por lote</span>
      </div>
    </section>
  )
}

export default ResumenLotes
