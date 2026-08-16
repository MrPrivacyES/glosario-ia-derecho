# Inbox del glosario

Suelta aquí cualquier cosa que pueda dar términos nuevos, y luego ejecuta `/procesar-inbox`:

- **URLs**: un `.md` o `.txt` con uno o varios enlaces (artículos, guías, noticias).
- **Notas rápidas**: "añadir 'agente de IA', salió en las directrices de la Comisión de febrero".
- **Documentos completos**: PDFs de papers, propuestas de norma, leyes, dictámenes, guías.
  Con estos, Claude hace primero *minería*: te propone la lista de términos candidatos
  (con artículo/página de referencia) y solo redacta los que tú elijas.
- **Sugerencias de lectores**: pégalas tal cual.

Todo lo que sale del inbox nace como `estado: borrador`: no se publica en la web hasta que
lo apruebes y ejecutes `/publicar`. Lo procesado se archiva en `inbox/procesado/` con su
registro de qué término salió de cada fuente.
