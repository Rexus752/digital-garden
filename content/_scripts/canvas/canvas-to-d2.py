# d2 --theme=200 --layout=elk --pad=0 ./content/_scripts/canvas/canvas.d2 

#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


# ============================================================
# Configurazione
# ============================================================

BASE_URL = "https://rexus752.dev"


# ============================================================
# Utility
# ============================================================

def decode(value):
    """Decodifica un valore URL-encoded."""
    return unquote(value)


def normalize_slug(value):
    """
    Trasforma un nome di pagina in uno slug.

    Esempi:

        "Matematica"
        -> "matematica"

        "Algebra lineare"
        -> "algebra-lineare"

        "Teoria degli insiemi"
        -> "teoria-degli-insiemi"
    """

    value = decode(value).strip().lower()

    # Spazi e underscore diventano -
    value = re.sub(r"[\s_]+", "-", value)

    # Mantiene lettere Unicode, numeri e -
    value = re.sub(r"[^\w-]", "-", value, flags=re.UNICODE)

    # Elimina trattini consecutivi
    value = re.sub(r"-+", "-", value)

    # Elimina trattini ai bordi
    value = value.strip("-")

    return value


def page_url(path):
    """
    Converte un path Markdown di Obsidian nell'URL del sito.

    Esempi:

        index.md
        -> https://rexus752.dev

        Matematica.md
        -> https://rexus752.dev/matematica

        Matematica/Algebra/Algebra lineare/Algebra lineare.md
        -> https://rexus752.dev/matematica/algebra/algebra-lineare/algebra-lineare
    """

    path = decode(path).strip()

    # Rimuove eventuale slash iniziale
    path = path.lstrip("/")

    # Rimuove .md
    if path.lower().endswith(".md"):
        path = path[:-3]

    # index.md è la root del sito
    if path.lower() == "index":
        return BASE_URL

    parts = path.split("/")

    parts = [
        normalize_slug(part)
        for part in parts
        if part.strip()
    ]

    return BASE_URL + "/" + "/".join(parts)


def icon_url(path):
    """
    Converte:

        _icons/Matematica.svg

    in:

        https://rexus752.dev/_icons/matematica.svg
    """

    path = decode(path).strip().lstrip("/")

    parts = path.split("/")

    # Normalizziamo solo il nome dell'icona.
    # La directory _icons resta invariata.
    if parts:
        filename = parts[-1]

        stem = Path(filename).stem
        extension = Path(filename).suffix

        stem = normalize_slug(stem)

        parts[-1] = stem + extension.lower()

    return BASE_URL + "/" + "/".join(parts)


# ============================================================
# Parsing dei nodi Markdown
# ============================================================

MARKDOWN_LINK_RE = re.compile(
    r"#\s*\[([^\]]+)\]\(([^)]+)\)"
)


def parse_text_node(text):
    """
    Analizza un nodo Canvas di tipo text.

    Esempio:

        # [Matematica](Matematica.md)

    restituisce:

        {
            "title": "Matematica",
            "path": "Matematica.md"
        }

    Se il testo non contiene un link Markdown restituisce None.
    """

    if not text:
        return None

    match = MARKDOWN_LINK_RE.search(text)

    if not match:
        return None

    title = match.group(1).strip()
    path = match.group(2).strip()

    return {
        "title": title,
        "path": path,
    }


# ============================================================
# Geometria Canvas
# ============================================================

def rectangle(node):
    """
    Restituisce:

        left, top, right, bottom
    """

    x = node.get("x", 0)
    y = node.get("y", 0)

    width = node.get("width", 0)
    height = node.get("height", 0)

    return (
        x,
        y,
        x + width,
        y + height,
    )


def contains(outer, inner):
    """
    Restituisce True se il rettangolo `inner`
    è contenuto interamente in `outer`.
    """

    ox1, oy1, ox2, oy2 = rectangle(outer)
    ix1, iy1, ix2, iy2 = rectangle(inner)

    return (
        ix1 >= ox1
        and iy1 >= oy1
        and ix2 <= ox2
        and iy2 <= oy2
    )


