import { useState } from 'react'
import EquipoCard from './EquipoCard'

const FORMULARIO_VACIO = { codigo: '', nombre: '', tipo: 'SENSOR' }

// Recibe el arreglo inicial por props y lo guarda en el estado para poder agregar registros.
function ListaEquipos({ equiposIniciales }) {
  const [equipos, setEquipos] = useState(equiposIniciales)
  const [busqueda, setBusqueda] = useState('')
  const [formulario, setFormulario] = useState(FORMULARIO_VACIO)
  const [error, setError] = useState('')

  // Filtro sin distinguir mayúsculas/minúsculas
  const equiposFiltrados = equipos.filter((equipo) =>
    equipo.nombre.toLowerCase().includes(busqueda.toLowerCase())
  )

  const manejarCambio = (e) => {
    setFormulario({ ...formulario, [e.target.name]: e.target.value })
  }

  const manejarEnvio = (e) => {
    e.preventDefault()

    // Regla tomada de EquipamientoSerializer.validate_codigo (Semana 8)
    if (formulario.codigo.trim().length < 3) {
      setError('El código debe tener al menos 3 caracteres.')
      return
    }
    if (formulario.nombre.trim() === '') {
      setError('El nombre del equipo es obligatorio.')
      return
    }
    if (equipos.some((eq) => eq.codigo.toLowerCase() === formulario.codigo.trim().toLowerCase())) {
      setError('Ya existe un equipo con ese código.')
      return
    }

    const nuevo = {
      id: Math.max(0, ...equipos.map((eq) => eq.id)) + 1,
      codigo: formulario.codigo.trim(),
      nombre: formulario.nombre.trim(),
      tipo: formulario.tipo,
      estado: 'OPERATIVO',
    }

    setEquipos([...equipos, nuevo]) // arreglo NUEVO, sin push
    setFormulario(FORMULARIO_VACIO)
    setError('')
  }

  return (
    <div>
      <input
        className="buscador"
        type="text"
        placeholder="Buscar equipo por nombre..."
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
      />

      {equiposFiltrados.length === 0 ? (
        <p className="mensaje-vacio">Ningún equipo coincide con la búsqueda.</p>
      ) : (
        <div className="grid-cards">
          {equiposFiltrados.map((equipo) => (
            <EquipoCard
              key={equipo.id}
              codigo={equipo.codigo}
              nombre={equipo.nombre}
              tipo={equipo.tipo}
              estado={equipo.estado}
            />
          ))}
        </div>
      )}

      <form className="formulario" onSubmit={manejarEnvio}>
        <h3>Agregar equipo</h3>
        <input name="codigo" placeholder="Código (mín. 3 caracteres)" value={formulario.codigo} onChange={manejarCambio} />
        <input name="nombre" placeholder="Nombre del equipo" value={formulario.nombre} onChange={manejarCambio} />
        <select name="tipo" value={formulario.tipo} onChange={manejarCambio}>
          <option value="SENSOR">Sensor</option>
          <option value="COMEDERO">Comedero</option>
          <option value="EXTRACTOR">Extractor</option>
        </select>
        <button type="submit">Agregar</button>
        {error && <p className="error-form">{error}</p>}
      </form>
    </div>
  )
}

export default ListaEquipos
