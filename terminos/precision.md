---
termino: Precisión
alias: Accuracy
slug: precision
categorias: [ria, tecnico]
relacionados: [solidez, ciberseguridad, sobreaprendizaje]
actualizado: 2026-08-17
estado: publicado
---

Grado en que los resultados de un sistema de IA se corresponden con los correctos. El artículo 15 del [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20240712) exige que los sistemas de alto riesgo alcancen un nivel adecuado de precisión, solidez y ciberseguridad y funcionen de manera uniforme en esos sentidos durante todo su ciclo de vida, y obliga a declarar en las instrucciones de uso los niveles de precisión y los parámetros con los que se han medido.

Hay aquí una trampa terminológica que la [guía de la AESIA](https://aesia.digital.gob.es/storage/media/09-guia-de-precision.pdf) señala expresamente: el Reglamento traduce el inglés *accuracy* por «precisión», pero en estadística y aprendizaje automático «precisión» designa una métrica distinta (*precision*, la proporción de aciertos entre los casos señalados como positivos), mientras que *accuracy* es la proporción global de aciertos. Quien lea un informe técnico en inglés y un contrato en español puede estar hablando de dos cosas distintas con la misma palabra, y conviene fijar en el contrato qué métrica concreta se compromete.

Lo relevante jurídicamente es que el Reglamento no impone un umbral: exige que el nivel sea adecuado a la finalidad prevista, se declare y se mantenga. El compromiso de precisión pasa así a ser materia negociable —y exigible— entre proveedor y responsable del despliegue.

Cuando hay datos personales de por medio conviene además no confundir esta precisión con la exactitud del artículo 5.1.d del RGPD, que responde a otra lógica. La [nota técnica de la AEPD de 21 de julio de 2026](https://www.aepd.es/guias/calidad-datos-inteligencia-artificial.pdf) lo ordena así: la exactitud mira a la idoneidad de los datos para la finalidad —y puede exigir un nivel de precisión concreto—, mientras que la minimización impide superar el que resulte necesario. Las dos obligaciones se suman a la del artículo 15 del Reglamento de IA sin sustituirla, de modo que un sistema puede cumplir el umbral técnico declarado y aun así tratar datos con una granularidad excesiva.
