import { useCallback, useEffect, useState } from 'react'
import api from '../api'
import BuscadorLotes from './BuscadorLotes'
import ListaLotes from './ListaLotes'
import ResumenLotes from './ResumenLotes'
import LoteForm from './LoteForm'
import AvisoPanel from './AvisoPanel'

// ==========================================================
// PADRE de la pantalla "Gestión de Lotes" del panel administrativo.
// Es el ÚNICO dueño del estado de la entidad (lotes) y del filtro.
// Baja datos por props y recibe avisos de los hijos por funciones.
// ==========================================================
function PanelLotes() {
  const [lotes, setLotes] = useState([])
  const [busqueda, setBusqueda] = useState('')
  const [revision, setRevision] = useState(0)
  const [filtroEstado, setFiltroEstado] = useState('TODOS')
  const [aviso, setAviso] = useState(null)
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')
  const [loteEditar, setLoteEditar] = useState(null)
  const [guardando, setGuardando] = useState(false)
  const [errorFormulario, setErrorFormulario] = useState('')

  const mostrarAviso = (texto) => setAviso({ texto, momento: Date.now() })
  const cerrarAviso = useCallback(() => setAviso(null), [])

  // Ejercicio 13: búsqueda y filtro combinados desde Django mediante query params.
  useEffect(() => {
    let activo = true
    async function cargarLotes() {
      try {
        const params = {}
        if (busqueda.trim()) params.search = busqueda.trim()
        if (filtroEstado !== 'TODOS') params.estado = filtroEstado
        const respuesta = await api.get('/lotes/', { params })
        if (activo) setLotes(respuesta.data)
      } catch (err) {
        console.error('No se pudieron consultar los lotes:', err)
        if (activo) setError('No se pudo cargar la lista de lotes.')
      } finally {
        if (activo) setCargando(false)
      }
    }
    cargarLotes()
    return () => { activo = false }
  }, [busqueda, filtroEstado, revision])

  // ---------- Avisos que suben desde los hijos ----------

  // Ejercicio 12: confirmar y eliminar realmente en Django (DELETE 204).
  const eliminarLote = async (id) => {
    const lote = lotes.find((l) => l.id === id)
    if (!lote || !window.confirm(`¿Deseas eliminar el lote ${lote.codigo_lote}?`)) return

    try {
      await api.delete(`/lotes/${id}/`)
      setLotes((actuales) => actuales.filter((l) => l.id !== id))
      if (loteEditar?.id === id) setLoteEditar(null)
      mostrarAviso(`Lote ${lote.codigo_lote} eliminado correctamente`)
      setRevision((valor) => valor + 1)
    } catch (err) {
      if (err.response?.status === 404) {
        setErrorFormulario('El lote ya no existe en Django (404). Actualiza la página para sincronizar la lista.')
      } else {
        setErrorFormulario('No se pudo eliminar el lote. Revisa la conexión con Django.')
      }
    }
  }

  // LoteFila -> onCambiarEstado(id): map() devuelve un arreglo nuevo
  const cambiarEstadoLote = (id) => {
    const lote = lotes.find((l) => l.id === id)
    const nuevoEstado = lote.estado === 'CRECIMIENTO' ? 'FINALIZADO' : 'CRECIMIENTO'
    setLotes(
      lotes.map((l) => (l.id === id ? { ...l, estado: nuevoEstado } : l))
    )
    mostrarAviso(`Lote ${lote.codigo_lote} ahora está ${nuevoEstado}`)
  }

  // El formulario avisa al padre, que realiza POST o PATCH en Django.
  const guardarLote = async (datos) => {
    setGuardando(true)
    setErrorFormulario('')
    try {
      if (loteEditar) {
        const respuesta = await api.patch(`/lotes/${loteEditar.id}/`, datos)
        setLotes((actuales) => actuales.map((l) => l.id === loteEditar.id ? respuesta.data : l))
        mostrarAviso(`Lote ${respuesta.data.codigo_lote} actualizado`)
      } else {
        const respuesta = await api.post('/lotes/', datos)
        setLotes((actuales) => [...actuales, respuesta.data])
        mostrarAviso(`Lote ${respuesta.data.codigo_lote} registrado`)
      }
      setLoteEditar(null)
      setRevision((valor) => valor + 1)
    } catch (err) {
      const detalle = err.response?.data
      if (detalle && typeof detalle === 'object') {
        setErrorFormulario(Object.entries(detalle).map(([campo, mensajes]) =>
          `${campo}: ${Array.isArray(mensajes) ? mensajes.join(', ') : mensajes}`
        ).join(' | '))
      } else {
        setErrorFormulario('No se pudo guardar el lote. Revisa que Django esté funcionando.')
      }
    } finally {
      setGuardando(false)
    }
  }

  // La API ya entrega los lotes filtrados; React solo los muestra.
  const lotesFiltrados = lotes

  // ---------- useEffect: título de la pestaña ----------
  useEffect(() => {
    document.title = `Lotes (${lotes.length}) — AviControl ERP`
  }, [lotes.length])

  return (
    <div className="contenedor-principal">
      <header className="encabezado-app">
        <h1>AviControl ERP — Panel administrativo</h1>
        <p>Laboratorio 12 — Lotes reales desde Django (React + Axios)</p>
      </header>

      {aviso && (
        <AvisoPanel key={aviso.momento} mensaje={aviso.texto} onCerrar={cerrarAviso} />
      )}

      {cargando && <p role="status">Cargando lotes...</p>}
      {error && <p className="error-form" role="alert">{error}</p>}
      {!cargando && !error && <ResumenLotes lotes={lotes} />}

      {!cargando && !error && <BuscadorLotes
        valor={busqueda}
        onCambiar={setBusqueda}
        estado={filtroEstado}
        onCambiarEstado={setFiltroEstado}
      />}

      {!cargando && !error && <ListaLotes
        lotes={lotesFiltrados}
        onEliminar={eliminarLote}
        onCambiarEstado={cambiarEstadoLote}
        onEditar={(lote) => { setLoteEditar(lote); setErrorFormulario('') }}
      />}

      {!cargando && !error && <LoteForm
        key={loteEditar?.id ?? 'nuevo'}
        codigosExistentes={lotes.map((l) => l.codigo_lote)}
        onGuardar={guardarLote}
        loteEditar={loteEditar}
        onCancelar={() => { setLoteEditar(null); setErrorFormulario('') }}
        guardando={guardando}
        errorServidor={errorFormulario}
      />}
    </div>
  )
}

export default PanelLotes
