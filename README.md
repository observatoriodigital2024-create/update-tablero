# Tablero interactivo de proyectos OMD 2026–2027

Proyecto de Observable Framework construido a partir de `Libro de proyectos OMD 2026-27.xlsx`.

## Contenido

- Filtros por frente, estado y responsable.
- Búsqueda de proyectos, observaciones y tareas.
- Indicadores de actividad y seguimiento.
- Gráficas por estado, frente y responsable.
- Tabla interactiva descargable.
- Fichas desplegables por proyecto.

## Abrir en Visual Studio Code

1. Abre esta carpeta en Visual Studio Code.
2. Selecciona **Terminal → New Terminal**.
3. Ejecuta:

```bash
npm install
npm run dev
```

4. Abre la dirección que aparezca en la terminal.

## Actualizar los datos

Sustituye el archivo Excel y ejecuta:

```bash
python scripts/extract_data.py "data-source/Libro de proyectos OMD 2026-27.xlsx" src/data
```

También puedes editar directamente `src/data/proyectos.csv`.

## Publicar con GitHub Pages

1. Publica esta carpeta en un repositorio público de GitHub.
2. En GitHub abre **Settings → Pages**.
3. En **Build and deployment → Source**, selecciona **GitHub Actions**.
4. Cada cambio enviado a la rama `main` reconstruirá y publicará el tablero.

La dirección será similar a:

`https://TU-USUARIO.github.io/NOMBRE-DEL-REPOSITORIO/`
