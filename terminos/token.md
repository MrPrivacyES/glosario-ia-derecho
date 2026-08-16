---
termino: Token
alias: 
slug: token
categorias: [tecnico]
relacionados: [context-window, embedding, llm-o-large-language-model]
actualizado: 2026-08-16
estado: publicado
---

consisten en datos de entrada transformados de forma que el sistema de IA pueda entenderlos, analizarlos, recordarlos y procesarlos para proporcionar los datos de salida más ajustados. Los datos de entrada se tokenizan en palabras, sub-palabras o caracteres, según la estrategia usada. Luego se vectorizan en números y se les dan pesos de importancia/atención, procesándolos de forma no secuencial para intentar entender cuál sería el token más relevante y ajustado de acuerdo al cotexto global de los datos de entrada. Por ejemplo, el prompt es “Cuéntame un chiste sobre IA”. El sistema lo procesa en los tokens “Cuéntame / un / chiste / sobre / IA” (normalmente son un poco más o menos de una palabra). Esos tokens no los procesará de izquierda a derecha, sino que les dará más o menos peso de importancia (“Cuéntame / chiste / IA” seguramente tendrán más peso) y a partir de eso devolverá (en lenguaje natural) los tokens de salida que normalmente tengan más relación con los tokens de entrada. [El análisis de la agencia de protección de datos de Hamburgo](https://datenschutz-hamburg.de/fileadmin/user_upload/HmbBfDI/Datenschutz/Informationen/240715_Discussion_Paper_Hamburg_DPA_KI_Models.pdf) sobre si los LLM incluyen datos personales, analizaba el papel de los tokens como principal elemento informativo a procesar.
