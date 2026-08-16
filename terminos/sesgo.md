---
termino: Sesgo
alias: Bias
slug: sesgo
categorias: [tecnico, riesgos]
relacionados: [datos-de-entrenamiento, web-scraping, gobernanza-de-datos]
actualizado: 2026-08-16
estado: publicado
---

Desviación sistemática en el comportamiento de un sistema de IA que hace que sus resultados perjudiquen o favorezcan de forma injustificada a determinadas personas o grupos. Puede venir de los datos —conjuntos poco representativos, o que reflejan discriminaciones históricas—, del diseño del modelo o del propio uso, cuando quien lo emplea confía acríticamente en lo que la máquina propone.

El [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02024R1689-20240712) lo trata como un problema de gobernanza de datos: su artículo 10.2 obliga, en los sistemas de alto riesgo, a examinar los posibles sesgos que puedan afectar a la salud y la seguridad, perjudicar derechos fundamentales o dar lugar a discriminación prohibida por el Derecho de la Unión (letra f), y a adoptar medidas para detectarlos, prevenirlos y mitigarlos (letra g). Detectar un sesgo suele exigir tratar precisamente los datos que revelan el origen racial, la salud o la orientación sexual, y ahí surge la paradoja: para comprobar que no discriminas necesitas categorías especiales del artículo 9 del RGPD. El artículo 10.5 lo permitía de forma excepcional y estrictamente necesaria; el [Reglamento (UE) 2026/1744](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32026R1744) lo suprimió y trasladó la regla a un nuevo artículo 4 bis, que la extiende, con las mismas garantías, a los proveedores y responsables del despliegue de cualquier sistema o modelo de IA. El [CEPD y el SEPD](https://www.edpb.europa.eu/documents/legislative-opinion/edpb-edps-joint-opinion-12026-on-the-proposal-for-a-regulation-as_en) advirtieron del riesgo de abuso y pidieron mantener el listón de la estricta necesidad.

Conviene además distinguir de dónde viene, porque la medida correctora cambia. La [guía del SEPD sobre gestión de riesgos](https://www.edps.europa.eu/system/files/2025-11/2025-11-11_ai_risks_management_guidance_en.pdf) separa el sesgo en los datos de entrenamiento —que se corrige con gobernanza de datos y representatividad—, el sesgo algorítmico introducido por el propio diseño del modelo y sus métricas de optimización, y el sesgo de interpretación, que aparece cuando quien recibe el resultado lo lee mal o le atribuye una certeza que no tiene. Este último no se arregla tocando el modelo: se arregla con formación y con supervisión humana efectiva.
