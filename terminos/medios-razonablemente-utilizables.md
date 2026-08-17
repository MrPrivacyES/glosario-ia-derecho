---
termino: Medios razonablemente utilizables
alias: Means reasonably likely to be used
slug: medios-razonablemente-utilizables
categorias: [datos]
relacionados: [anonimato-de-los-modelos, ataques-de-reidentificacion, tecnologias-de-mejora-de-la-privacidad]
actualizado: 2026-08-17
estado: publicado
---

Criterio con el que el Derecho de la Unión decide si un dato está verdaderamente anonimizado. El considerando 26 del RGPD lo formula así: para determinar si una persona es identificable deben tenerse en cuenta todos los medios que razonablemente pueda utilizar el responsable del tratamiento o cualquier otra persona, valorando el coste, el tiempo necesario y la tecnología disponible en el momento del tratamiento y su evolución. Es, por tanto, un estándar relativo y móvil: lo que hoy es anónimo puede dejar de serlo mañana.

Las [Directrices 02/2026 del CEPD sobre anonimización](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf), adoptadas el 7 de julio de 2026 y en consulta pública hasta el 30 de octubre, actualizan el dictamen 05/2014 del Grupo del Artículo 29 y consolidan la lectura **relativa** del criterio tras la [sentencia del Tribunal de Justicia de 4 de septiembre de 2025, SEPD/JUR (C-413/23 P)](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62023CJ0413): un mismo conjunto de datos puede ser personal en manos de una entidad y anónimo en las de otra, de modo que la pregunta útil no es «¿son anónimos?» sino «¿anónimos para quién?». Como prueba, el CEPD propone tres criterios acumulativos —ausencia de aislamiento de registros, de correlación y de inferencia—; si los tres se cumplen, los datos pueden considerarse anónimos con seguridad, y si falla alguno hace falta un análisis adicional.

Aplicado a los modelos de IA, la [CNIL](https://www.cnil.fr/en/analysing-status-ai-model-regard-gdpr) traduce el criterio en factores concretos: la información adicional accesible a quien intente reidentificar, el coste y el tiempo que le exigiría obtenerla, el estado de la técnica en extracción de datos de modelos, y el contexto de despliegue —no es igual un modelo publicado abiertamente que uno interno accesible a unos pocos empleados—.

De ahí se sigue lo que más suele sorprender a quien lo lee por primera vez: el anonimato de un modelo no es una propiedad permanente, sino una conclusión fechada. La CNIL recomienda revisar periódicamente la validez del análisis conforme avance el estado de la técnica y, si una extracción llega a producirse, valorarla como posible brecha de seguridad del artículo 33 del RGPD.
