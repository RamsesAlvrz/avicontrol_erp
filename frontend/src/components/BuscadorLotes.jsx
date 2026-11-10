import { ESTADOS_LOTE } from '../datos'

// Filtro controlado: los valores viven en PanelLotes; aquí solo se avisan los cambios.
function BuscadorLotes({ valor, onCambiar, estado, onCambiarEstado }) {
  return (
    <div className="filtros-panel">
      <input
        className="buscador"
        type="text"
        placeholder="Buscar por código de lote o raza..."
        value={valor}
        onChange={(e) => onCambiar(e.target.value)}
      />
      <select value={estado} onChange={(e) => onCambiarEstado(e.target.value)}>
        <option value="TODOS">Todos los estados</option>
        {Object.entries(ESTADOS_LOTE).map(([clave, etiqueta]) => (
          <option key={clave} value={clave}>{etiqueta}</option>
        ))}
      </select>
    </div>
  )
}

export default BuscadorLotes
