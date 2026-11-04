import DetalleItem from './DetalleItem'

// Relación 1:N: una orden contiene varios detalles (componente dentro de componente).
// Los nombres de la API (numero_comprobante, ...) ya llegan convertidos a props.
function OrdenCard({ numero, fecha, cliente, estado, detalles }) {
  // Total calculado con JavaScript a partir de los detalles
  const total = detalles.reduce((acumulado, d) => acumulado + Number(d.subtotal), 0)

  return (
    <div className="card-anidada">
      <h3>Orden {numero}</h3>
      <p>Cliente: {cliente} | Fecha: {fecha} | Estado: <em>{estado}</em></p>
      <ul>
        {detalles.map((d) => (
          <DetalleItem
            key={d.id}
            cantidad={d.cantidad}
            precioUnitario={d.precio_unitario}
            subtotal={d.subtotal}
          />
        ))}
      </ul>
      <p>Total calculado: <strong>S/ {total.toFixed(2)}</strong></p>
    </div>
  )
}

export default OrdenCard
