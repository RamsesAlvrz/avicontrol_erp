import ProductoCard from './ProductoCard'

// Recibe los productos (ya filtrados por el padre) y la función onAgregar,
// que solo pasa de largo hasta cada ProductoCard.
function Catalogo({ productos, onAgregar }) {
  return (
    <div>
      <h2>Catálogo de productos</h2>

      {productos.length === 0 ? (
        <p className="mensaje-vacio">No hay productos que coincidan</p>
      ) : (
        <div className="grid-cards">
          {productos.map((producto) => (
            <ProductoCard
              key={producto.id}
              producto={producto}
              onAgregar={onAgregar}
            />
          ))}
        </div>
      )}
    </div>
  )
}

export default Catalogo
