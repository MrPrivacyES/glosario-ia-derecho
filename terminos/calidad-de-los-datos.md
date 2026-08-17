---
termino: Calidad de los datos
alias: Data quality
slug: calidad-de-los-datos
categorias: [datos, gobernanza]
relacionados: [precision, gobernanza-de-datos, datos-de-entrenamiento, sesgo]
actualizado: 2026-08-17
estado: publicado
---

Grado en que un conjunto de datos reúne las propiedades necesarias para que el tratamiento alcance su finalidad. La [nota técnica de la AEPD de 21 de julio de 2026](https://www.aepd.es/guias/calidad-datos-inteligencia-artificial.pdf) advierte de que no equivale al principio de exactitud del RGPD: la calidad es un concepto más amplio, que alcanza también a los datos no personales y responde a requisitos ajenos a la protección de datos.

Su aportación más útil es reinterpretar la exactitud del [artículo 5.1.d del RGPD](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02016R0679-20160504) en clave de idoneidad. La exactitud no se agota en la veracidad y la actualización: según la finalidad, puede exigir además un determinado nivel de precisión, granularidad o frecuencia de actualización, y a la inversa, la veracidad y la actualidad solo son exigibles cuando resultan necesarias para esa finalidad, no en todo tratamiento.

De ahí sale un argumento poco explotado. La AEPD sitúa exactitud y minimización como los dos extremos de un mismo rango: la primera fija el mínimo de calidad necesario, y la segunda el máximo, porque el RGPD no legitima tratar datos con una precisión, granularidad o frecuencia que excedan lo necesario. Un conjunto de entrenamiento *excesivamente* fino puede ser ilícito, no solo insuficiente. La Agencia añade dos consecuencias prácticas: en aprendizaje automático la calidad debe medirse en el conjunto y no solo dato a dato, y como no existen tratamientos perfectos, hay que fijar un umbral mínimo aceptable, definir métricas y documentar las debilidades del sistema junto con las salvaguardas que las gestionan.
