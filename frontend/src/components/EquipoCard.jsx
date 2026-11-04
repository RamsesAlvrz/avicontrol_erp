import { useState } from 'react'

// Muestra UN registro de Equipamiento. Los datos llegan por props desestructuradas.
// "estado" tiene un valor por defecto.
function EquipoCard({ codigo, nombre, tipo, estado = 'OPERATIVO' }) {
  // Cada tarjeta tiene su PROPIO contador (estado local).
  const [revisiones, setRevisiones] = useState(0)
  const enMantenimiento = estado === 'MANTENIMIENTO'

  return (
    <div className="card-item">
      <h3>{nombre}</h3>
      <p><strong>Código:</strong> {codigo}</p>
      <p><strong>Tipo:</strong> {tipo}</p>
      <p>
        <strong>Estado:</strong>{' '}
        <span className={enMantenimiento ? 'badge-warn' : 'badge-ok'}>{estado}</span>
      </p>

      {/* Solo se muestra cuando el contador es mayor que cero */}
      {revisiones > 0 && <p>Revisiones registradas: <strong>{revisiones}</strong></p>}

      <button
        type="button"
        onClick={() => setRevisiones(revisiones + 1)}
        disabled={enMantenimiento}
      >
        Registrar revisión
      </button>
      {enMantenimiento && <p className="nota">Equipo en mantenimiento: no se puede revisar.</p>}
    </div>
  )
}

export default EquipoCard
