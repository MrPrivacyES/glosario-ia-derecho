---
name: publicar
description: Compila el glosario (build.py), verifica la salida generada en docs/, hace commit y push a GitHub para que GitHub Pages redespliegue la web pública del glosario.
---

# /publicar

Publicar el estado actual del glosario en la web.

1. Ejecutar `python3 build.py` desde la raíz del repo.
2. Verificar la salida: `docs/index.html` y `docs/glosario.json` regenerados, número de
   términos publicados coherente con `terminos/` (los `estado: borrador` no cuentan), y
   que el build no reportó errores de parseo.
3. Revisión visual rápida: abrir `docs/index.html` en el navegador integrado y comprobar
   que carga, que el buscador responde y que un término al azar se muestra bien.
4. `git add -A && git commit` con mensaje descriptivo de qué términos cambian
   (p. ej. "Añade 'agente de IA' y actualiza 'riesgo sistémico'").
5. `git push`. GitHub Pages redespliega solo en ~1 minuto.
6. Confirmar a Jorge la URL pública y qué ha cambiado.
