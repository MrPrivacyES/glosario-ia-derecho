---
termino: Context Window
alias: token
slug: context-window
categorias: [tecnico]
relacionados: [token, llm-o-large-language-model, ingenieria-de-contexto]
actualizado: 2026-08-26
estado: publicado
---

El contexto de ventana o “Context Window (Token)”, [según IBM](https://www.ibm.com/think/topics/context-window#:~:text=The%2520context%2520window%2520(or%2520%E2%80%9Ccontext,of%2520information%2520into%2520each%2520output.), consiste en los tokens que un sistema de IA, por ejemplo ChatGPT, puede procesar o recordar como datos de entrada cuando le pedimos algo. De forma que todo lo que le pidamos que vaya por encima de ese tamaño, no lo procesará. Por ejemplo, los token suelen equivaler a 3/4 de una palabra o incluso 1,5 palabras, ya que también tienen en cuenta puntuación y espacios en blanco. Inicialmente GPT sólo [procesaba 4096 tokens](https://povio.com/blog/ai-tokens-the-building-blocks-of-language-models). De modo que en un texto de 10.000 palabras no podía procesar todo el contenido y el resumen o respuesta se vería condicionado. Con el tiempo esa ventana ha ido creciendo con rapidez: de los 128.000 a 200.000 tokens habituales en 2025 se ha pasado al millón —y hasta dos millones en algunos modelos— en las familias punteras de 2026, y el récord anunciado sigue siendo el de LTM-2-Mini de Magic.dev, [con 100 millones de tokens](https://codingscape.com/blog/llms-with-largest-context-windows). Conviene por eso desconfiar de cualquier cifra concreta: envejece en meses, y lo que no envejece es la consecuencia jurídica. Los problemas legales derivados de los token están relacionados con los sesgos, los pesos, el origen del dataset o los datos de salida de vueltos, entre otros.
