import OrdenCard from './OrdenCard'

function ListaOrdenes({ ordenes }) {
  if (ordenes.length === 0) {
    return <p className="mensaje-vacio">No hay órdenes de venta.</p>
  }

  return (
    <div>
      {ordenes.map((orden) => (
        <OrdenCard
          key={orden.id}
          numero={orden.numero_comprobante}
          fecha={orden.fecha_emision}
          cliente={orden.cliente.razon_social}
          estado={orden.estado_entrega}
          detalles={orden.detalles}
        />
      ))}
    </div>
  )
}

export default ListaOrdenes
