// Relación 1:1 (Lote ↔ PerfilSanitarioLote) con renderizado condicional.
function PerfilSanitarioCard({ lote, peso, mortalidad, certificado = false }) {
  const mortalidadNum = Number(mortalidad)

  return (
    <div
      className="card-item"
      style={{ borderTop: certificado ? '5px solid #2e7d32' : '5px solid #c62828' }}
    >
      <h3>Lote: {lote}</h3>
      <p>Peso promedio: {Number(peso).toFixed(2)} g</p>
      <p>Mortalidad: <strong>{mortalidadNum.toFixed(2)}%</strong></p>
      <p>
        Certificación SENASA:{' '}
        {certificado ? <span className="badge-ok">VIGENTE</span> : <span className="badge-warn">PENDIENTE</span>}
      </p>
      {mortalidadNum > 5 && (
        <div className="alerta-urgente">⚠ Índice de mortalidad crítico (&gt; 5%). Requiere inspección urgente.</div>
      )}
    </div>
  )
}

export default PerfilSanitarioCard
