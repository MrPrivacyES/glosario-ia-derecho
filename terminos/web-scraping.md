---
termino: Web scraping
alias: Rastreo y extracción web
slug: web-scraping
categorias: [datos, tecnico]
relacionados: [datos-de-entrenamiento, sesgo, modelo-de-ia-de-uso-general]
actualizado: 2026-08-16
estado: borrador
---

Recogida y extracción automatizada de información de fuentes accesibles al público en internet, normalmente para construir conjuntos de datos de entrenamiento. Es la forma en que se ha reunido buena parte del material con el que se entrenan los grandes modelos, y el [informe del grupo de trabajo del CEPD sobre ChatGPT](https://www.edpb.europa.eu/system/files/2024-05/edpb_20240523_report_chatgpt_taskforce_en.pdf) usa la expresión para englobar tanto el *scraping* como el *crawling*.

Jurídicamente es terreno resbaladizo. Que un dato esté publicado no lo hace libre: sigue siendo dato personal, y la base jurídica que se invoca —el interés legítimo del artículo 6.1.f del RGPD— exige el triple test de interés legítimo, necesidad y ponderación, tomando en cuenta las expectativas razonables del interesado. Con categorías especiales el listón sube: el CEPD recuerda que la excepción del artículo 9.2.e exige que el interesado haya hecho manifiestamente públicos sus datos mediante un acto afirmativo claro, y la mera accesibilidad no equivale a eso. Como examinar caso por caso es inviable a esa escala, el peso recae en las salvaguardas: criterios de recogida precisos, exclusión de fuentes sensibles, filtrado y borrado o anonimización antes de la fase de entrenamiento. La carga de probar que funcionan es del responsable. La CNIL y el Garante italiano han publicado orientaciones específicas en la misma línea.
