#!/usr/bin/env python3
"""Compila terminos/*.md a docs/index.html (web interactiva) + docs/glosario.json (datos abiertos).

Sin dependencias externas: solo stdlib. Ejecutar desde la raíz del repo:
    python3 build.py
"""
import json, os, re, sys, html, datetime, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "terminos")
OUT = os.path.join(ROOT, "docs")

CATEGORIAS = {
    "ria": "Reglamento IA",
    "tecnico": "Técnico",
    "actores": "Actores y roles",
    "datos": "Datos y privacidad",
    "biometria": "Biometría",
    "riesgos": "Riesgos y seguridad",
    "gobernanza": "Gobernanza",
    "cultura": "Cultura IA",
}

def parse_frontmatter(text, fname):
    m = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    if not m:
        sys.exit(f"ERROR: {fname} no tiene frontmatter")
    fm, body = {}, text[m.end():].strip()
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        fm[k.strip()] = v
    return fm, body

def md_to_html(md):
    """Markdown mínimo: enlaces, negrita, cursiva, párrafos."""
    def esc(s):
        return html.escape(s, quote=False)
    out, pos, parts = [], 0, []
    # proteger enlaces primero
    tokens = []
    def link_sub(m):
        tokens.append((m.group(1), m.group(2)))
        return f"\x00{len(tokens)-1}\x00"
    md = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link_sub, md)
    md = esc(md)
    md = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", md)
    md = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", md)
    def link_back(m):
        txt, url = tokens[int(m.group(1))]
        txt = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", esc(txt))
        return f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{txt}</a>'
    md = re.sub(r"\x00(\d+)\x00", link_back, md)
    paras = [p.strip() for p in md.split("\n\n") if p.strip()]
    html_out = "".join(f"<p>{p}</p>" for p in paras)
    # capitalizar la primera letra visible (las definiciones migradas seguían a "Término:")
    return re.sub(r"^(<p>(?:<[^>]+>)*)([a-záéíóúü])", lambda m: m.group(1) + m.group(2).upper(), html_out)

def first_sentence(md):
    """Primera frase del cuerpo, sin markdown, como extracto."""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)
    text = re.sub(r"\*+", "", text).strip()
    m = re.search(r"^(.*?[.!?])(\s|$)", text, re.S)
    s = (m.group(1) if m else text).strip().replace("\n", " ")
    s = s[:1].upper() + s[1:]
    return s if len(s) <= 320 else s[:317].rsplit(" ", 1)[0] + "…"

def normaliza(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s.lower()) if not unicodedata.combining(c))

def main():
    terms, borradores = [], 0
    for fname in sorted(os.listdir(SRC)):
        if not fname.endswith(".md"):
            continue
        fm, body = parse_frontmatter(open(os.path.join(SRC, fname), encoding="utf-8").read(), fname)
        for req in ("termino", "slug", "categorias", "relacionados", "actualizado"):
            if req not in fm:
                sys.exit(f"ERROR: {fname} sin campo '{req}'")
        if fm.get("estado", "publicado") != "publicado":
            borradores += 1
            continue
        if fm["slug"] != fname[:-3]:
            sys.exit(f"ERROR: slug '{fm['slug']}' no coincide con archivo {fname}")
        for c in fm["categorias"]:
            if c not in CATEGORIAS:
                sys.exit(f"ERROR: {fname} categoría desconocida '{c}'")
        terms.append({
            "termino": fm["termino"],
            "alias": fm.get("alias", ""),
            "slug": fm["slug"],
            "categorias": fm["categorias"],
            "relacionados": fm["relacionados"],
            "actualizado": fm["actualizado"],
            "extracto": first_sentence(body),
            "html": md_to_html(body),
            "buscar": normaliza(fm["termino"] + " " + fm.get("alias", "") + " " + body),
        })

    slugs = {t["slug"] for t in terms}
    for t in terms:
        rotos = [r for r in t["relacionados"] if r not in slugs]
        if rotos:
            print(f"AVISO: {t['slug']} tiene relacionados inexistentes o en borrador: {rotos}")
        t["relacionados"] = [r for r in t["relacionados"] if r in slugs]

    terms.sort(key=lambda t: normaliza(t["termino"]))
    os.makedirs(OUT, exist_ok=True)
    hoy = datetime.date.today().isoformat()

    # datos abiertos (sin campo de búsqueda ni html)
    abierto = [{k: t[k] for k in ("termino", "alias", "slug", "categorias", "relacionados", "actualizado", "extracto")} for t in terms]
    with open(os.path.join(OUT, "glosario.json"), "w", encoding="utf-8") as f:
        json.dump({"titulo": "Glosario sobre IA y Derecho — The Legal Letters",
                   "url": "https://glosario.thelegaletters.com",
                   "licencia": "CC BY 4.0",
                   "generado": hoy, "terminos": abierto}, f, ensure_ascii=False, indent=1)

    tpl = open(os.path.join(ROOT, "plantilla.html"), encoding="utf-8").read()
    page = (tpl.replace("__DATA__", json.dumps(terms, ensure_ascii=False))
               .replace("__CATS__", json.dumps(CATEGORIAS, ensure_ascii=False))
               .replace("__COUNT__", str(len(terms)))
               .replace("__FECHA__", hoy))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)

    print(f"OK: {len(terms)} términos publicados ({borradores} en borrador) → docs/index.html + docs/glosario.json")

if __name__ == "__main__":
    main()
