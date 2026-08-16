---
termino: Context Window
alias: token
slug: context-window
categorias: [tecnico]
relacionados: [token, llm-o-large-language-model]
actualizado: 2026-08-16
estado: publicado
---

El contexto de ventana o “Context Window (Token)”, [según IBM](https://www.ibm.com/think/topics/context-window#:~:text=The%2520context%2520window%2520(or%2520%E2%80%9Ccontext,of%2520information%2520into%2520each%2520output.), consiste en los tokens que una sistema de IA, por ejemplo ChatGPT, puede procesar o recordar como datos de entrada cuando le pedimos algo. De forma que todo lo que le pidamos que vaya por encima de ese tamaño, no lo procesará. Por ejemplo, los token suelen equivaler a 3/4 de una palabra o incluso 1,5 palabras, ya que también tienen en cuenta puntuación y espacios en blanco. Inicialmente GPT sólo [procesaba 4096 tokens](https://povio.com/blog/ai-tokens-the-building-blocks-of-language-models). De modo que en un texto de 10.000 palabras no podía procesar todo el contenido y el resumen o respuesta se vería condicionado. Con el tiempo esa ventana ha ido creciendo, y los modelos comunes operan ahora mismo entre 128 y 200 mil tokens. El más grande actualmente (marzo 2025) es **Magic.dev's LTM-2-Mini, **[con 100 millones de tokens](https://codingscape.com/blog/llms-with-largest-context-windows). Los problemas legales derivados de los token están relacionados con los sesgos, los pesos, el origen del dataset o los datos de salida de vueltos, entre otros.
