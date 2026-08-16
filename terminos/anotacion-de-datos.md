---
termino: Anotación de datos
alias: Etiquetado o data annotation
slug: anotacion-de-datos
categorias: [datos, tecnico]
relacionados: [datos-de-entrenamiento, gobernanza-de-datos, sesgo]
actualizado: 2026-08-16
estado: borrador
---

Proceso de añadir a cada dato la etiqueta que el modelo debe aprender a predecir: marcar en una grabación quién habla, señalar en una imagen la posición de una persona y si está de pie o tendida, asociar a un análisis de sangre el diagnóstico que emitió un médico. Puede ser humana, semiautomática o automática, y a menudo reutiliza caracterizaciones hechas antes con otra finalidad. El artículo 10.2.c del [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20240712) la incluye expresamente entre las operaciones de preparación de datos sujetas a gobernanza.

La [ficha de la CNIL](https://www.cnil.fr/en/annotating-data) explica por qué merece atención propia y no queda absorbida por el tratamiento general. La etiqueta es en sí misma un dato personal nuevo, que a menudo pertenece a una categoría especial —un diagnóstico, una emoción atribuida, una calificación de comportamiento— y que no estaba en el dato original: anotar no es solo organizar, es crear información sobre la persona. De ahí se siguen dos exigencias concretas: la etiqueta debe ser exacta y pertinente para la finalidad, y quien anota —con frecuencia personal externo, a veces deslocalizado— accede a datos personales, lo que convierte la anotación en un encargo de tratamiento que hay que regular y no en un mero servicio auxiliar.
