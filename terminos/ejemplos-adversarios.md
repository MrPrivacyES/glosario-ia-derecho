---
termino: Ejemplos adversarios
alias: Adversarial examples o evasión de modelos
slug: ejemplos-adversarios
categorias: [tecnico, riesgos]
relacionados: [ciberseguridad, envenenamiento-de-datos, prompt-injection]
actualizado: 2026-08-16
estado: publicado
---

Entradas manipuladas de forma deliberada, a menudo con alteraciones imperceptibles para una persona, que hacen que un modelo cometa un error. El [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20240712) los define en su artículo 15.5 como «la información de entrada diseñada para hacer que el modelo de IA cometa un error», y les da como sinónimo la «evasión de modelos».

El ejemplo clásico es visual: unas pegatinas colocadas sobre una señal de tráfico que llevan a un sistema de conducción a leer un límite de velocidad distinto, o un ruido añadido a una fotografía que cambia por completo la clasificación sin que el ojo humano note nada. La diferencia con el envenenamiento de datos está en el momento del ataque: aquél corrompe el entrenamiento; éste actúa sobre el sistema ya desplegado y en funcionamiento.

Para el jurista, el interés está en que rompe una presunción cómoda: que un sistema validado con buenos resultados seguirá comportándose así. Un sistema puede ser preciso y sólido y aun así fallar de forma dirigida ante un atacante, lo que traslada la cuestión al terreno de la diligencia —qué pruebas de resistencia se hicieron, qué se documentó— y no al del resultado. La [guía de la AESIA](https://aesia.digital.gob.es/storage/media/11-guia-ciberseguridad.pdf) recoge las medidas de mitigación exigibles.
