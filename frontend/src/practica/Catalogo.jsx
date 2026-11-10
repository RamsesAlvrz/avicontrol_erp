
import ProductoCard from './ProductoCard'

function Catalogo({ productos }) {
  return (
    <div>
      <h2>Catálogo de productos</h2>

      <div className="grid-cards">
        {productos.map((producto) => (
          <ProductoCard
            key={producto.id}
            producto={producto}
          />
        ))}
      </div>
    </div>
  )
}

export default Catalogo
