# Registro de fuentes procesadas

Qué término salió de cada fuente. Los documentos archivados en esta carpeta no se
versionan (ver `.gitignore`): el original vive en `Desktop/Claude CoWork/Guias_IA_Autoridades/`.

## 2026-08-16 — EDPB-EDPS Joint Opinion 1/2026 sobre el Ómnibus digital de IA

Fuente: `01_EDPB/EDPB-EDPS_Joint_Opinion_1-2026_Digital_Omnibus_AI_EN.md` (adoptado el 20-1-2026).

| Término | Estado | Referencia en la fuente |
|---|---|---|
| `sistema-de-ia-de-alto-riesgo` | nuevo (borrador) | §§47-51 |
| `autoridad-de-vigilancia-del-mercado` | nuevo (borrador) | §§35-41 |
| `autoridades-de-derechos-fundamentales` | nuevo (borrador) | §§35-41 (art. 77 RIA) |
| `sesgo` | nuevo (borrador) | §§7-16 (art. 10.5 y nuevo art. 4 bis) |
| `clausula-de-anterioridad` | nuevo (borrador) | §49 (art. 111.2 RIA) |
| `consejo-de-ia` | nuevo (borrador) | §29 |

## 2026-08-16 — EDPB-EDPS Dictamen conjunto 5/2021 sobre la propuesta de Reglamento de IA

Fuente: `01_EDPB/EDPB-EDPS_Joint_Opinion_5-2021_AI_Act_ES.md` (adoptado el 18-6-2021).

Aviso: el documento es anterior al texto final y usa terminología superada («usuario» por
«responsable del despliegue», «Ley de IA» por «Reglamento»). Sirve para conceptos y para la
posición de las autoridades, nunca para citas literales del articulado.

| Término | Estado | Referencia en la fuente |
|---|---|---|
| `enfoque-basado-en-el-riesgo` | nuevo (borrador) | §§16-18 |
| `supervision-humana` | nuevo (borrador) | §7 (art. 14 RIA) |
| `evaluacion-de-la-conformidad` | nuevo (borrador) | §§21, 47 |
| `marcado-ce` | nuevo (borrador) | §§21, 47 |
| `persona-afectada` | nuevo (borrador) | §18 («ángulo muerto») |
| `normas-armonizadas` | nuevo (borrador) | §47 |
| `identificacion-biometrica` | actualizado | §§10, 31 |

## 2026-08-16 — EDPB, informe del grupo de trabajo sobre ChatGPT

Fuente: `01_EDPB/EDPB_ChatGPT_Taskforce_Report_EN.md` (23-5-2024).

| Término | Estado | Referencia en la fuente |
|---|---|---|
| `alucinacion` | nuevo (borrador) | §§30-31 (exactitud, art. 5.1.d RGPD) |
| `web-scraping` | nuevo (borrador) | §§15-19 |

### Descartado de estas tres fuentes

Ventanilla única, interés legítimo y su ponderación, EIPD, derechos del interesado: son RGPD
puro, no IA. Pequeña empresa de mediana capitalización (SMC): demasiado nicho.

## 2026-08-16 — AESIA, serie de 16 guías sobre los requisitos del RIA

Fuente: `12_AESIA/AESIA_01` a `AESIA_16`. Una guía por requisito del capítulo III, sección 2,
más la maquinaria de cumplimiento que lo rodea. Publicadas en
https://aesia.digital.gob.es. Valor principal: fijan la terminología oficial en castellano.

