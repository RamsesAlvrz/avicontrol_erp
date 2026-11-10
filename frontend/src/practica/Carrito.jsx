import { useEffect } from 'react'

// Hermano de Catalogo: recibe las líneas del carrito por props y avisa
// al padre con onQuitar(id) y onVaciar().
function Carrito({ lineas, onQuitar, onVaciar }) {
  // Ejercicio 5: datos DERIVADOS con reduce() (sin useState)
  const total = lineas.reduce(
    (suma, linea) => suma + Number(linea.precio) * linea.cantidad,
    0
  )
  const cantidad = lineas.reduce((suma, linea) => suma + linea.cantidad, 0)

  // Ejercicio 8: se ejecuta al montar y cada vez que cambia "cantidad"
  useEffect(() => {
    console.log('Efecto del carrito, unidades:', cantidad)
    document.title = `Carrito (${cantidad}) — Cafetería`
  }, [cantidad])

  return (
    <aside className="carrito">
      <h2>Carrito</h2>

      {lineas.length === 0 && (
        <p className="mensaje-vacio">El carrito está vacío</p>
      )}

      {lineas.length > 0 && (
        <>
          <ul className="carrito-lineas">
            {lineas.map((linea) => (
              <li key={linea.id}>
                <span>
                  {linea.nombre} x {linea.cantidad} = S/{' '}
                  {(Number(linea.precio) * linea.cantidad).toFixed(2)}
                </span>
                <button type="button" onClick={() => onQuitar(linea.id)}>
                  Quitar
                </button>
              </li>
            ))}
          </ul>

          <p>Unidades: {cantidad}</p>
          <p className="carrito-total">Total: S/ {total.toFixed(2)}</p>

          <button type="button" className="boton-secundario" onClick={onVaciar}>
            Vaciar carrito
          </button>
        </>
      )}
    </aside>
  )
}

export default Carrito
