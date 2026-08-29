---
termino: Ingeniería de contexto
alias: Context engineering
slug: ingenieria-de-contexto
categorias: [tecnico, datos]
relacionados: [prompt, context-window, retrieval-augmented-generation, ia-agentica]
actualizado: 2026-08-26
estado: publicado
---

Conjunto de estrategias para seleccionar y mantener la información —los *tokens*— que un modelo tiene delante en cada paso de la inferencia, [según la definición de Anthropic de 29 de septiembre de 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) que popularizó el término. La diferencia con el *prompt engineering* es de nivel: este se ocupa de cómo redactar la instrucción; aquella, de qué entra en la ventana de contexto en su conjunto —instrucciones de sistema, herramientas y sus resultados, ejemplos, historial, notas de memoria y datos recuperados de fuentes externas— y de qué se descarta cuando el espacio se agota, mediante técnicas como la compactación por resumen.

La relevancia jurídica está en ese desplazamiento. Mientras la interacción se reducía al *prompt*, era razonable analizar el tratamiento a partir de lo que la persona escribía. En un sistema con ingeniería de contexto, lo que llega al modelo lo decide una canalización diseñada por el proveedor o por el responsable del despliegue: qué documentos se recuperan, qué historial se arrastra, qué se guarda como memoria persistente entre sesiones y con qué herramientas se consulta. Eso convierte la minimización de datos del artículo 5.1.c del [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02016R0679-20160504) en una decisión de arquitectura, no de buen uso por parte del usuario, y traslada a quien diseña la carga de justificar por qué cada pieza de contexto era necesaria para la finalidad.

De ahí tres consecuencias prácticas. La memoria persistente exige base jurídica y plazo propios: guardar el contexto de sesiones anteriores es conservación, no continuidad de la conversación. En el despacho, el contexto es el vehículo natural de la fuga de secreto profesional —el expediente entero puede acabar inyectado sin que nadie lo teclee—, y la AEPD ya advierte de que, además de lo que se escribe en el *prompt*, [se envía a la IA información que el usuario no ve](https://www.aepd.es/guias/recomendaciones-ia-aepd.pdf). Y la trazabilidad se complica: si el contexto se recorta o se resume automáticamente, reconstruir después por qué el sistema respondió lo que respondió obliga a registrar el contexto efectivo de cada llamada, no solo la pregunta y la respuesta.
