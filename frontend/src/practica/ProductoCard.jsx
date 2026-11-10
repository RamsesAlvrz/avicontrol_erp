
function ProductoCard({ producto }) {
  return (
    <div className="card-item">
      <h3>{producto.nombre}</h3>

      <p>
        Precio: S/ {Number(producto.precio).toFixed(2)}
      </p>

      <p>Stock: {producto.stock}</p>

      {producto.stock === 0 && (
        <p style={{ color: 'red', fontWeight: 'bold' }}>
          Agotado
        </p>
      )}
    </div>
  )
}

export default ProductoCard
