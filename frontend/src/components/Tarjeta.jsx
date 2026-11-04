// Componente contenedor: recibe un título y "children" (lo que va entre sus etiquetas).
function Tarjeta({ titulo, children }) {
  return (
    <section className="tarjeta">
      <h2 className="tarjeta-titulo">{titulo}</h2>
      <div className="tarjeta-cuerpo">{children}</div>
    </section>
  )
}

export default Tarjeta
