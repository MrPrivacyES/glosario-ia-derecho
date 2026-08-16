---
name: procesar-inbox
description: Vacía la bandeja inbox/ del glosario. Convierte URLs, notas, PDFs, papers, propuestas de norma o leyes pendientes en términos nuevos o actualizaciones, siguiendo el mismo flujo que /nuevo-termino. Para documentos largos, primero extrae y propone una lista de términos candidatos ("minería") antes de redactar.
---

# /procesar-inbox

Vaciar `inbox/` convirtiendo su contenido en términos del glosario.

1. Listar todo lo que haya en `inbox/`: archivos `.md`/`.txt` con URLs o notas, y también
   documentos completos — PDFs de papers, guías, informes, propuestas de norma, leyes,
   dictámenes. Ignorar `inbox/README.md` y `inbox/procesado/`.

2. **Elementos cortos** (una URL, una nota, una sugerencia): decidir si dan término nuevo,
   actualización de uno existente, o se descartan. Una misma fuente puede alimentar varios
   términos.

3. **Documentos largos** (PDF, paper, propuesta de norma, ley): modo minería —
   a. Leer el documento entero (skill pdf si hace falta; los muy largos, por partes).
   b. Extraer **términos candidatos**: conceptos definidos en el propio texto (en normas,
      mirar siempre el artículo de definiciones), términos técnicos o jurídicos nuevos con
      recorrido, y términos ya publicados cuya definición el documento cambia o matiza.
      Filtro editorial: solo lo que un abogado se vaya a encontrar; no toda palabra nueva.
   c. Presentar a Jorge la lista de candidatos con una línea de justificación y la
      referencia (artículo/página) cada uno, y **esperar su selección** antes de redactar
      — salvo que haya pedido procesado directo, en cuyo caso redactar los claros y
      señalar los dudosos.

4. Para cada término aprobado, aplicar el flujo de `/nuevo-termino` (investigar, redactar,
   verificar con `verificacion-legalize`, enlazar bidireccional). Los que surjan del inbox
   nacen como `estado: borrador` salvo instrucción contraria. Si la fuente es una
   *propuesta* de norma aún no aprobada, decirlo expresamente en la entrada («según la
   propuesta de…, pendiente de aprobación»).

5. Mover el archivo procesado a `inbox/procesado/` con la fecha en el nombre
   (`2026-08-16-<nombre>.ext`) y registrar en `inbox/procesado/registro.md` qué términos
   generó cada fuente.

6. Resumir a Jorge: elementos procesados, términos creados/actualizados, descartes y por qué.
