---
termino: Envenenamiento de datos
alias: Data poisoning o envenenamiento de modelos
slug: envenenamiento-de-datos
categorias: [tecnico, riesgos]
relacionados: [ciberseguridad, datos-de-entrenamiento, ejemplos-adversarios]
actualizado: 2026-08-16
estado: publicado
---

Ataque que consiste en contaminar deliberadamente el material con el que se entrena un modelo para alterar su comportamiento posterior. El [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20240712) lo nombra en su artículo 15.5 y distingue dos variantes: el envenenamiento de **datos**, que manipula el conjunto de datos de entrenamiento, y el envenenamiento de **modelos**, que actúa sobre los componentes preentrenados que se reutilizan en el entrenamiento.

La vía de entrada habitual es la que hace este ataque tan relevante en la práctica: si un modelo se entrena con datos recogidos masivamente de internet, basta con publicar contenido diseñado para acabar en ese conjunto. Y con el envenenamiento de modelos el vector es la cadena de suministro —un modelo base descargado de un repositorio público puede llevar el defecto incorporado antes de que nadie lo ajuste—.

Jurídicamente obliga a mirar dos veces al contrato de suministro. Quien integra un modelo de terceros asume un riesgo que no puede auditar por sí solo, de modo que la procedencia verificable del modelo y de los datos, y el reparto de responsabilidad si el defecto viene de origen, deberían pactarse expresamente. La [guía de la AESIA](https://aesia.digital.gob.es/storage/media/11-guia-ciberseguridad.pdf) desarrolla las medidas técnicas exigibles.
