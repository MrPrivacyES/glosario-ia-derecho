---
termino: Mixture of Experts (MoE) o “Mezcla de expertos”
alias: 
slug: mixture-of-experts
categorias: [tecnico]
relacionados: [llm-o-large-language-model, parametros]
actualizado: 2026-08-16
estado: publicado
---

Arquitectura en la que varios sub-modelos especializados (“Expertos”) compiten o son seleccionados dinámicamente mediante un router para responder a cada entrada, aumentando la capacidad efectiva sin elevar el coste de inferencia linealmente ([explicación técnica de Hugging Face](https://huggingface.co/blog/moe)). Legalmente hablando, las rutas de activación crean trazabilidad dentro del modelo, aspecto valioso para el deber de explicación. Sin embargo, también complican la atribución de fallos y la determinación de qué “experto” concreto causó un daño, lo que afecta a la prueba de defectuosidad en responsabilidad civil extracontractual. DeepSeek ha sido uno de los modelos que más ha recurrido a MoE.
