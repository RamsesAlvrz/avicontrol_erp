import { useEffect } from 'react'

// Muestra "Agregado: <nombre>" y pide al padre que lo oculte a los 3 segundos.
function Aviso({ mensaje, onCerrar }) {
  useEffect(() => {
    console.log('Aviso montado:', mensaje)
    const temporizador = setTimeout(() => {
      onCerrar()
    }, 3000)

    // Limpieza: se ejecuta al desmontar el Aviso (o antes de repetir el efecto)
    return () => {
      console.log('Aviso desmontado, se limpia el temporizador')
      clearTimeout(temporizador)
    }
  }, [mensaje, onCerrar])

  return <div className="aviso">{mensaje}</div>
}

export default Aviso
