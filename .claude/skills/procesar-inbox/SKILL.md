---
name: procesar-inbox
description: Vacía la bandeja inbox/ del glosario. Convierte cada URL, nota o sugerencia pendiente en términos nuevos o actualizaciones de términos existentes, siguiendo el mismo flujo que /nuevo-termino, y archiva lo procesado.
---

# /procesar-inbox

Vaciar `inbox/` convirtiendo su contenido en términos del glosario.

1. Listar todo lo que haya en `inbox/` (archivos .md o .txt con URLs, notas, capturas de
   ideas). Ignorar `inbox/README.md`.
2. Para cada elemento, decidir: ¿término nuevo, actualización de uno existente, o
   descartable? Una misma fuente puede alimentar varios términos.
3. Aplicar el flujo de `/nuevo-termino` para cada término resultante (investigar, redactar,
   verificar con `verificacion-legalize`, enlazar bidireccional). Los que surjan del inbox
   nacen como `estado: borrador` salvo instrucción contraria.
4. Mover el archivo procesado a `inbox/procesado/` con la fecha en el nombre
   (`2026-08-16-<nombre>.md`) y anotar dentro qué términos generó.
5. Resumir a Jorge: elementos procesados, términos creados/actualizados, descartes y por qué.
