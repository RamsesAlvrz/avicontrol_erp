// Una visita veterinaria (fila del modelo intermedio VisitaVeterinaria).
function VisitaItem({ fecha, lote, estado, diagnostico }) {
  return (
    <li className="item-visita">
      <strong>[{fecha}]</strong> Lote: {lote} — Estado: <em>{estado}</em>
      <br />
      <span>Diagnóstico: {diagnostico}</span>
    </li>
  )
}

export default VisitaItem
