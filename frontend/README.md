# AviControl ERP — Frontend (React + Vite)

Laboratorio 10 (Semana 10): componentes, props, estado (`useState`) y eventos.

## Cómo ejecutarlo
```bash
cd frontend
npm install
npm run dev     # http://localhost:5173/
npm run lint
npm run build
```

## Componentes (`src/components`)
| Componente | Qué hace |
| --- | --- |
| `Tarjeta` | Contenedor reutilizable: recibe `titulo` y `children`. |
| `EquipoCard` | Muestra un equipo; botón "Registrar revisión" con contador (`useState`), deshabilitado si está en mantenimiento. |
| `ListaEquipos` | Guarda la lista en el estado; buscador controlado y formulario controlado con validación (código ≥ 3 caracteres). |
| `OrdenCard` / `DetalleItem` | Relación 1:N: la orden muestra cada detalle con `DetalleItem` y calcula el total. |
| `ListaOrdenes` | Recorre las órdenes con `map()` y `key`. |
| `VeterinarioCard` | Muestra un veterinario; botón con estado "Marcar favorito". |
| `ListaVeterinarios` | Buscador controlado y formulario con validación (colegiatura ≥ 5 caracteres). |
| `PerfilSanitarioCard` / `ListaPerfiles` | Relación 1:1 con renderizado condicional (alerta si mortalidad > 5 %). |
| `VisitaItem` / `ReporteVisitas` | Relación N:M con modelo intermedio (visitas anidadas por veterinario). |

Los datos están escritos a mano en `src/datos.js` con la forma de la API de la Semana 8; aún no se consume la API.
