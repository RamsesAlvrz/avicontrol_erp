// Un renglón (detalle) de una orden de venta.
function DetalleItem({ cantidad, precioUnitario, subtotal }) {
  return (
    <li className="item-visita">
      {cantidad} unidades × S/ {Number(precioUnitario).toFixed(2)} = <strong>S/ {Number(subtotal).toFixed(2)}</strong>
    </li>
  )
}

export default DetalleItem
