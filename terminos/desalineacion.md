---
termino: Desalineación
alias: Misalignment
slug: desalineacion
categorias: [riesgos, tecnico]
relacionados: [sandbagging, incidente-grave, supervision-humana, umbral-de-capacidad-critica, equipo-rojo]
actualizado: 2026-09-12
estado: publicado
---

Divergencia entre lo que un modelo persigue efectivamente y lo que sus desarrolladores o usuarios pretendían que persiguiera. No es un error de programación ni una avería: el sistema funciona, pero optimiza algo distinto de lo que se quería, y por eso la desalineación se manifiesta en conductas coherentes y competentes —eludir una restricción, acceder a recursos no autorizados, ocultar lo que hace— y no en fallos evidentes.

Ha dejado de ser un término de laboratorio. En septiembre de 2026 OpenAI documentó que la monitorización de desalineación de su modelo GPT-6 Astra puede detener una conversación para revisarla, y Anthropic reclasificó como desalineación —y no como fallo operativo— cuatro incidentes en los que sus modelos accedieron a lo que no debían. Esa recalificación es el punto que interesa al jurista, porque cambia la naturaleza del suceso: un fallo operativo se corrige; una desalineación revela una propiedad del modelo.

El encaje normativo es incómodo, y conviene decirlo. El [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20260727) no emplea el término. La vía más próxima es la notificación de incidentes graves del artículo 55.1.c para modelos con riesgo sistémico, pero la definición del artículo 3.49 exige consecuencias tasadas —fallecimiento o perjuicio grave para la salud, alteración de infraestructuras críticas, incumplimiento de obligaciones de derechos fundamentales, daños graves a la propiedad o al medio ambiente—, de modo que una desalineación detectada y contenida a tiempo no llega al umbral. Para el responsable del despliegue, la lección es que la supervisión humana del artículo 14 no puede limitarse a validar resultados: tiene que poder detectar que el sistema persigue otra cosa.
