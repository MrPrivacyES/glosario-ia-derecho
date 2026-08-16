---
termino: Sobreaprendizaje
alias: Overfitting o sobreajuste
slug: sobreaprendizaje
categorias: [tecnico]
relacionados: [precision, datos-de-entrenamiento, datos-de-validacion]
actualizado: 2026-08-16
estado: publicado
---

Defecto de un modelo que ha aprendido demasiado bien los datos con los que se entrenó —incluidos su ruido y sus peculiaridades— y por eso rinde de maravilla sobre ellos y mal sobre datos nuevos. Es el motivo por el que se reservan conjuntos de datos de validación y de prueba separados: sin ellos, las métricas del entrenamiento son un espejismo.

El [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20240712) no lo menciona, pero es el fenómeno que está detrás de varias de sus exigencias: la separación de conjuntos de entrenamiento, validación y prueba del artículo 10, la representatividad de los datos y los niveles declarados de precisión y solidez del artículo 15. La [guía de la AESIA sobre precisión](https://aesia.digital.gob.es/storage/media/09-guia-de-precision.pdf) lo trata como un problema a controlar a lo largo del ciclo de vida.

El interés para un abogado es concreto: cuando un proveedor exhibe una cifra de precisión, la pregunta pertinente no es cuánto vale sino sobre qué datos se midió. Una precisión altísima obtenida sobre el propio conjunto de entrenamiento no acredita nada, y un sistema sobreajustado a una población acaba fallando justo con quien no se parece a ella —lo que convierte un defecto técnico en un problema de discriminación—.
