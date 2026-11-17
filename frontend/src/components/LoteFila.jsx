import { ESTADOS_LOTE } from '../datos'

// Una fila del listado. No modifica la lista: solo AVISA al padre con el id.
function LoteFila({ lote, onEliminar, onCambiarEstado, onEditar }) {
  const enCrecimiento = lote.estado === 'CRECIMIENTO'

  return (
    <tr>
      <td><strong>{lote.codigo_lote}</strong></td>
      <td>{lote.galpon}</td>
      <td>{lote.raza}</td>
      <td>{lote.cantidad_inicial.toLocaleString('es-PE')}</td>
      <td>{lote.fecha_ingreso}</td>
      <td>
        <span className={enCrecimiento ? 'badge-ok' : 'badge-warn'}>
          {ESTADOS_LOTE[lote.estado]}
        </span>
      </td>
      <td className="acciones">
        <button type="button" onClick={() => onEditar(lote)}>Editar</button>
        <button type="button" onClick={() => onCambiarEstado(lote.id)}>
          {enCrecimiento ? 'Finalizar' : 'Reactivar'}
        </button>
        <button type="button" className="boton-peligro" onClick={() => onEliminar(lote.id)}>
          Eliminar
        </button>
      </td>
    </tr>
  )
}

export default LoteFila
