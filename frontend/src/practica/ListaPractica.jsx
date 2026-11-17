import { useEffect, useState } from 'react'
import api from '../api'

// Laboratorio 12: GET con Axios y useEffect.
function ListaPractica() {
  const [equipos, setEquipos] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    let activo = true

    async function cargarEquipos() {
      try {
        const respuesta = await api.get('/equipamientos/')
        if (activo) setEquipos(respuesta.data)
      } catch (err) {
        console.error('Error al consultar equipamientos:', err)
        if (activo) setError('No se pudo cargar la lista')
      } finally {
        if (activo) setCargando(false)
      }
    }

    cargarEquipos()
    return () => { activo = false }
  }, [])

  return (
    <div className="contenedor-principal">
      <header className="encabezado-app">
        <h1>Laboratorio 12 — Equipamientos</h1>
        <p>Consulta GET a Django REST Framework mediante Axios.</p>
      </header>
      {cargando ? (
        <p>Cargando...</p>
      ) : error ? (
        <p className="error-form" role="alert">{error}</p>
      ) : equipos.length === 0 ? (
        <p className="mensaje-vacio">No hay equipamientos registrados.</p>
      ) : (
        <table className="tabla-panel">
          <thead><tr><th>ID</th><th>Código</th><th>Nombre</th><th>Tipo</th><th>Estado</th></tr></thead>
          <tbody>
            {equipos.map((equipo) => (
              <tr key={equipo.id}>
                <td>{equipo.id}</td>
                <td>{equipo.codigo}</td>
                <td>{equipo.nombre}</td>
                <td>{equipo.tipo}</td>
                <td>{equipo.estado}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}

export default ListaPractica
