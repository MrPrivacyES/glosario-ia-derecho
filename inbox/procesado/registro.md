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
