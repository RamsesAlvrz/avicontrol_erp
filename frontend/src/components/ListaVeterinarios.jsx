import { useState } from 'react'
import VeterinarioCard from './VeterinarioCard'

const FORMULARIO_VACIO = { nombre_completo: '', colegiatura: '', especialidad: '', telefono: '' }

function ListaVeterinarios({ veterinariosIniciales }) {
  const [veterinarios, setVeterinarios] = useState(veterinariosIniciales)
  const [busqueda, setBusqueda] = useState('')
  const [formulario, setFormulario] = useState(FORMULARIO_VACIO)
  const [error, setError] = useState('')

  const filtrados = veterinarios.filter((vet) =>
    vet.nombre_completo.toLowerCase().includes(busqueda.toLowerCase())
  )

  const manejarCambio = (e) => {
    setFormulario({ ...formulario, [e.target.name]: e.target.value })
  }

  const manejarEnvio = (e) => {
    e.preventDefault()

    // Regla tomada de VeterinarioSerializer.validate_colegiatura (Semana 8)
    if (formulario.colegiatura.trim().length < 5) {
      setError('La colegiatura debe tener al menos 5 caracteres.')
      return
    }
    if (formulario.nombre_completo.trim() === '' || formulario.especialidad.trim() === '') {
      setError('El nombre y la especialidad son obligatorios.')
      return
    }

    const nuevo = {
      id: Math.max(0, ...veterinarios.map((v) => v.id)) + 1,
      nombre_completo: formulario.nombre_completo.trim(),
      colegiatura: formulario.colegiatura.trim(),
      especialidad: formulario.especialidad.trim(),
      telefono: formulario.telefono.trim() || undefined, // usa el valor por defecto de la tarjeta
    }

    setVeterinarios([...veterinarios, nuevo])
    setFormulario(FORMULARIO_VACIO)
    setError('')
  }

  return (
    <div>
      <input
        className="buscador"
        type="text"
        placeholder="Buscar veterinario por nombre..."
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
      />

      {filtrados.length === 0 ? (
        <p className="mensaje-vacio">Ningún veterinario coincide con la búsqueda.</p>
      ) : (
        <div className="grid-cards">
          {filtrados.map((vet) => (
            <VeterinarioCard
              key={vet.id}
              nombre={vet.nombre_completo}
              colegiatura={vet.colegiatura}
              especialidad={vet.especialidad}
              telefono={vet.telefono}
            />
          ))}
        </div>
      )}

      <form className="formulario" onSubmit={manejarEnvio}>
        <h3>Registrar veterinario</h3>
        <input name="nombre_completo" placeholder="Nombre completo" value={formulario.nombre_completo} onChange={manejarCambio} />
        <input name="colegiatura" placeholder="Colegiatura (mín. 5 caracteres)" value={formulario.colegiatura} onChange={manejarCambio} />
        <input name="especialidad" placeholder="Especialidad" value={formulario.especialidad} onChange={manejarCambio} />
        <input name="telefono" placeholder="Teléfono (opcional)" value={formulario.telefono} onChange={manejarCambio} />
        <button type="submit">Registrar</button>
        {error && <p className="error-form">{error}</p>}
      </form>
    </div>
  )
}

export default ListaVeterinarios
