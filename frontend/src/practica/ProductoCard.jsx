// Componente hijo: muestra un producto y AVISA al padre con onAgregar(producto).
// No modifica la prop "producto" ni guarda el carrito.
function ProductoCard({ producto, onAgregar }) {
  const agotado = producto.stock === 0

  return (
    <div className="card-item">
      <h3>{producto.nombre}</h3>

      <p>
        Precio: S/ {Number(producto.precio).toFixed(2)}
      </p>

      <p>Stock: {producto.stock}</p>

      {agotado && (
        <p style={{ color: 'red', fontWeight: 'bold' }}>
          Agotado
        </p>
      )}

      {/* Correcto: se pasa una función flecha; React la ejecuta solo al hacer clic.
          Incorrecto (Ejercicio 3): onClick={onAgregar(producto)} la ejecuta al dibujar. */}
      <button
        type="button"
        disabled={agotado}
        onClick={() => onAgregar(producto)}
      >
        Agregar
      </button>
    </div>
  )
}

export default ProductoCard
