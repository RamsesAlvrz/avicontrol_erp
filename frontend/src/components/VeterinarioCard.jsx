import { useState } from 'react'

// Un veterinario. "telefono" tiene valor por defecto por si llega vacío.
function VeterinarioCard({ nombre, colegiatura, especialidad, telefono = 'Sin teléfono' }) {
  const [favorito, setFavorito] = useState(false)

  return (
    <div className="card-item" style={{ borderTop: favorito ? '5px solid #f9a825' : '5px solid transparent' }}>
      <h3>{nombre}{favorito && ' ★'}</h3>
      <p><strong>Colegiatura:</strong> {colegiatura}</p>
      <p><strong>Especialidad:</strong> {especialidad}</p>
      <p><strong>Teléfono:</strong> {telefono}</p>
      <button type="button" onClick={() => setFavorito(!favorito)}>
        {favorito ? 'Quitar de favoritos' : 'Marcar favorito'}
      </button>
    </div>
  )
}

export default VeterinarioCard
