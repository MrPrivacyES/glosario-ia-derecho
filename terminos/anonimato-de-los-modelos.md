---
termino: Anonimato de un modelo de IA
alias: Estatuto del modelo o model anonymity
slug: anonimato-de-los-modelos
categorias: [datos, tecnico]
relacionados: [memorizacion, ataques-de-reidentificacion, medios-razonablemente-utilizables, modelo-de-ia-de-uso-general]
actualizado: 2026-08-16
estado: publicado
---

Cuestión previa a cualquier análisis de protección de datos sobre un modelo entrenado con datos personales: si del propio modelo pueden extraerse esos datos, el RGPD se aplica al modelo; si no, el modelo es anónimo y queda fuera. Un modelo es una representación estadística de las características de la base con la que se entrenó, y esa representación puede ser lo bastante fiel como para que los datos originales se reconstruyan.

El [Dictamen 28/2024 del CEPD](https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en) fijó el criterio: hay que analizarlo caso por caso; un modelo diseñado específicamente para producir o inferir información sobre las personas de su conjunto de entrenamiento contiene datos personales sin más discusión; y para que un modelo entrenado con datos personales sin esa finalidad sea anónimo debe ser altamente improbable tanto identificar a esas personas a partir de sus parámetros —ataques de caja blanca— como extraer los datos mediante consultas.

La [ficha de la CNIL](https://www.cnil.fr/en/analysing-status-ai-model-regard-gdpr) convierte el criterio en método: el proveedor debe documentar el análisis, indicar los indicios de memorización y, en la mayoría de los casos, aportar los resultados de pruebas de ataque de reidentificación. La conclusión práctica incomoda pero es clara: afirmar que un modelo es anónimo sin haberlo probado no es una posición defendible ante una autoridad.
