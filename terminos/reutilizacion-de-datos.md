---
termino: Reutilización de datos
alias: Difusor y reutilizador de datos
slug: reutilizacion-de-datos
categorias: [datos]
relacionados: [web-scraping, fase-de-desarrollo, responsable-del-tratamiento]
actualizado: 2026-08-16
estado: borrador
---

Uso de datos ya recogidos —propios o ajenos— para construir un conjunto de entrenamiento. Es la vía por la que se alimentan la mayoría de los modelos, y la [CNIL](https://www.cnil.fr/node/164402) exige distinguir dos supuestos con consecuencias distintas.

Si la organización reutiliza datos que ella misma recogió para otra finalidad, debe superar el **test de compatibilidad** del artículo 6.4 del RGPD: comprobar que el nuevo tratamiento es compatible con aquel para el que se recogieron, salvo que se apoye en el consentimiento o en una norma. No hace falta test cuando la finalidad de entrenamiento se previó y se comunicó desde la recogida, lo que convierte una cláusula informativa bien redactada en la diferencia entre poder reutilizar y no poder.

Si los datos vienen de un tercero, la CNIL separa dos figuras: el **difusor**, quien publica en línea los datos o el conjunto, y el **reutilizador**, quien los trata por cuenta propia. Cada uno responde de su propio tratamiento —el difusor de la difusión, el reutilizador del uso—, y el difusor no responde en principio de lo que otros hagan después, aunque puede imponer condiciones que limiten la reutilización. Para el reutilizador la consecuencia es incómoda pero clara: la licitud del origen no se hereda, hay que verificarla.
