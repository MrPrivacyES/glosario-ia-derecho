---
termino: Ajuste fino
alias: Fine-tuning
slug: ajuste-fino
categorias: [tecnico, datos]
relacionados: [aprendizaje-por-transferencia, datos-de-entrenamiento, proveedor-posterior]
actualizado: 2026-08-16
estado: publicado
---

Segunda fase del entrenamiento de un modelo: sobre un modelo ya preentrenado con un corpus general y costoso, se realiza un entrenamiento adicional con un conjunto de datos mucho más pequeño y específico para especializarlo en una tarea, un dominio o un estilo. Es la técnica que permite a una organización mediana tener un modelo propio sin entrenar nada desde cero.

Jurídicamente abre tres frentes. El primero es de roles: quien ajusta un modelo ajeno con datos propios decide la finalidad y los medios esenciales de ese tratamiento, de modo que la [CNIL](https://www.cnil.fr/node/164396) lo califica de responsable del tratamiento; y bajo el Reglamento de IA puede convertirse en proveedor posterior. El segundo es de riesgo: los datos de ajuste suelen ser los más sensibles —historiales, expedientes, documentación interna— y son también los que un modelo memoriza con más facilidad, por su escaso volumen. La [CNIL](https://www.cnil.fr/en/analysing-status-ai-model-regard-gdpr) recomienda por eso separar en el análisis la probabilidad de extracción de los datos de preentrenamiento y la de los de ajuste, porque los riesgos son distintos. El tercero es contractual: conviene pactar qué ocurre con el modelo ajustado si se rescinde la licencia del modelo base.