def center(node):
    """Restituisce il centro geometrico di un nodo."""

    x = node.get("x", 0)
    y = node.get("y", 0)

    width = node.get("width", 0)
    height = node.get("height", 0)

    return (
        x + width / 2,
        y + height / 2,
    )


def distance_squared(a, b):
    """Distanza euclidea al quadrato tra i centri di due nodi."""

    ax, ay = center(a)
    bx, by = center(b)

    return (ax - bx) ** 2 + (ay - by) ** 2


# ============================================================
# Costruzione della struttura
# ============================================================

def build_structure(canvas):
    nodes = canvas.get("nodes", [])

    groups = [
        node
        for node in nodes
        if node.get("type") == "group"
    ]

    text_nodes = []
    icon_nodes = []

    for node in nodes:

        if node.get("type") == "text":
            parsed = parse_text_node(node.get("text", ""))

            if parsed is not None:
                text_nodes.append({
                    **node,
                    "title": parsed["title"],
                    "path": parsed["path"],
                })

        elif node.get("type") == "file":
            file = node.get("file", "")

            if file.startswith("_icons/"):
                icon_nodes.append(node)

    return groups, text_nodes, icon_nodes


# ============================================================
# Individuazione dei gruppi
# ============================================================

def find_groups_for_node(node, groups):
    """
    Trova tutti i gruppi che contengono il nodo.

    È possibile che un gruppo sia contenuto in un altro gruppo,
    quindi restituiamo tutti quelli compatibili.
    """

    return [
        group
        for group in groups
        if contains(group, node)
    ]


def smallest_group(groups):
    """
    Se un nodo appartiene a più gruppi, seleziona quello
    con area minore, cioè quello più specifico.
    """

    if not groups:
        return None

    return min(
        groups,
        key=lambda group:
            group.get("width", 0) * group.get("height", 0)
    )


# ============================================================
# Associazione delle icone
# ============================================================

def find_icon_for_node(node, icon_nodes, groups):
    """
    Cerca l'icona associata a un nodo.

    Strategia:

    1. Se l'icona e il nodo appartengono allo stesso gruppo,
       l'icona è candidata.

    2. Se esiste un solo candidato, viene utilizzato.

    3. Se esistono più candidati, viene scelta quella più vicina.

    4. Se non esiste nessuna icona nello stesso gruppo,
       il nodo rimane senza icona.

    Questo evita di assegnare arbitrariamente un'icona
    appartenente ad una zona completamente diversa del Canvas.
    """

    node_groups = find_groups_for_node(node, groups)

    # --------------------------------------------------------
    # Caso 1: nodo dentro un gruppo
    # --------------------------------------------------------

    if node_groups:

        candidates = []

        for icon in icon_nodes:

            icon_groups = find_groups_for_node(icon, groups)

            # Condivide almeno un gruppo
            if any(
                group["id"] in {
                    g["id"] for g in node_groups
                }
                for group in icon_groups
            ):
                candidates.append(icon)

        if len(candidates) == 1:
            return candidates[0]

        if candidates:
            return min(
                candidates,
                key=lambda icon:
                    distance_squared(node, icon)
            )

    # --------------------------------------------------------
    # Caso 2: nessun gruppo
    # --------------------------------------------------------
    #
    # Per i nodi senza gruppo NON prendiamo semplicemente
    # l'icona più vicina.
    #
    # Cerchiamo soltanto un'icona molto vicina e con la stessa
    # altezza/posizione tipica di un accoppiamento icon + text.
    # --------------------------------------------------------

    best_icon = None
    best_distance = float("inf")

    for icon in icon_nodes:

        distance = distance_squared(node, icon)

        # Soglia volutamente conservativa.
        #
        # Nel Canvas normalmente l'icona si trova a poche
        # decine di pixel dal nodo testuale.
        if distance > 120 ** 2:
            continue

        if distance < best_distance:
            best_distance = distance
            best_icon = icon

    return best_icon


