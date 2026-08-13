---
title: Plan anual OMD 2026–2027
toc: false
---

```js
const proyectos = FileAttachment("data/proyectos.csv").csv({typed: true});
const responsables = FileAttachment("data/responsables.csv").csv({typed: true});
```

<header class="hero">
  <div>
    <span class="kicker">OBSERVATORIO DE MEDIOS DIGITALES</span>
    <h1>Plan anual OMD</h1>
    <p>Agenda de investigación, producción académica, transferencia de conocimiento, procuración de fondos y colaboración institucional.</p>
  </div>
  <div class="year">26–27</div>
</header>

<section class="annual-plan">
  <div class="plan-label">PROPÓSITO DEL CICLO</div>
  <div class="plan-content">
    <p class="plan-lead">Durante el ciclo 2026–2027, el Observatorio de Medios Digitales concentrará su trabajo en consolidar una agenda común de investigación aplicada sobre desinformación, inteligencia artificial, alfabetización mediática e informacional, plataformas digitales y análisis de conversaciones públicas de coyuntura, como las elecciones.</p>
    <p>El objetivo central será articular los proyectos actualmente en desarrollo con una estrategia compartida de producción académica, generación de recursos, procuración de fondos y colaboración institucional, de manera que cada iniciativa contribuya al posicionamiento y fortalecimiento del Observatorio.</p>
    <h2>Prioridades del periodo</h2>
    <ol class="priorities">
      <li><span>01</span><p><strong>Consolidar los proyectos estratégicos del OMD</strong>, particularmente aquellos vinculados con alfabetización mediática, inteligencia artificial en la educación, análisis de plataformas socio-digitales, desinformación y observación de coyunturas digitales, como la electoral.</p></li>
      <li><span>02</span><p><strong>Fortalecer la producción académica conjunta</strong> mediante artículos Scopus, capítulos, informes, bases de datos, metodologías y otros resultados derivados directamente de los proyectos del Observatorio.</p></li>
      <li><span>03</span><p><strong>Convertir los proyectos y datos generados por el OMD en productos de transferencia y divulgación</strong>, incluyendo informes, visualizaciones, recursos educativos, newsletter, contenidos para medios y recursos abiertos.</p></li>
      <li><span>04</span><p><strong>Identificar y presentar propuestas de financiamiento</strong> que permitan ampliar y dar continuidad a las líneas prioritarias del Observatorio, privilegiando proyectos colaborativos y alianzas estratégicas frente a postulaciones individuales.</p></li>
      <li><span>05</span><p><strong>Ampliar la colaboración</strong> con profesores, grupos de investigación y áreas del Tecnológico de Monterrey, así como con universidades, medios, organizaciones civiles, verificadores, empresas y organismos nacionales e internacionales.</p></li>
      <li><span>06</span><p><strong>Integrar estudiantes y colaboradores en proyectos de investigación</strong> que permitan fortalecer capacidades en análisis de datos, investigación digital, inteligencia artificial y alfabetización mediática.</p></li>
      <li class="priority-goals"><span>07</span><p><strong>Consolidar metodologías, herramientas y recursos propios del OMD</strong> que puedan reutilizarse en distintos proyectos y coyunturas, fortaleciendo al Observatorio como una infraestructura permanente de investigación y análisis digital.</p></li>
    </ol>
  </div>
</section>

## Seguimiento de proyectos

<p class="section-note dashboard-intro">A partir del 1 de agosto de 2026</p>
<p class="section-note dashboard-intro">Utiliza los filtros para explorar los proyectos que hacen operativa esta agenda anual y revisar sus responsables, avances y siguientes acciones.</p>

```js
const categoriaInput = Inputs.select(
  ["Todos", ...new Set(proyectos.map(d => d.categoria))],
  {label: "Frente", value: "Todos"}
);
const categoria = Generators.input(categoriaInput);
const estadoInput = Inputs.select(
  ["Todos", ...new Set(proyectos.map(d => d.estado))],
  {label: "Estado", value: "Todos"}
);
const estado = Generators.input(estadoInput);
const responsableInput = Inputs.select(
  ["Todos", ...new Set(responsables.map(d => d.responsable))],
  {label: "Responsable", value: "Todos"}
);
const responsable = Generators.input(responsableInput);
const busquedaInput = Inputs.text({label: "Buscar", placeholder: "Proyecto, observación o pendiente…"});
const busqueda = Generators.input(busquedaInput);
```

