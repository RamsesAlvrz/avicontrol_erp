import { useState } from 'react'

const FORMULARIO_VACIO = {
  codigo_lote: '',
  galpon: '',
  raza: '',
  cantidad_inicial: '',
  fecha_ingreso: '',
}

// Formulario de alta CONTROLADO. Valida y entrega el registro al padre con onGuardar.
function LoteForm({ codigosExistentes, onGuardar }) {
  const [formulario, setFormulario] = useState(FORMULARIO_VACIO)
  const [error, setError] = useState('')

  const manejarCambio = (e) => {
    setFormulario({ ...formulario, [e.target.name]: e.target.value })
  }

  const manejarEnvio = (e) => {
    e.preventDefault()

    const codigo = formulario.codigo_lote.trim().toUpperCase()
    const cantidad = Number(formulario.cantidad_inicial)
    const galpon = Number(formulario.galpon)

    // Reglas del modelo/serializer de Lote (Semana 8)
    if (codigo === '' || formulario.raza.trim() === '' || formulario.fecha_ingreso === '') {
      setError('El código de lote, la raza y la fecha de ingreso son obligatorios.')
      return
    }
    if (codigosExistentes.includes(codigo)) {
      setError(`Ya existe un lote con el código ${codigo} (codigo_lote es único).`)
      return
    }
    if (!Number.isInteger(cantidad) || cantidad <= 0) {
      setError('La cantidad inicial de aves debe ser un número entero mayor que cero.')
      return
    }
    if (!Number.isInteger(galpon) || galpon <= 0) {
      setError('Indique un galpón válido (id mayor que cero).')
      return
    }

    onGuardar({
      galpon,
      codigo_lote: codigo,
      cantidad_inicial: cantidad,
      fecha_ingreso: formulario.fecha_ingreso,
      raza: formulario.raza.trim(),
      estado: 'CRECIMIENTO',
    })

    setFormulario(FORMULARIO_VACIO)
    setError('')
  }

  return (
    <form className="formulario" onSubmit={manejarEnvio} noValidate>
      <h3>Registrar lote</h3>
      <input name="codigo_lote" placeholder="Código de lote (ej. LOT-2026-F)" value={formulario.codigo_lote} onChange={manejarCambio} />
      <input name="galpon" type="number" placeholder="Galpón (id)" value={formulario.galpon} onChange={manejarCambio} />
      <input name="raza" placeholder="Raza" value={formulario.raza} onChange={manejarCambio} />
      <input name="cantidad_inicial" type="number" placeholder="Cantidad inicial de aves" value={formulario.cantidad_inicial} onChange={manejarCambio} />
      <input name="fecha_ingreso" type="date" value={formulario.fecha_ingreso} onChange={manejarCambio} />
      <button type="submit">Registrar lote</button>
      {error && <p className="error-form">{error}</p>}
    </form>
  )
}

export default LoteForm