# ============================================================
# Generazione D2
# ============================================================

def escape_d2_string(value):
    """
    Escape minimo necessario per una stringa D2 racchiusa
    tra virgolette.
    """

    return value.replace("\\", "\\\\").replace('"', '\\"')


def generate_d2(canvas):
    groups, text_nodes, icon_nodes = build_structure(canvas)

    # --------------------------------------------------------
    # Mappa ID Canvas -> titolo D2
    # --------------------------------------------------------

    node_map = {}

    for node in text_nodes:

        node_map[node["id"]] = {
            "title": node["title"],
            "path": node["path"],
            "link": page_url(node["path"]),
            "icon": None,
        }

    # --------------------------------------------------------
    # Associa icone
    # --------------------------------------------------------

    for node in text_nodes:

        icon = find_icon_for_node(
            node,
            icon_nodes,
            groups,
        )

        if icon is not None:
            node_map[node["id"]]["icon"] = icon_url(
                icon["file"]
            )

    # --------------------------------------------------------
    # Output
    # --------------------------------------------------------

    lines = []

    lines.append("direction: right")
    lines.append("")

    # --------------------------------------------------------
    # Nodi
    # --------------------------------------------------------

    emitted_titles = set()

    for node in text_nodes:

        data = node_map[node["id"]]

        title = data["title"]

        # Se due nodi Canvas rappresentano la stessa pagina,
        # non la dichiariamo due volte.
        if title in emitted_titles:
            continue

        emitted_titles.add(title)

        title_escaped = escape_d2_string(title)

        lines.append(f'"{title_escaped}": {{')

        if data["link"]:
            lines.append(
                f"  link: {data['link']}"
            )

        if data["icon"]:
            lines.append(
                f"  icon: {data['icon']}"
            )

        lines.append("}")
        lines.append("")

    # --------------------------------------------------------
    # Archi
    # --------------------------------------------------------

    edges = canvas.get("edges", [])

    emitted_edges = set()

    for edge in edges:

        from_id = edge.get("fromNode")
        to_id = edge.get("toNode")

        # Ignora archi che non collegano nodi text validi.
        if from_id not in node_map:
            continue

        if to_id not in node_map:
            continue

        from_title = node_map[from_id]["title"]
        to_title = node_map[to_id]["title"]

        edge_key = (
            from_title,
            to_title,
        )

        if edge_key in emitted_edges:
            continue

        emitted_edges.add(edge_key)

        from_escaped = escape_d2_string(from_title)
        to_escaped = escape_d2_string(to_title)

        lines.append(
            f'"{from_escaped}" -> "{to_escaped}"'
        )

    return "\n".join(lines) + "\n"


# ============================================================
# CLI
# ============================================================

def main():

    if len(sys.argv) < 2:
        print(
            f"Uso: {sys.argv[0]} INPUT.canvas [OUTPUT.d2]",
            file=sys.stderr,
        )
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix(".d2")

    # --------------------------------------------------------
    # Lettura Canvas
    # --------------------------------------------------------

    try:
        with input_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            canvas = json.load(file)

    except FileNotFoundError:
        print(
            f"Errore: file non trovato: {input_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    except json.JSONDecodeError as error:
        print(
            f"Errore: JSON non valido:\n{error}",
            file=sys.stderr,
        )
        sys.exit(1)

    # --------------------------------------------------------
    # Conversione
    # --------------------------------------------------------

    d2 = generate_d2(canvas)

    # --------------------------------------------------------
    # Scrittura
    # --------------------------------------------------------

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        file.write(d2)

    print(f"Canvas: {input_path}")
    print(f"D2:     {output_path}")


if __name__ == "__main__":
    main()
