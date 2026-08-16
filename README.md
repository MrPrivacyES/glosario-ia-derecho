# Glosario sobre IA y Derecho

Glosario vivo de términos sobre inteligencia artificial y Derecho, un proyecto de
[The Legal Letters](https://www.thelegaletters.com). Mantenido con Claude Code siguiendo el
modelo de "LLM wiki" de Karpathy: los archivos Markdown de `terminos/` son la fuente de
verdad y Claude actúa como redactor y mantenedor según las reglas de [CLAUDE.md](CLAUDE.md).

**Web pública:** https://glosario.thelegaletters.com (GitHub Pages, servida desde `docs/`).

## Cómo funciona

| Comando | Qué hace |
|---|---|
| `/nuevo-termino <término o URL>` | Redacta una entrada nueva, verifica citas y crea enlaces cruzados |
| `/procesar-inbox` | Convierte las URLs y notas de `inbox/` en términos |
| `/vigilancia` | Revisa fuentes (Comisión, AEPD, EDPB…) y propone términos o actualizaciones |
| `/lint-glosario` | Salud del glosario: enlaces rotos, huérfanos, citas desactualizadas |
| `/publicar` | Compila con `build.py`, commit y push → la web se redespliega sola |

## Publicar a mano

```bash
python3 build.py && git add -A && git commit -m "Actualiza glosario" && git push
```

`build.py` no tiene dependencias (solo stdlib de Python 3). Genera:

- `docs/index.html` — web interactiva autocontenida (buscador, filtros, enlaces cruzados)
- `docs/glosario.json` — datos abiertos reutilizables (CC BY 4.0)

## Licencia

Contenido bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es).
© Jorge Morell Ramos.
