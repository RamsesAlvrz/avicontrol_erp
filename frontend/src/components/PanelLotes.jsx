import { useCallback, useEffect, useState } from 'react'
import { lotesData } from '../datos'
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
  const [lotes, setLotes] = useState(lotesData)
  const [busqueda, setBusqueda] = useState('')
  const [filtroEstado, setFiltroEstado] = useState('TODOS')
  const [aviso, setAviso] = useState(null)

  const mostrarAviso = (texto) => setAviso({ texto, momento: Date.now() })
  const cerrarAviso = useCallback(() => setAviso(null), [])

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
        <p>Laboratorio 11 — Gestión de lotes de aves (comunicación entre componentes)</p>
      </header>

      {aviso && (
        <AvisoPanel key={aviso.momento} mensaje={aviso.texto} onCerrar={cerrarAviso} />
      )}

      <ResumenLotes lotes={lotes} />

      <BuscadorLotes
        valor={busqueda}
        onCambiar={setBusqueda}
        estado={filtroEstado}
        onCambiarEstado={setFiltroEstado}
      />

      <ListaLotes
        lotes={lotesFiltrados}
        onEliminar={eliminarLote}
        onCambiarEstado={cambiarEstadoLote}
      />

      <LoteForm
        codigosExistentes={lotes.map((l) => l.codigo_lote)}
        onGuardar={guardarLote}
      />
    </div>
  )
}

export default PanelLotes
