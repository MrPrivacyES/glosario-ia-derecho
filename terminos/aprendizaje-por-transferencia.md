---
termino: Aprendizaje por transferencia
alias: Transfer learning
slug: aprendizaje-por-transferencia
categorias: [tecnico]
relacionados: [ajuste-fino, aprendizaje-automatico, open-weights]
actualizado: 2026-08-16
estado: publicado
---

Técnica que reutiliza un modelo entrenado para una tarea como punto de partida para otra distinta, aprovechando las representaciones que ya aprendió. Un modelo entrenado para reconocer objetos en fotografías sirve, con relativamente pocos datos añadidos, para detectar defectos en piezas industriales o lesiones en radiografías. Es más amplio que el ajuste fino: éste especializa un modelo dentro de su misma tarea, aquél lo traslada a otra.

Su relevancia jurídica está en la cadena de valor que crea. Quien parte de un modelo de terceros hereda todo lo que ese modelo trae dentro —los datos con los que se entrenó, sus sesgos, su eventual memorización y los defectos que pueda arrastrar— sin haber participado en esas decisiones ni poder auditarlas con facilidad. La [CNIL](https://www.cnil.fr/node/164396) considera responsable del tratamiento a quien reentrena o adapta un modelo preentrenado con un conjunto de datos propio, cuando persigue una finalidad propia y determina él mismo los medios esenciales. Y bajo el Reglamento de IA, modificar un modelo ajeno puede bastar para asumir obligaciones de proveedor. En términos prácticos, es la razón por la que la procedencia documentada del modelo base debería exigirse siempre por contrato.
