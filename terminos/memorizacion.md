---
termino: Memorización
alias: Regurgitación o memorisation
slug: memorizacion
categorias: [tecnico, datos]
relacionados: [anonimato-de-los-modelos, sobreaprendizaje, datos-de-entrenamiento]
actualizado: 2026-08-16
estado: publicado
---

Fenómeno por el que un modelo retiene fragmentos literales de sus datos de entrenamiento y puede llegar a reproducirlos en sus salidas. Cuando la reproducción ocurre en el uso normal del sistema —basta a veces un *prompt* muy específico— suele hablarse de regurgitación; cuando hace falta un ataque deliberado para extraerlos, de extracción.

Es el mecanismo del que depende todo lo demás en materia de datos personales: si el modelo memoriza, deja de ser anónimo. La [ficha de la CNIL](https://www.cnil.fr/en/analysing-status-ai-model-regard-gdpr) enumera los indicios que obligan a sospecharlo: datos raros o atípicos en el conjunto de entrenamiento —los *outliers* son los que más se memorizan—, modelos con muchos parámetros en relación con el volumen de datos, ausencia de medidas contra el sobreaprendizaje, funcionalidades destinadas a reproducir contenidos similares a los de entrenamiento, y ataques exitosos publicados sobre modelos comparables.

Dos advertencias de la CNIL merecen retenerse. Que un modelo no regurgite nada en pruebas rápidas no demuestra que no memorice; solo el resultado positivo es concluyente. Y las medidas contra el sobreaprendizaje —regularización, *dropout*, parada temprana— reducen la memorización pero no la eliminan, de modo que sirven como mitigación documentable, no como prueba de anonimato.
