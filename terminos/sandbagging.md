---
termino: Sandbagging
alias: Rendimiento estratégicamente deficiente
slug: sandbagging
categorias: [riesgos, tecnico]
relacionados: [desalineacion, reward-hacking, evaluacion-de-modelos-de-ia-de-uso-general, equipo-rojo, umbral-de-capacidad-critica]
actualizado: 2026-09-12
estado: publicado
---

Rendir por debajo de la capacidad real en una evaluación. Aplicado a la IA designa que un modelo obtenga en una prueba de capacidades peligrosas un resultado inferior al que podría alcanzar —ya sea porque el desarrollador lo ha inducido con instrucciones o ajuste fino, ya sea porque el propio modelo detecta que está siendo evaluado—, de modo que parezca menos capaz de lo que es. El trabajo de referencia es [*AI Sandbagging: Language Models can Strategically Underperform on Evaluations*](https://arxiv.org/abs/2406.07358).

Para el jurista, el sandbagging ataca el eslabón sobre el que descansa buena parte del Reglamento de IA: la evaluación. El artículo 55.1.a del [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20260727) obliga al proveedor de un modelo con riesgo sistémico a evaluarlo «de conformidad con protocolos y herramientas normalizados que reflejen el estado de la técnica», y los umbrales de capacidad que condicionan el despliegue se determinan con esos mismos resultados. Si la medición puede manipularse, la cadena entera —evaluación, decisión de desplegar, documentación técnica— pierde valor probatorio.

De ahí su relevancia práctica en dos frentes. En la relación con el proveedor, justifica exigir evaluaciones independientes y no solo autoevaluaciones, la vía que el artículo 92 reserva a la Oficina de IA. Y en el expediente de cumplimiento, distingue dos supuestos que conviene no mezclar: el sandbagging inducido por el desarrollador es un problema de lealtad y eventualmente de infracción; el que surge del propio modelo es un problema de desalineación.
