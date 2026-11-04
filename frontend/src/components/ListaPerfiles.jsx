import PerfilSanitarioCard from './PerfilSanitarioCard'

function ListaPerfiles({ perfiles }) {
  if (perfiles.length === 0) {
    return <p className="mensaje-vacio">No existen perfiles sanitarios evaluados.</p>
  }

  return (
    <div className="grid-cards">
      {perfiles.map((perfil) => (
        <PerfilSanitarioCard
          key={perfil.id}
          lote={perfil.lote_codigo}
          peso={perfil.peso_promedio_gr}
          mortalidad={perfil.indice_mortalidad}
          certificado={perfil.certificado_sanitario}
        />
      ))}
    </div>
  )
}

export default ListaPerfiles
