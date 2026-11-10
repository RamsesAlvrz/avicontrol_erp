
import { productos } from './datos'
import Catalogo from './Catalogo'

function Practica() {
  return (
    <div className="contenedor-principal">
      <h1>Laboratorio 11 - Parte 1</h1>
      <p>Comunicación entre componentes con props</p>

      <Catalogo productos={productos} />
    </div>
  )
}

export default Practica