```js
const termino = busqueda.trim().toLocaleLowerCase("es");
const filtrados = proyectos.filter(d =>
  (categoria === "Todos" || d.categoria === categoria) &&
  (estado === "Todos" || d.estado === estado) &&
  (responsable === "Todos" || d.lista_responsables.split("|").includes(responsable)) &&
  (!termino || `${d.proyecto} ${d.responsables} ${d.observaciones} ${d.por_hacer}`.toLocaleLowerCase("es").includes(termino))
);
const terminados = filtrados.filter(d => d.estado === "Terminado").length;
```

<style>
    :root{
      --ink:#142620;
      --cream:#f4f1e9;
      --lime:#c8ff48;
      --coral:#652d90; /* updated: naranja -> morado */
      --muted:#68756f;
      --line:#d7dcd8;
      --headline:#1b75bb; /* titulares azules */
    }

    body{background:var(--cream);color:var(--ink);font-size:18px}
    #observablehq-main{max-width:1440px;padding:0 34px 70px}
    .hero{display:flex;justify-content:space-between;align-items:end;padding:72px 0 48px;border-bottom:1px solid var(--ink);margin-bottom:0}
    .kicker{font-size:19.5px;font-weight:800;letter-spacing:.17em;color:var(--coral)}
    .hero h1{font-family:Georgia,serif;font-size:clamp(52px,8vw,108px);line-height:.9;letter-spacing:-.06em;margin:24px 0;color:var(--ink)}
    .hero p{max-width:700px;font-size:19px;line-height:1.5;color:#415049}
    .year{font:bold clamp(50px,8vw,115px)/.8 Georgia,serif;color:var(--coral);white-space:nowrap}
    .annual-plan{display:grid;grid-template-columns:1fr 3fr;gap:50px;padding:60px 0 70px;border-bottom:1px solid var(--ink)}
    .plan-label{font-size:16.5px;font-weight:800;letter-spacing:.17em;color:var(--headline)}
    .plan-content{max-width:960px}
    .plan-content>p{font-size:18px;line-height:1.7;color:#415049}
    .plan-lead{font:500 clamp(25px,3vw,38px)/1.25 Georgia,serif!important;letter-spacing:-.025em;color:var(--ink)!important;margin-top:0}
    .plan-content h2{margin:55px 0 24px}
    /* Titulares en azul */
    .plan-content h2, h2, h3, h4 { color: var(--headline) }

    .priorities{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--line)}
    .priorities li{display:grid;grid-template-columns:44px 1fr;gap:12px;padding:22px 22px 22px 0;border-bottom:1px solid var(--line)}
    .priorities li:nth-child(odd){border-right:1px solid var(--line)}
    .priorities li:nth-child(even){padding-left:22px}
    .priorities span{font-size:20px;font-weight:800;color:var(--coral)}
    .priorities p{margin:0;font-size:15px;line-height:1.55;color:#415049}
    .priorities strong{color:var(--ink)}
    .priorities .priority-goals{grid-column:1/-1;border-right:0;padding:30px 0;width:100%}
    .priority-goals h3{margin:0 0 12px;font:500 25px/1.15 Georgia,serif;color:var(--ink)}
    .priority-goals p+p{margin-top:12px}
    .dashboard-intro{max-width:680px;font-size:18px;line-height:1.6}
    .filters{display:grid;grid-template-columns:1fr 1fr 1fr 1.5fr;gap:14px;align-items:end;margin:25px 0}
    .filters form{margin:0}
    .filters .search input{font-size:18px}
    .kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:#fff;border:1px solid var(--line);margin:25px 0 70px}
    .kpis article{background:#fff;padding:24px;border:1px solid var(--line)}
    .kpis span{font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.09em}
    .kpis strong{display:block;font:500 55px/1 Georgia,serif;margin:18px 0 10px}
    .kpi-number{color:var(--headline)}
    .kpis small,.section-note{color:var(--muted)}
    h2{font:500 33px/1 Georgia,serif;letter-spacing:-.03em;margin-top:70px}
    .chart-card h3{font-size:18px;text-transform:uppercase;letter-spacing:.1em;margin:0 0 14px}
    .grid-two{display:grid;grid-template-columns:1fr 1fr;gap:18px}
    .chart-card{background:#fff;border:1px solid var(--line);padding:22px;border-radius:4px;overflow:hidden}
    .chart-card h3{font-size:15px;text-transform:uppercase;letter-spacing:.1em;margin:0 0 14px}
    .wide{max-width:100%}
    .cards{display:grid;gap:10px}
    .project-card{background:#fff;border:1px solid var(--line);border-radius:3px}
    .project-card summary{cursor:pointer;display:grid;grid-template-columns:100px 1fr 220px;gap:18px;align-items:center;padding:17px 20px;list-style:none}
    .project-card summary::-webkit-details-marker{display:none}
    .project-card summary strong{font-size:18px}
    .project-card summary small{text-align:right;color:var(--muted)}
    .project-body{display:grid;grid-template-columns:1fr 1fr;gap:22px;padding:5px 20px 22px;border-top:1px solid var(--line)}
    .project-body b{font-size:12px;text-transform:uppercase;letter-spacing:.1em}
    .project-body p{line-height:1.55;color:var(--ink)}
    .project-body .full{grid-column:1/-1}
    .action{background:#eef8cd;padding:15px}
    .pill{font-size:12px;text-transform:uppercase;font-weight:800;padding:6px 8px;border-radius:99px;text-align:center;background:#dfe5e2;color:#0f1a23}
    .pill-en-curso{background:#f7b955;color:#12212a}
    .pill-no-iniciado{background:#f08432;color:#12212a}
    .pill-por-iniciar{background:#f08432;color:#12212a}
    .pill-terminado{background:#4caf50;color:#fff}
    .pill-rechazado{background:#e53935;color:#fff}
    .footer{margin-top:70px;padding-top:25px;border-top:1px solid var(--ink);font-size:13px;color:var(--muted)}
    .observablehq table, .observablehq th, .observablehq td{font-size:15px}
    @media(max-width:800px){#observablehq-main{padding:0 16px 50px}.hero{display:block;padding-top:40px}.year{margin-top:28px}.annual-plan{grid-template-columns:1fr;gap:25px;padding:42px 0}.priorities{grid-template-columns:1fr}.priorities li,.priorities li:nth-child(even){padding:18px 0;border-right:0}.priorities .priority-goals{grid-column:auto}.filters,.kpis,.grid-two{grid-template-columns:1fr}.project-card summary{grid-template-columns:90px 1fr}.project-card summary small{display:none}.project-body{grid-template-columns:1fr}.kpis{gap:0}h2{font-size:38px}}
    </style>

  ```js
  const conTareas = filtrados.filter(d => d.por_hacer).length;
  const activos = filtrados.filter(d => d.estado === "En curso").length;
  const noIniciados = filtrados.filter(d => d.estado === "Por iniciar").length;
  ```

<div class="filters">
  <div>${categoriaInput}</div><div>${estadoInput}</div><div>${responsableInput}</div><div class="search">${busquedaInput}</div>
</div>

<div class="kpis">
  <article><span>Proyectos visibles</span><strong class="kpi-number">${filtrados.length}</strong><small>de ${proyectos.length} registrados</small></article>
  <article><span>En curso</span><strong class="kpi-number">${activos}</strong><small>requieren seguimiento</small></article>
  <article><span>Terminados</span><strong class="kpi-number">${terminados}</strong><small>${filtrados.length ? Math.round(terminados / filtrados.length * 100) : 0}% de la selección</small></article>
  <article><span>Por iniciar</span><strong class="kpi-number">${noIniciados}</strong><small>por activar</small></article>
</div>

## Panorama del portafolio

<div class="grid-two">
  <div class="chart-card">
    <h3>Proyectos por estado</h3>
    ${resize(width => Plot.plot({
      width,
      height: 310,
      marginLeft: 92,
      x: {label: null, grid: true, tickFormat: d => Number.isInteger(d) ? d : ""},
      y: {label: null},
      color: {domain: ["En curso", "Por iniciar", "Terminado"], range: ["#f7b955", "#f08432", "#4caf50"], legend: true},
      marks: [
        Plot.barX(filtrados, Plot.groupY({x: "count"}, {y: "estado", fill: "estado", sort: {y: "-x"}, tip: true})),
        Plot.ruleX([0])
      ]
    }))}
  </div>
  <div class="chart-card">
    <h3>Distribución por frente</h3>
    ${resize(width => Plot.plot({
      width,
      height: 310,
      marginLeft: 175,
      x: {label: null, grid: true, tickFormat: d => Number.isInteger(d) ? d : ""},
      y: {label: null},
      color: {range: ["#08306b", "#08519c", "#2171b5", "#4292c6", "#6baed6"]},
      marks: [
        Plot.barX(filtrados, Plot.groupY({x: "count"}, {y: "categoria", fill: "categoria", sort: {y: "-x"}, tip: true})),
        Plot.ruleX([0])
      ]
    }))}
  </div>
</div>

## Responsabilidades

```js
const carga = responsables
  .filter(r => filtrados.some(p => p.id === r.id))
  .reduce((map, r) => map.set(r.responsable, (map.get(r.responsable) || 0) + 1), new Map());
const cargaDatos = Array.from(carga, ([responsable, proyectos]) => ({responsable, proyectos}))
  .sort((a, b) => b.proyectos - a.proyectos)
  .slice(0, 12);
```

<div class="chart-card wide">
  <h3>Participación por responsable</h3>
  ${resize(width => Plot.plot({
    width,
    height: Math.max(310, cargaDatos.length * 32),
    marginLeft: 150,
    x: {label: "Proyectos", grid: true, tickFormat: d => Number.isInteger(d) ? d : ""},
    y: {label: null},
    marks: [
      Plot.barX(cargaDatos, {x: "proyectos", y: "responsable", fill: "responsable", sort: {y: "-x"}, tip: true}),
      Plot.text(cargaDatos, {x: "proyectos", y: "responsable", text: "proyectos", dx: 10, textAnchor: "start", fontWeight: 700})
    ],
    color: {range: ["#4b2f7f", "#5d3b8f", "#652d90", "#7a61ad", "#b29adb"]}
  }))}
</div>

## Libro de proyectos

<p class="section-note">Selecciona una fila para revisar la información o descarga la vista filtrada desde el menú de la tabla.</p>

```js
const tabla = Inputs.table(filtrados, {
  columns: ["proyecto", "categoria", "responsables", "estado", "fecha_inicio", "fecha_fin", "por_hacer"],
  header: {proyecto: "Proyecto", categoria: "Frente", responsables: "Responsable(s)", estado: "Estado", fecha_inicio: "Inicio", fecha_fin: "Fin", por_hacer: "Por hacer"},
  width: {proyecto: 260, categoria: 190, responsables: 220, estado: 100, fecha_inicio: 110, fecha_fin: 110, por_hacer: 300},
  rows: 12,
  layout: "auto"
});
display(tabla);
```

## Fichas de seguimiento

<div class="cards">
${filtrados.map(d => html`<details class="project-card">
  <summary><span class=${`pill pill-${d.estado.toLowerCase().replaceAll(" ", "-")}`}>${d.estado}</span><strong>${d.proyecto}</strong><small>${d.categoria}</small></summary>
  <div class="project-body">
    <div><b>Responsable(s)</b><p>${d.responsables || "Por definir"}</p></div>
    <div><b>Periodo</b><p>${d.fecha_inicio || "Por definir"} → ${d.fecha_fin || "Por definir"}</p></div>
    <div class="full"><b>Observaciones</b><p>${d.observaciones || "Sin observaciones registradas."}</p></div>
    <div class="full action"><b>Siguiente acción</b><p>${d.por_hacer || "Sin tareas pendientes registradas."}</p></div>
  </div>
</details>`)}
</div>

<footer class="footer">Fuente: Libro de proyectos OMD 2026–2027 · Última actualización del tablero: ${new Date().toLocaleDateString("es-MX", {dateStyle: "long"})}</footer>


