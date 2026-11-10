import { useState } from 'react'
import './App.css'
import Practica from './practica/Practica'
import PanelLotes from './components/PanelLotes'
import Tarjeta from './components/Tarjeta'
import ListaEquipos from './components/ListaEquipos'
import ListaOrdenes from './components/ListaOrdenes'
import ListaVeterinarios from './components/ListaVeterinarios'
import ListaPerfiles from './components/ListaPerfiles'
import ReporteVisitas from './components/ReporteVisitas'
import {
  equipamientosData,
  ordenesData,
  veterinariosData,
  perfilesSanitariosData,
  historialVisitasData,
} from './datos'

// Contenido del Laboratorio 10 (se conserva sin cambios)
function Laboratorio10() {
  return (
    <div className="contenedor-principal">
      <header className="encabezado-app">
        <h1>AviControl ERP</h1>
        <p>Laboratorio 10 — Componentes, estado y eventos con React</p>
      </header>

      <h2 className="titulo-parte">Parte 1 — Módulo compartido</h2>
      <Tarjeta titulo="Equipamiento de galpones">
        <ListaEquipos equiposIniciales={equipamientosData} />
      </Tarjeta>
      <Tarjeta titulo="Órdenes de venta y sus detalles (1:N)">
        <ListaOrdenes ordenes={ordenesData} />
      </Tarjeta>

      <h2 className="titulo-parte">Parte 2 — Sanidad y control veterinario</h2>
      <Tarjeta titulo="Directorio de veterinarios">
        <ListaVeterinarios veterinariosIniciales={veterinariosData} />
      </Tarjeta>
      <Tarjeta titulo="Perfiles sanitarios de lotes (1:1)">
        <ListaPerfiles perfiles={perfilesSanitariosData} />
      </Tarjeta>
      <Tarjeta titulo="Historial de visitas (N:M con modelo intermedio)">
        <ReporteVisitas historial={historialVisitasData} />
      </Tarjeta>
    </div>
  )
}

const VISTAS = {
  panel: 'Panel de Lotes (Lab 11 — Parte 2)',
  practica: 'Práctica Cafetería (Lab 11 — Parte 1)',
  lab10: 'Laboratorio 10',
}

function App() {
  const [vista, setVista] = useState('panel')

  return (
    <>
      <nav className="navegacion">
        {Object.entries(VISTAS).map(([clave, etiqueta]) => (
          <button
            key={clave}
            type="button"
            className={vista === clave ? 'activo' : ''}
            onClick={() => setVista(clave)}
          >
            {etiqueta}
          </button>
        ))}
      </nav>

      {vista === 'panel' && <PanelLotes />}
      {vista === 'practica' && <Practica />}
      {vista === 'lab10' && <Laboratorio10 />}
    </>
  )
}

export default App