| Término | Estado | Guía de origen y artículo del RIA |
|---|---|---|
| `sistema-de-gestion-de-riesgos` | nuevo (borrador) | Guía 05 · art. 9 |
| `gobernanza-de-datos` | nuevo (borrador) | Guía 07 · art. 10 |
| `documentacion-tecnica` | nuevo (borrador) | Guía 15 · arts. 11 y 18, anexo IV |
| `conservacion-de-registros` | nuevo (borrador) | Guía 12 · arts. 12 y 26.6 |
| `transparencia` | nuevo (borrador) | Guía 08 · art. 13 |
| `instrucciones-de-uso` | nuevo (borrador) | Guía 08 · art. 13.2 y 13.3 |
| `explicabilidad` | nuevo (borrador) | Guía 08 · arts. 13.3 y 86 |
| `precision` | nuevo (borrador) | Guía 09 · art. 15 |
| `solidez` | nuevo (borrador) | Guía 10 · art. 15 |
| `ciberseguridad` | nuevo (borrador) | Guía 11 · art. 15.5 |
| `envenenamiento-de-datos` | nuevo (borrador) | Guía 11 · art. 15.5 |
| `ejemplos-adversarios` | nuevo (borrador) | Guía 11 · art. 15.5 |
| `sistema-de-gestion-de-la-calidad` | nuevo (borrador) | Guía 04 · art. 17 |
| `organismo-notificado` | nuevo (borrador) | Guía 03 · art. 3.22 |
| `vigilancia-poscomercializacion` | nuevo (borrador) | Guía 13 · arts. 3.25 y 72 |
| `incidente-grave` | nuevo (borrador) | Guía 14 · arts. 3.49 y 73 |
| `sobreaprendizaje` | nuevo (borrador) | Guía 09 |
| `supervision-humana` | actualizado | Guía 06 · art. 14 |

Hallazgo terminológico: la AESIA titula su guía 06 «Vigilancia humana», mientras que el texto
español del RIA titula el artículo 14 «Supervisión humana». Ambas expresiones circulan como
sinónimas; recogido como alias en el término.

### Descartado de la serie AESIA

Las guías 01, 02 y 16 son introductorias y de checklist: no aportan términos que no estén ya
cubiertos. Se descartan también las métricas concretas de evaluación (F1, balanced accuracy,
matriz de confusión) y el aparato de normas ISO citado: son instrumental técnico que un
abogado no necesita definir, aunque sí reconocer.

## 2026-08-16 — CNIL, 5 documentos y 17 fichas «how-to» sobre IA

Fuente: `04_CNIL/` (fichas publicadas en https://www.cnil.fr, últimas actualizadas el
5-1-2026). Valor principal: es el corpus que mejor articula RGPD y desarrollo de modelos,
y el único que da un método operativo para el anonimato de un modelo.

| Término | Estado | Ficha de origen |
|---|---|---|
| `anonimato-de-los-modelos` | nuevo (borrador) | HowTo 16 + Dictamen 28/2024 del CEPD |
| `memorizacion` | nuevo (borrador) | HowTo 16 |
| `ataques-de-reidentificacion` | nuevo (borrador) | HowTo 16 |
| `medios-razonablemente-utilizables` | nuevo (borrador) | HowTo 16 + cons. 26 RGPD |
| `fase-de-desarrollo` | nuevo (borrador) | HowTo 01 |
| `ajuste-fino` | nuevo (borrador) | HowTo 03 y 16 |
| `aprendizaje-por-transferencia` | nuevo (borrador) | HowTo 03 |
| `anotacion-de-datos` | nuevo (borrador) | HowTo 14 · art. 10.2.c RIA |
| `reutilizacion-de-datos` | nuevo (borrador) | HowTo 03 y 05 · art. 6.4 RGPD |
| `responsable-del-tratamiento` | nuevo (borrador) | HowTo 03 |
| `web-scraping` | actualizado | HowTo 10 |

### Descartado de la serie CNIL

Las fichas 02 (finalidad), 04 y 09 (base jurídica e interés legítimo), 06 (EIPD), 07
(protección desde el diseño), 08 (recogida de datos), 12 (información a los interesados),
13 (ejercicio de derechos) y 15 (seguridad del desarrollo) desarrollan obligaciones del
RGPD aplicadas a la IA, pero no acuñan vocabulario propio: son procedimiento, no términos.
La 11 (modelos de código abierto) queda cubierta por `open-weights` e
`inteligencia-artificial-de-codigo-abierto`. Las síntesis de consultas públicas de 2025 son
recopilaciones de aportaciones de terceros, sin doctrina propia.

## 2026-08-16 — AEPD (12 documentos) y AP Países Bajos (16 documentos)

