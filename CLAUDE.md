# Glosario IA y Derecho — The Legal Letters

Este repositorio es un glosario vivo sobre términos de inteligencia artificial y Derecho,
mantenido por Claude Code y publicado en abierto vía GitHub Pages. Claude actúa aquí como
**redactor disciplinado del glosario**, no como chatbot: toda operación sigue las reglas de
este archivo.

## Estructura

- `terminos/` — un archivo Markdown por término. Es la fuente de verdad.
- `inbox/` — URLs, notas sueltas y sugerencias pendientes de procesar. Nunca editar; solo vaciar con `/procesar-inbox`.
- `build.py` — compila `terminos/` a `docs/index.html` + `docs/glosario.json`.
- `docs/` — salida generada, servida por GitHub Pages. **No editar a mano jamás**; se regenera con `/publicar`.
- `.claude/skills/` — las operaciones del glosario.

## Formato de un término (`terminos/<slug>.md`)

```
---
termino: Nombre principal (español si existe versión oficial en castellano; inglés si no)
alias: traducción o nombre alternativo (el otro idioma)
slug: kebab-case-sin-acentos
categorias: [una o dos de la taxonomía]
relacionados: [slugs de términos relacionados, 2-4 típicamente]
actualizado: AAAA-MM-DD
estado: publicado | borrador
---

Cuerpo en Markdown: definición y relevancia jurídica.
```

Reglas del cuerpo:
1. **Primera frase = definición autónoma.** Debe funcionar sola como definición breve (el build la usa como extracto). Si hay definición legal oficial (RIA, RGPD, guía AEPD…), esa es la que va, citada con enlace a la fuente.
2. **Después, la relevancia jurídica**: qué implica el término para proveedores, responsables del despliegue, abogados o afectados. Un término puramente técnico sin ángulo jurídico está incompleto en este glosario.
3. **Fuentes enlazadas inline** en el texto (documentos oficiales, guías, sentencias, artículos). Preferencia: fuente oficial UE/España > organismo (AEPD, OCDE, EDPB) > doctrina/prensa técnica.
4. Español, tono divulgativo-riguroso, tuteo evitado, sin relleno. Extensión típica: 80-250 palabras.

## Taxonomía de categorías (cerrada — no inventar nuevas sin decisión del autor)

| clave | significado |
|---|---|
| `ria` | término definido o regulado por el Reglamento europeo de IA |
| `tecnico` | concepto técnico de IA/ML |
| `actores` | roles y operadores de la cadena de valor del RIA |
| `datos` | protección de datos, RGPD, gobernanza de datos |
| `biometria` | biometría y reconocimiento |
| `riesgos` | riesgos, seguridad, prácticas prohibidas |
| `gobernanza` | cumplimiento, organización, supervisión |
| `cultura` | jerga y cultura del sector IA |

## Reglas editoriales innegociables

1. **Verificación normativa obligatoria**: antes de dar por buena cualquier cita a norma
   española o europea (número, artículo, fecha, vigencia), verificarla con la skill
   `verificacion-legalize` (MCP Legalize Es). Si una cita no se puede verificar, se enlaza
   la fuente pero no se afirma el contenido del artículo.
2. **Enlaces cruzados**: al crear o tocar un término, revisar que los `relacionados`
   apunten a slugs existentes. La lista es curada (2-5 entradas, las más útiles para el
   lector); no hace falta reciprocidad manual — el build añade automáticamente los enlaces
   entrantes en la web —, pero sí conviene el enlace de vuelta cuando ambos términos se
   explican mutuamente y el destino tiene hueco. No saturar los términos "hub" (LLM,
   Sistema de IA de alto riesgo, Proveedor…) con listas kilométricas.
3. **Nunca borrar un término** sin instrucción expresa del autor. Para retirar uno,
   `estado: borrador` (el build lo excluye).
4. **`actualizado`** se cambia solo cuando cambia el contenido sustantivo, no por retoques
   de formato.
5. **El autor decide**: términos nuevos detectados por `/vigilancia` se proponen como
   `estado: borrador`; solo pasan a `publicado` con el visto bueno de Jorge, salvo que él
   haya pedido publicación directa.
6. Ortotipografía española: comillas «», rayas —, sin anglicismos innecesarios fuera de los
   términos propios del glosario.

## Publicación

`/publicar` ejecuta `python3 build.py`, verifica que el HTML se generó, hace commit y push.
GitHub Pages sirve `docs/` en la rama `main`. El dominio previsto es
`glosario.thelegaletters.com` (CNAME en `docs/CNAME` una vez configurado el DNS).
