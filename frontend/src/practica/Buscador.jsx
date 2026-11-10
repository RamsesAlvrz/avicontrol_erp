// Campo de texto CONTROLADO: el valor vive en el padre (Practica).
// Buscador solo avisa cada cambio con onCambiar(texto).
function Buscador({ valor, onCambiar }) {
  return (
    <input
      className="buscador"
      type="text"
      placeholder="Buscar producto..."
      value={valor}
      onChange={(e) => onCambiar(e.target.value)}
    />
  )
}

export default Buscador
