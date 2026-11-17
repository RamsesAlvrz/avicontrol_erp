import LoteFila from './LoteFila'

// Listado: recibe los lotes ya filtrados y reenvía las funciones a cada fila.
function ListaLotes({ lotes, onEliminar, onCambiarEstado, onEditar }) {
  if (lotes.length === 0) {
    return <p className="mensaje-vacio">No hay lotes que coincidan con la búsqueda.</p>
  }

  return (
    <table className="tabla-panel">
      <thead>
        <tr>
          <th>Código</th>
          <th>Galpón</th>
          <th>Raza</th>
          <th>Aves</th>
          <th>Ingreso</th>
          <th>Estado</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        {lotes.map((lote) => (
          <LoteFila
            key={lote.id}
            lote={lote}
            onEliminar={onEliminar}
            onCambiarEstado={onCambiarEstado}
            onEditar={onEditar}
          />
        ))}
      </tbody>
    </table>
  )
}

export default ListaLotes
