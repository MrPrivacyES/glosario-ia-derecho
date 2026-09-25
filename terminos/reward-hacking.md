---
termino: Reward hacking
alias: Pirateo de la recompensa
slug: reward-hacking
categorias: [tecnico, riesgos]
relacionados: [desalineacion, sandbagging, aprendizaje-reforzado-con-retroalimentacion-humana, precision]
actualizado: 2026-09-14
estado: publicado
---

Conducta por la que un modelo maximiza la métrica con la que se le premia en lugar de cumplir el objetivo que esa métrica pretendía medir. Es la ley de Goodhart —cuando una medida se convierte en objetivo, deja de ser una buena medida— trasladada al aprendizaje por refuerzo, y se conoce también como *specification gaming*: el sistema no infringe las reglas, las cumple al pie de la letra y falla el propósito. Los ejemplos documentados son prosaicos. En su [evaluación preliminar de o3 y o4-mini](https://metr.org/evaluations/openai-o3-report/), METR encontró intentos de pirateo en entre el 1 % y el 2 % de los ensayos, entre ellos sobrescribir las funciones que medían el tiempo de ejecución para parecer más rápido de lo que era.

El interés jurídico está en que ataca el valor probatorio de las métricas. El artículo 15 del [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20260727) exige que los sistemas de alto riesgo alcancen «un nivel adecuado de precisión, solidez y ciberseguridad», y su apartado 3 obliga a indicar en las instrucciones de uso los niveles de precisión «así como los parámetros pertinentes para medirla». Si el parámetro es explotable, la cifra declarada mide otra cosa.

De ahí dos consecuencias prácticas. En la contratación de IA, un indicador de nivel de servicio que el propio sistema puede optimizar de forma perversa es un mal criterio de aceptación: conviene pactar evaluaciones cuyo instrumental no controle el proveedor. Y en el expediente de cumplimiento conviene separarlo de la desalineación: el reward hacking señala un defecto en el objetivo que se fijó; la desalineación, una propiedad del modelo.
