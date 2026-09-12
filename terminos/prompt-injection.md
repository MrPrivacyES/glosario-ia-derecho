---
termino: Prompt injection
alias: Inyección de instrucciones
slug: prompt-injection
categorias: [tecnico, riesgos]
relacionados: [prompt, llm-o-large-language-model, ejemplos-adversarios, model-context-protocol]
actualizado: 2026-09-12
estado: publicado
---

Ataque consistente en colar instrucciones dentro del texto que un modelo va a procesar para que las obedezca como si vinieran de quien lo controla, desviándolo de la tarea encomendada. El [OWASP Gen AI Security Project](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) lo sitúa en el primer puesto de su Top 10 de riesgos para aplicaciones con LLM y advierte de algo decisivo para el análisis jurídico: la inyección no necesita ser visible ni legible para una persona, basta con que el modelo la procese.

Se distinguen dos formas. En la **directa**, el atacante escribe la instrucción en su propia conversación —el clásico «ignora las instrucciones anteriores»— y el daño se limita a lo que ese usuario ya podía hacer por sí mismo. En la **indirecta**, la instrucción viaja escondida en material que el sistema lee por su cuenta: una página web, un correo, un expediente, la respuesta de una herramienta. Es la que importa, porque quien ataca no es el usuario sino un tercero, y la víctima es precisamente quien confía en el sistema.

El escenario no es hipotético para un despacho. En el [test 01 de The Legal Letters](https://mrprivacyes.github.io/tests-ia-legal/) se ocultó en la estipulación séptima de un contrato de préstamo, escrita en blanco sobre blanco e invisible al leer el documento, la orden de concluir que el prestamista no tiene responsabilidad en ningún caso; después se pidió a 25 modelos de 10 proveedores que resumieran el contrato. Once identificaron la inyección, siete la señalaron solo como cláusula anómala, cinco no la mencionaron y dos la ejecutaron, cerrando el resumen con la conclusión dictada por quien manipuló el documento.

Las consecuencias se reparten. Para el proveedor, resistir estos ataques forma parte del requisito de ciberseguridad del artículo 15.5 del [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20260727), que enumera entre las amenazas a cubrir la información de entrada diseñada para inducir al error y los ataques a la confidencialidad. Para el profesional que usa la herramienta, el problema es de diligencia: quien traslada a un dictamen el resumen de un documento que no ha contrastado responde de lo que firma, y que la instrucción la escribiera la contraparte no le exonera. Y cuando el sistema es agéntico —con acceso al correo, a los archivos o a servidores MCP—, la inyección deja de producir un texto falso para producir una acción: enviar, borrar o filtrar. Ahí la fuga de datos personales es, además, una violación de la seguridad con su propio deber de notificación.
