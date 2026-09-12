---
termino: Marca de agua
alias: Watermarking
slug: marca-de-agua
categorias: [ria, tecnico]
relacionados: [contenido-sintetico, ultrafalsificacion, codigo-de-buenas-practicas]
actualizado: 2026-09-12
estado: publicado
---

Señal imperceptible que se incrusta en el propio contenido generado por una IA —en los píxeles de una imagen, en la onda de audio o en la distribución de los tokens de un texto— para que una máquina pueda después detectar su origen artificial, incluso tras recortes, recompresiones o capturas de pantalla. No es un requisito nominal del Reglamento de IA: el [artículo 50.2 del Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20240712) exige un marcado «en un formato legible por máquina», y el considerando 133 cita las marcas de agua junto a la identificación de metadatos, los métodos criptográficos de procedencia, los métodos de registro y las impresiones dactilares como técnicas admisibles.

Para el abogado, la consecuencia práctica es que la obligación es de resultado, no de medio: hay libertad de solución técnica, pero debe ser eficaz, interoperable, sólida y fiable en la medida en que sea técnicamente viable. El [Código de buenas prácticas sobre transparencia del contenido generado por IA](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations) propone un enfoque en capas —divulgación visible, metadatos firmados digitalmente y marca de agua imperceptible— como forma acreditada de cumplir.

La marca de agua en **texto**, que era el caso más difícil y el que más dudas planteaba, ha pasado en 2026 de la teoría a la práctica: Anthropic [anunció en agosto](https://fortune.com/2026/08/11/anthropic-claude-watermark-ai-text-police-ai-slop/) que sus modelos lanzados a partir del 2 de agosto de 2026 —la fecha en que empezó a aplicarse el artículo 50— incrustan una señal detectable por máquina en la elección de palabras del modelo, sin alterar el sentido ni la calidad del texto, y que la aplicará en todo el mundo y no solo en Europa. Dos matices importan al abogado. El primero, que la detección es probabilística y solo indica que el modelo intervino, no que generara el texto entero: pedirle que corrija o traduzca un párrafo puede dejar rastro. El segundo, que la verificación depende de la clave criptográfica del proveedor, lo que sitúa al propio proveedor como tercero necesario en cualquier disputa probatoria sobre el origen de un texto.
