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
  const [filtroEstado, setFiltroEstado] = useState('TODOS')
  const [aviso, setAviso] = useState(null)
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')

  const mostrarAviso = (texto) => setAviso({ texto, momento: Date.now() })
  const cerrarAviso = useCallback(() => setAviso(null), [])

  // Ejercicio 10: los lotes se consultan desde Django, no desde datos.js.
  useEffect(() => {
    let activo = true
    async function cargarLotes() {
      try {
        const respuesta = await api.get('/lotes/')
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
  }, [])

  // ---------- Avisos que suben desde los hijos ----------

  // LoteFila -> onEliminar(id): filter() devuelve un arreglo nuevo
  const eliminarLote = (id) => {
    const lote = lotes.find((l) => l.id === id)
    setLotes(lotes.filter((l) => l.id !== id))
    mostrarAviso(`Lote ${lote.codigo_lote} eliminado`)
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

  // LoteForm -> onGuardar(datos): spread para agregar sin push
  const guardarLote = (datos) => {
    const nuevo = {
      id: Math.max(0, ...lotes.map((l) => l.id)) + 1,
      ...datos,
    }
    setLotes([...lotes, nuevo])
    mostrarAviso(`Lote ${nuevo.codigo_lote} registrado`)
  }

  // ---------- Datos derivados (no son estado) ----------
  const texto = busqueda.trim().toLowerCase()
  const lotesFiltrados = lotes.filter((l) => {
    const coincideTexto =
      l.codigo_lote.toLowerCase().includes(texto) ||
      l.raza.toLowerCase().includes(texto)
    const coincideEstado = filtroEstado === 'TODOS' || l.estado === filtroEstado
    return coincideTexto && coincideEstado
  })

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
      />}

      {!cargando && !error && <LoteForm
        codigosExistentes={lotes.map((l) => l.codigo_lote)}
        onGuardar={guardarLote}
      />}
    </div>
  )
}

export default PanelLotes
