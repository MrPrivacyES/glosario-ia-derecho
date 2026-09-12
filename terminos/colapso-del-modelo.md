---
termino: Colapso del modelo
alias: Model collapse
slug: colapso-del-modelo
categorias: [tecnico, datos]
relacionados: [datos-sinteticos, datos-de-entrenamiento, calidad-de-los-datos, sobreaprendizaje, memorizacion]
actualizado: 2026-09-12
estado: publicado
---

Degradación progresiva que sufre un modelo generativo cuando se entrena, generación tras generación, con contenido producido por modelos anteriores en lugar de con datos originales: las colas de la distribución desaparecen primero, la diversidad de las salidas se estrecha y el resultado acaba alejándose de la realidad que pretendía representar. Lo describió el equipo de Shumailov en [*AI models collapse when trained on recursively generated data*](https://www.nature.com/articles/s41586-024-07566-y), publicado en *Nature* en julio de 2024, que concluye que el uso indiscriminado de contenido generado por modelos introduce defectos irreversibles.

El ángulo jurídico es de calidad de los datos, no de derechos de autor. El artículo 10.3 del [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20260727) exige que los conjuntos de entrenamiento, validación y prueba de un sistema de alto riesgo sean «pertinentes, suficientemente representativos y, en la mayor medida posible, carecerán de errores y estarán completos en vista de su finalidad prevista», y el artículo 10.2.f nombra el mecanismo casi con estas palabras al obligar a examinar los sesgos «especialmente cuando las salidas de datos influyan en las informaciones de entrada de futuras operaciones». Un conjunto contaminado con salidas sintéticas no declaradas compromete ese requisito y, con él, la documentación técnica y la evaluación de la conformidad.

De ahí dos cautelas prácticas. Primera: la procedencia de los datos deja de ser un asunto de propiedad intelectual y pasa a ser también de trazabilidad técnica, con la consiguiente exigencia contractual al proveedor del conjunto. Segunda: el colapso se mitiga conservando una proporción no despreciable de datos reales, de modo que quien contrata datos sintéticos por su comodidad regulatoria debería pactar también ese suelo.