Fuentes: `03_AEPD/` y `08_AP_PaisesBajos/`. Procesadas juntas porque se complementan: la AEPD
aporta las tecnologías de mejora de la privacidad en castellano; la AP, la delimitación
práctica de las prácticas prohibidas del artículo 5 del RIA a través de sus llamamientos a
aportaciones (Department for the Coordination of Algorithmic Oversight).

| Término | Estado | Fuente |
|---|---|---|
| `practicas-prohibidas` | nuevo (borrador) | AP, llamamientos 1 a 4 · art. 5 RIA |
| `tecnicas-subliminales` | nuevo (borrador) | AP DCA-2024-01 · art. 5.1.a y b |
| `policia-predictiva` | nuevo (borrador) | AP, prohibición D · art. 5.1.d |
| `contenido-intimo-sintetico` | nuevo (borrador) | AEPD, imágenes de terceros · art. 5.1.b bis (Ómnibus) |
| `intervencion-humana-significativa` | nuevo (borrador) | AP, herramientas · art. 22 RGPD |
| `datos-sinteticos` | nuevo (borrador) | AEPD, guía PDPC Singapur |
| `aprendizaje-federado` | nuevo (borrador) | AEPD, TechDispatch |
| `tecnologias-de-mejora-de-la-privacidad` | nuevo (borrador) | AEPD, ambas guías |
| `datos-biometricos` | nuevo (borrador) | arts. 3.34 y 3.36 RIA |
| `social-scoring` | actualizado | AP DCA-2024-03 · art. 5.1.c |
| `sistemas-de-reconocimiento-de-emociones` | actualizado | AP DCA-2024-02 · art. 3.39 |

Hallazgo normativo: el Ómnibus digital de 2026 insertó dos prohibiciones nuevas en el art. 5.1
del RIA —letra b bis, contenido íntimo sintético sin consentimiento, y letra b ter, material
de abuso sexual infantil—, aplicables desde el 2 de diciembre de 2026, con un apartado 1 bis
que acota cuándo alcanzan al desarrollador del sistema.

### Descartado de estas dos series

De la AEPD: la guía de adecuación al RGPD (2020) y la de requisitos de auditorías (2021)
son metodología de cumplimiento, valiosas pero sin vocabulario propio que no esté ya
recogido; la política interna de IA generativa y su anexo son documentos de organización
interna de la propia Agencia; el decálogo «Cuidado con lo que le confIAs» y la infografía son
divulgación ciudadana; «10 malentendidos sobre machine learning» aclara conceptos ya
cubiertos por `aprendizaje-automatico` e `inteligencia-artificial`.

De la AP: los cuatro informes periódicos de riesgos algorítmicos (ARR y RAN, unas 120.000
palabras) son panorámicas de mercado, no fuentes terminológicas; las dos guías de
alfabetización quedan cubiertas por `alfabetizacion-en-materia-de-ia`; la propuesta de espacio
controlado de pruebas neerlandés y el dictamen sobre la estructura de supervisión son
posiciones institucionales nacionales; el documento sobre normas de producto está en
neerlandés y solapa con `normas-armonizadas`.

## 2026-08-16 — SEPD (7), Garante italiano (5) y DSK Alemania (3)

Fuentes: `02_EDPS/`, `07_Garante_Italia/` y `06_DSK_Alemania/`. Procesadas juntas por ser
nichos. Rendimiento bajo en número, como estaba previsto, pero incluye dos huecos de
primer orden que ninguna de las series anteriores había destapado.

| Término | Estado | Fuente |
|---|---|---|
| `ia-generativa` | nuevo (borrador) | SEPD, orientaciones sobre IA generativa |
| `evaluacion-de-impacto-derechos-fundamentales` | nuevo (borrador) | art. 27 RIA |
| `human-in-the-loop` | nuevo (borrador) | Garante, decálogo de IA en sanidad |
| `ciclo-de-vida-del-sistema-de-ia` | nuevo (borrador) | SEPD, guía de gestión de riesgos |
| `retrieval-augmented-generation` | actualizado | DSK, orientación sobre RAG (oct. 2025) |
| `sesgo` | actualizado | SEPD, taxonomía de sesgos |
| `contenido-intimo-sintetico` | actualizado | SEPD, declaración conjunta de 23-2-2026 |

