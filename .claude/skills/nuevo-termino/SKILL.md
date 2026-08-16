---
name: nuevo-termino
description: Añade un término nuevo al glosario a partir de un nombre o de una URL fuente. Redacta la entrada según la línea editorial, verifica las citas normativas con Legalize, crea los enlaces cruzados en ambas direcciones y deja el término listo para publicar.
---

# /nuevo-termino <término | URL>

Añadir una entrada al glosario. Pasos, en orden:

1. **Comprobar duplicados**: buscar en `terminos/` por nombre, alias y sinónimos. Si ya
   existe, proponer actualizarlo en lugar de duplicar.
2. **Investigar**: si el argumento es una URL, leerla como fuente principal. Si es solo un
   nombre, buscar la definición legal oficial primero (RIA, RGPD, guías AEPD/EDPB/Comisión)
   y después fuentes técnicas solventes. Buscar en web lo que haga falta.
3. **Redactar** siguiendo el formato y las reglas de CLAUDE.md: primera frase = definición
   autónoma; después relevancia jurídica; fuentes enlazadas inline; 80-250 palabras;
   frontmatter completo con categorías de la taxonomía cerrada.
4. **Verificar citas normativas** con la skill `verificacion-legalize` antes de dar el
   texto por bueno. Corregir cualquier discrepancia.
5. **Enlazar**: elegir 2-4 `relacionados` que existan en `terminos/`, y añadir el nuevo
   slug a los `relacionados` de esos términos cuando la relación sea simétrica.
6. **Estado**: `publicado` si lo pide Jorge directamente; `borrador` si surge de vigilancia
   o de terceros.
7. Mostrar la entrada completa a Jorge y recordarle que `/publicar` la sube a la web.
