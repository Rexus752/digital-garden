import re

ICON_NAME = "Informatica a UniTo"

padding = 0.1  # Padding del 10% per lato

icon_path = f"./content/_icons/{ICON_NAME}.svg"

# Conversione delle unità fisiche in pixel CSS.
units = {
    "": 1,
    "px": 1,
    "pt": 96 / 72,
    "pc": 16,
    "mm": 96 / 25.4,
    "cm": 96 / 2.54,
    "in": 96,
}


def parse_length(value):
    """Legge una dimensione SVG e la converte in pixel."""
    match = re.fullmatch(
        r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)"
        r"(?:[eE][+-]?\d+)?)\s*([a-zA-Z]*)\s*",
        value or "",
    )

    if not match:
        raise ValueError(f"Dimensione SVG non valida: {value!r}")

    number = float(match.group(1))
    unit = match.group(2).lower()

    if unit not in units:
        raise ValueError(f"Unità SVG non supportata: {unit!r}")

    return number * units[unit]


with open(icon_path, "r", encoding="utf-8") as svg_file:
    svg = svg_file.read()

# Individua il tag SVG iniziale.
match = re.search(r"<svg\b[^>]*>", svg, re.DOTALL)

if not match:
    raise ValueError("Il file non contiene un tag <svg> valido.")

root_tag = match.group()
content = svg[match.end():]

# Cerca il viewBox originale.
viewbox_match = re.search(
    r'\bviewBox\s*=\s*["\']([^"\']+)["\']',
    root_tag,
    re.IGNORECASE,
)

if viewbox_match:
    # Caso 1: il viewBox è già presente.
    values = re.split(r"[\s,]+", viewbox_match.group(1).strip())

    if len(values) != 4:
        raise ValueError("Il viewBox deve contenere quattro valori.")

    x, y, width, height = map(float, values)

else:
    # Caso 2: il viewBox è assente.
    width_match = re.search(
        r'\bwidth\s*=\s*["\']([^"\']+)["\']',
        root_tag,
        re.IGNORECASE,
    )
    height_match = re.search(
        r'\bheight\s*=\s*["\']([^"\']+)["\']',
        root_tag,
        re.IGNORECASE,
    )

    if not width_match or not height_match:
        raise ValueError(
            "Il file non contiene un viewBox e mancano "
            "width o height per ricavare le dimensioni."
        )

    width = parse_length(width_match.group(1))
    height = parse_length(height_match.group(1))
    x, y = 0, 0

if width <= 0 or height <= 0:
    raise ValueError("Le dimensioni del viewBox devono essere positive.")

if padding < 0:
    raise ValueError("Il padding non può essere negativo.")

# Calcola il nuovo viewBox quadrato.
side = max(width, height) * (1 + 2 * padding)

new_x = x + (width - side) / 2
new_y = y + (height - side) / 2

viewbox = f"{new_x:g} {new_y:g} {side:g} {side:g}"

# Ricostruisce il tag SVG con la formattazione desiderata.
new_svg = (
    '<svg\n'
    '    xmlns="http://www.w3.org/2000/svg"\n'
    f'    viewBox="{viewbox}"\n'
    '    fill="#ffffff"\n'
    '    stroke-width="2"\n'
    '>\n'
    + content
)

with open(icon_path, "w", encoding="utf-8") as new_file:
    new_file.write(new_svg)
