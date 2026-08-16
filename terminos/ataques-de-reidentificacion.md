---
termino: Ataques de reidentificación
alias: Inferencia de pertenencia, inversión de modelo o reconstrucción
slug: ataques-de-reidentificacion
categorias: [tecnico, datos]
relacionados: [anonimato-de-los-modelos, memorizacion, ciberseguridad]
actualizado: 2026-08-16
estado: publicado
---

Familia de técnicas que buscan recuperar datos personales a partir de un modelo ya entrenado, y que la [CNIL](https://www.cnil.fr/en/analysing-status-ai-model-regard-gdpr) exige ensayar antes de afirmar que un modelo es anónimo. Las principales son cuatro. La **inferencia de pertenencia** (*membership inference*) determina si los datos de una persona concreta estaban en el conjunto de entrenamiento —lo que ya revela información sensible cuando el conjunto es, por ejemplo, una cohorte de pacientes—. La **inversión de modelo** reconstruye características de los datos originales a partir de las respuestas del modelo. La **reconstrucción** recupera registros completos. Y la **exfiltración** obtiene datos consultando directamente el sistema.

Para el abogado hay tres consecuencias. La primera: resistir a un tipo de ataque no prejuzga la resistencia a otro, de modo que un informe que solo pruebe uno no cierra el análisis. La segunda: la evaluación debe contemplar no solo al responsable, sino a terceros que no deberían tener acceso, y por eso restringir el acceso reduce la probabilidad pero no la vuelve insignificante por sí sola. La tercera: las garantías legales y contractuales que limitan el uso de un modelo complementan las técnicas de anonimización, pero no las sustituyen.
