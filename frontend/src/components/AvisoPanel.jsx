import { useEffect } from 'react'

// Aviso temporal del panel: se oculta a los 3 segundos y limpia su temporizador.
function AvisoPanel({ mensaje, onCerrar }) {
  useEffect(() => {
    const temporizador = setTimeout(onCerrar, 3000)
    return () => clearTimeout(temporizador)
  }, [mensaje, onCerrar])

  return (
    <div className="aviso" role="status">
      {mensaje}
      <button type="button" className="aviso-cerrar" onClick={onCerrar} aria-label="Cerrar aviso">×</button>
    </div>
  )
}

export default AvisoPanel
