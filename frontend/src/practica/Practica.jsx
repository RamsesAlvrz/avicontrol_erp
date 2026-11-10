import { useCallback, useState } from 'react'
import { productos } from './datos'
import Buscador from './Buscador'
import Catalogo from './Catalogo'
import Carrito from './Carrito'
import Aviso from './Aviso'

// Componente PADRE: guarda el estado que comparten los hijos hermanos
// (Buscador, Catalogo, Carrito y Aviso) y les entrega datos y funciones por props.
function Practica() {
  // Ejercicio 4: estado elevado. Cada línea: { id, nombre, precio, cantidad }
  const [carrito, setCarrito] = useState([])
  // Ejercicio 7: texto del buscador, compartido por Buscador y Catalogo
  const [busqueda, setBusqueda] = useState('')
  // Ejercicio 8: último producto agregado (lo muestra Aviso)
  const [ultimoAgregado, setUltimoAgregado] = useState(null)

  // Ejercicio 3 y 4: el hijo (ProductoCard) avisa con onAgregar(producto)
  const agregarAlCarrito = (producto) => {
    console.log('Agregar al carrito:', producto.nombre)

    const existe = carrito.some((linea) => linea.id === producto.id)

    if (existe) {
      // Ya está: se crea un arreglo NUEVO aumentando la cantidad con map()
      setCarrito(
        carrito.map((linea) =>
          linea.id === producto.id
            ? { ...linea, cantidad: linea.cantidad + 1 }
            : linea
        )
      )
    } else {
      // No está: arreglo NUEVO con spread (sin push)
      setCarrito([
        ...carrito,
        { id: producto.id, nombre: producto.nombre, precio: producto.precio, cantidad: 1 },
      ])
    }

    // Objeto nuevo en cada clic para que Aviso reinicie su temporizador
    setUltimoAgregado({ nombre: producto.nombre, momento: Date.now() })
  }

  // Ejercicio 6: quitar una línea (filter devuelve un arreglo nuevo)
  const quitarDelCarrito = (id) => {
    setCarrito(carrito.filter((linea) => linea.id !== id))
  }

  // Ejercicio 6: vaciar el carrito (arreglo vacío nuevo)
  const vaciarCarrito = () => {
    setCarrito([])
  }

  // useCallback: la función conserva su identidad entre renders, así el efecto
  // de Aviso (que depende de onCerrar) no se reinicia al escribir en el buscador.
  const cerrarAviso = useCallback(() => setUltimoAgregado(null), [])

  // Ejercicio 7: dato derivado, se calcula en cada render (no es estado)
  const productosFiltrados = productos.filter((producto) =>
    producto.nombre.toLowerCase().includes(busqueda.toLowerCase())
  )

  return (
    <div className="contenedor-principal">
      <h1>Laboratorio 11 - Parte 1</h1>
      <p>Comunicación entre componentes: mini catálogo con carrito</p>

      {ultimoAgregado && (
        <Aviso
          key={ultimoAgregado.momento}
          mensaje={`Agregado: ${ultimoAgregado.nombre}`}
          onCerrar={cerrarAviso}
        />
      )}

      <Buscador valor={busqueda} onCambiar={setBusqueda} />

      <div className="practica-layout">
        <Catalogo productos={productosFiltrados} onAgregar={agregarAlCarrito} />
        <Carrito
          lineas={carrito}
          onQuitar={quitarDelCarrito}
          onVaciar={vaciarCarrito}
        />
      </div>
    </div>
  )
}

export default Practica
