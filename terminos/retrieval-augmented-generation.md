---
termino: Retrieval-Augmented Generation
alias: RAG
slug: retrieval-augmented-generation
categorias: [tecnico, datos]
relacionados: [embedding, llm-o-large-language-model, alucinacion, ia-generativa]
actualizado: 2026-08-16
estado: publicado
---

La *“Generación aumentada con recuperación”* es una arquitectura híbrida que primero recupera documentos relevantes de una base externa (por ejemplo, tus modelos de contrato) y luego los introduce en el modelo generativo, combinando precisión factual con capacidad de lenguaje. Legalmente hablando, el componente de recuperación podría estar creando un tratamiento adicional de datos que puede alterar la base jurídica del procesamiento. Además, la inserción de textos completos en las ventanas de contexto puede infringir derechos de reproducción de obras protegidas si no media excepción o la licencia correspondiente.

La conferencia de autoridades alemanas de protección de datos le dedicó en octubre de 2025 una [orientación específica](https://www.datenschutzkonferenz-online.de/media/oh/DSK_OH_RAG.pdf) que analiza la arquitectura frente a cada principio del RGPD, y su conclusión matiza el entusiasmo habitual. A favor: al apoyar las respuestas en documentos concretos, RAG mejora la exactitud y la transparencia, y permite actualizar o borrar información sin reentrenar el modelo, lo que facilita atender los derechos de rectificación y supresión —el punto donde los modelos puros fallan—. En contra: la base documental es un tratamiento propio que hay que legitimar, delimitar por finalidad y minimizar, y los controles de acceso del repositorio original no se heredan solos, de modo que un sistema mal configurado convierte en consultable por cualquiera lo que estaba restringido a unos pocos.