Dos gaps notables que no había detectado ninguna serie anterior: la evaluación de impacto
relativa a los derechos fundamentales del artículo 27 —la única obligación del RIA que pesa
sobre el responsable del despliegue y no sobre el proveedor— y la propia «IA generativa»,
que el glosario usaba sin definir.

### Descartado de estas tres series

Del SEPD: el dictamen conjunto sobre el Ómnibus duplica el ya procesado del CEPD; el
*Compass* 2026-2027 y el informe de mapeo de alto riesgo son planificación institucional
propia del supervisor europeo, sin vocabulario nuevo.

Del Garante: las directrices del Convenio 108 (2019) son anteriores al RIA y a la doctrina
actual; el vademécum sobre deepfakes (2020) queda cubierto por `ultrasuplantacion` y
`contenido-intimo-sintetico`; la nota sobre web scraping e IA generativa (2024) coincide con
lo ya recogido de la CNIL y del CEPD en `web-scraping`. El decálogo de sanidad se aprovechó
solo en `human-in-the-loop`: su grueso es Derecho italiano de protección de datos en el
sector público, no trasladable.

De la DSK: la orientación general sobre IA y protección de datos (2024) es una lista de
comprobación para responsables; la de medidas técnicas y organizativas en sistemas de IA
(2025) desarrolla el artículo 32 del RGPD sin acuñar términos propios. Ambas en alemán.

## 2026-08-16 — ICO Reino Unido (11), APD Bélgica (8) e IMY/Digg Suecia (6)

Fuentes: `09_ICO_ReinoUnido/`, `10_Belgica/` y `11_Suecia/`. Cierra el corpus
`Guias_IA_Autoridades`: las once carpetas quedan procesadas. Rendimiento el más bajo de
todas las tandas, como estaba previsto.

| Término | Estado | Fuente |
|---|---|---|
| `elaboracion-de-perfiles` | nuevo (borrador) | art. 4.4 RGPD · ICO, decisiones automatizadas |
| `decisiones-automatizadas` | nuevo (borrador) | art. 22 RGPD · ICO |
| `explicabilidad` | actualizado | ICO, «Explaining decisions made with AI» |
| `espacio-controlado-de-pruebas-para-la-ia` | actualizado | IMY, informe final de su espacio de protección de datos |

Nota sobre el ICO: es Derecho británico y, tras la Data (Use and Access) Act de 19 de junio
de 2025, su propia guía está en revisión. Se cita solo como referencia metodológica, nunca
como fuente normativa, y así queda advertido en los términos.

Los dos términos nuevos no salen en rigor del ICO sino del RGPD: la serie sirvió para
detectar que el glosario venía citando el artículo 22 en cuatro entradas sin haberlo
definido nunca.

### Descartado de estas tres series

Del ICO: las dos guías extensas (marco de auditoría de IA y guía sobre IA y protección de
datos, unas 90.000 palabras) desarrollan el RGPD británico; la estrategia de IA y biometría,
el enfoque regulador y la respuesta al RIA de 2021 son posición institucional; la política
interna de uso de IA es organización propia del regulador.

De Bélgica: los dos folletos —sistemas de IA y RGPD (2024) e impacto de la IA sobre la
privacidad (2026), cada uno en tres idiomas— son divulgación general que solapa
íntegramente con lo ya recogido de CNIL, AEPD y CEPD. La resolución AFAPDP sobre gobernanza
ética es una declaración de principios.

De Suecia: las directrices de Digg e IMY sobre IA generativa en la Administración quedan
cubiertas por `ia-generativa`; la guía sobre reconocimiento facial y RGPD es una ficha
breve; el resto está en sueco y no aporta vocabulario nuevo.

---

## Estado del corpus

Las once carpetas de `Guias_IA_Autoridades` (123 documentos) quedan procesadas en siete
tandas. Total: 61 términos nuevos y 12 actualizaciones sobre los 58 migrados de Ghost.
