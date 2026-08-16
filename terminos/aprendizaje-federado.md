---
termino: Aprendizaje federado
alias: Federated learning o FL
slug: aprendizaje-federado
categorias: [tecnico, datos]
relacionados: [tecnologias-de-mejora-de-la-privacidad, aprendizaje-automatico, responsable-del-tratamiento]
actualizado: 2026-08-16
estado: publicado
---

Modalidad de aprendizaje automático en la que varias fuentes de datos —dispositivos o servidores— colaboran para entrenar un modelo compartido manteniendo los datos descentralizados: en lugar de enviar los datos originales a un servidor central, cada fuente entrena localmente con los suyos y solo comparte actualizaciones del modelo, es decir, gradientes o pesos. La definición y el desarrollo son del [TechDispatch sobre aprendizaje federado](https://www.aepd.es/guias/tech-dispatch-aprendizaje-federado.pdf) difundido por la AEPD. Se distingue entre federación horizontal y vertical, y entre dispositivos transversales —millones de teléfonos— y silos transversales —unos pocos hospitales o bancos—.

Su atractivo jurídico es evidente: permite entrenar sobre datos de varias organizaciones sin que ninguna ceda sus bases, lo que lo convierte en la arquitectura de referencia para la investigación sanitaria multicéntrica. Pero no es una fórmula mágica de cumplimiento. Las actualizaciones del modelo pueden filtrar información sobre los datos locales y son atacables mediante inferencia de pertenencia o reconstrucción, de modo que a menudo siguen siendo datos personales. Y plantea un problema de roles que hay que resolver por escrito antes de empezar: quién es responsable de cada tratamiento local, quién del modelo agregado y si hay corresponsabilidad entre los participantes y el coordinador.
