---
name: vigilancia
description: Vigila las fuentes de referencia de IA y Derecho (RIA y actos de la Comisión, AEPD, EDPB, prensa técnica) en busca de términos nuevos o cambios que obliguen a actualizar términos existentes del glosario. Pensada para ejecutarse también como tarea programada semanal.
---

# /vigilancia

Detectar términos nuevos y actualizaciones necesarias. Diseñada para ejecución manual o
como tarea programada (semanal).

## Fuentes a revisar (por este orden)

1. **Regulación UE**: novedades del Reglamento de IA — actos delegados/de ejecución,
   directrices de la Comisión (AI Office), códigos de buenas prácticas. Buscar en
   digital-strategy.ec.europa.eu y EUR-Lex (truco CELLAR si el WAF bloquea).
2. **España**: AEPD (guías y blog), AESIA, anteproyectos relacionados con IA.
3. **Europa**: EDPB, dictámenes y directrices que toquen IA.
4. **Técnico**: términos nuevos con tracción real (lanzamientos de OpenAI/Anthropic/Google,
   papers muy citados, jerga emergente tipo "vibe coding"). Filtro: solo términos que un
   abogado se vaya a encontrar, no toda novedad técnica.

## Proceso

1. Revisar fuentes y quedarse con candidatos: términos que no están en `terminos/` o
   cambios que dejan obsoleto algo ya publicado (norma modificada, guía nueva, enlace roto).
2. Para cada candidato claro, aplicar el flujo de `/nuevo-termino` con `estado: borrador`.
3. Para actualizaciones de términos existentes, aplicar el cambio, verificar citas con
   `verificacion-legalize` y actualizar `actualizado`.
4. Informe final para Jorge: qué se propone (borradores creados), qué se actualizó, qué se
   descartó y por qué. No publicar en la web: la decisión de pasar borradores a
   `publicado` y ejecutar `/publicar` es de Jorge, salvo que haya dado orden permanente.
