---
name: lint-glosario
description: Revisión de salud del glosario. Detecta enlaces cruzados rotos o no recíprocos, términos huérfanos sin relaciones, frontmatter incompleto, categorías fuera de taxonomía, definiciones sin fuente, enlaces externos caídos y citas normativas desactualizadas.
---

# /lint-glosario

Chequeo de salud completo. Ejecutar sobre todos los archivos de `terminos/`.

## Comprobaciones

1. **Frontmatter**: campos obligatorios presentes (termino, slug, categorias, relacionados,
   actualizado, estado); slug coincide con el nombre de archivo; categorías dentro de la
   taxonomía cerrada de CLAUDE.md.
2. **Grafo de relaciones**: cada slug en `relacionados` existe; relaciones claramente
   simétricas que no son recíprocas; términos huérfanos (nadie los enlaza y no enlazan a
   nadie); clusters desconectados.
3. **Primera frase**: ¿funciona como definición autónoma? (el build la usa de extracto).
4. **Fuentes**: entradas sin ningún enlace a fuente; enlaces externos rotos (comprobar con
   curl HEAD, tolerando 403 de WAFs conocidos); restos de `?ref=thelegaletters.com`.
5. **Vigencia normativa**: citas a normas o artículos — muestreo con `verificacion-legalize`
   para detectar normas modificadas o derogadas (p. ej. cambios del paquete Ómnibus sobre
   el RIA). Priorizar términos con `actualizado` más antiguo.
6. **Duplicados y contradicciones**: términos que se solapan o definiciones que se
   contradicen entre sí.

## Salida

Informe por severidad (🔴 roto / 🟠 mejorable / 🟡 cosmético) con el archivo y la línea.
Arreglar en el acto lo mecánico (enlaces rotos internos, frontmatter, restos de tracking) e
informar; los cambios de contenido se proponen, no se aplican sin visto bueno.
