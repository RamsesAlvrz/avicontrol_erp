import { useEffect, useState } from 'react'
import api from '../api'

const formularioInicial = {
  codigo: '',
  nombre: '',
  tipo: 'SENSOR',
  estado: 'OPERATIVO',
}

function mostrarErrores(datos) {
  if (!datos || typeof datos !== 'object') return 'No se pudo guardar el equipamiento.'
  return Object.entries(datos)
    .map(([campo, mensajes]) => `${campo}: ${Array.isArray(mensajes) ? mensajes.join(', ') : mensajes}`)
    .join(' | ')
}

// Laboratorio 12: ejercicios 4, 5 y 6 (GET, estados y POST).
function ListaPractica() {
  const [equipos, setEquipos] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')
  const [formulario, setFormulario] = useState(formularioInicial)
  const [errorFormulario, setErrorFormulario] = useState('')
  const [mensaje, setMensaje] = useState('')
  const [guardando, setGuardando] = useState(false)

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

  function cambiarCampo(evento) {
    const { name, value } = evento.target
    setFormulario((actual) => ({ ...actual, [name]: value }))
  }

  async function registrarEquipo(evento) {
    evento.preventDefault()
    setErrorFormulario('')
    setMensaje('')
    setGuardando(true)

    try {
      const respuesta = await api.post('/equipamientos/', formulario)
      setEquipos((actuales) => [...actuales, respuesta.data])
      setFormulario(formularioInicial)
      setMensaje(`Equipamiento ${respuesta.data.codigo} registrado correctamente.`)
    } catch (err) {
      if (err.response?.status === 400) {
        setErrorFormulario(mostrarErrores(err.response.data))
      } else {
        setErrorFormulario('No se pudo registrar el equipamiento. Revisa la conexión con Django.')
      }
    } finally {
      setGuardando(false)
    }
  }

  return (
    <div className="contenedor-principal">
      <header className="encabezado-app">
        <h1>Laboratorio 12 — Equipamientos</h1>
        <p>Consulta GET y registro POST mediante Axios y Django REST Framework.</p>
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

      <form className="formulario" onSubmit={registrarEquipo}>
        <h2>Registrar equipamiento (POST)</h2>
        <label htmlFor="equipo-codigo">Código</label>
        <input id="equipo-codigo" name="codigo" value={formulario.codigo} onChange={cambiarCampo} placeholder="Ej. C-004" required />
        <label htmlFor="equipo-nombre">Nombre</label>
        <input id="equipo-nombre" name="nombre" value={formulario.nombre} onChange={cambiarCampo} placeholder="Ej. Comedero nuevo" required />
        <label htmlFor="equipo-tipo">Tipo</label>
        <select id="equipo-tipo" name="tipo" value={formulario.tipo} onChange={cambiarCampo}>
          <option value="SENSOR">Sensor de Temperatura/Humedad</option>
          <option value="COMEDERO">Comedero Automático</option>
          <option value="EXTRACTOR">Extractor de Aire</option>
        </select>
        <label htmlFor="equipo-estado">Estado</label>
        <select id="equipo-estado" name="estado" value={formulario.estado} onChange={cambiarCampo}>
          <option value="OPERATIVO">Operativo</option>
          <option value="MANTENIMIENTO">En mantenimiento</option>
        </select>
        <button type="submit" disabled={guardando}>{guardando ? 'Guardando...' : 'Registrar equipamiento'}</button>
        {mensaje && <p className="aviso" role="status">{mensaje}</p>}
        {errorFormulario && <p className="error-form" role="alert">{errorFormulario}</p>}
      </form>
    </div>
  )
}

export default ListaPractica
