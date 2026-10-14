#!/usr/bin/env python3

import re
import subprocess
import sys
from pathlib import Path


def remove_first_svg_rect(svg_path):
    """Rimuove il primo elemento <rect /> dall'SVG."""

    svg = svg_path.read_text(encoding="utf-8")

    svg, count = re.subn(
        r"<rect\b[^>]*/>",
        "",
        svg,
        count=1,
    )

    if count == 0:
        print(
            f"Avviso: nessun tag <rect /> trovato in {svg_path}",
            file=sys.stderr,
        )
        return

    svg_path.write_text(svg, encoding="utf-8")

    print(f"Rect rimosso: {svg_path}")


def main():
    if len(sys.argv) < 2:
        print(
            f"Uso: {sys.argv[0]} INPUT.d2 [OUTPUT.svg]",
            file=sys.stderr,
        )
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.is_file():
        print(
            f"Errore: file non trovato: {input_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix(".svg")

    # Generazione SVG tramite D2
    try:
        subprocess.run(
            [
                "d2",
                "--bundle",
                "--theme=200",
                "--pad=0",
                "--scale=1",
                str(input_path),
                str(output_path),
            ],
            check=True,
        )
    except subprocess.CalledProcessError as error:
        print(
            f"Errore durante la generazione SVG: {error}",
            file=sys.stderr,
        )
        sys.exit(error.returncode)
    except FileNotFoundError:
        print(
            "Errore: D2 non è installato o non è disponibile nel PATH.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Rimozione del primo rect
    remove_first_svg_rect(output_path)

    print(f"D2:  {input_path}")
    print(f"SVG: {output_path}")


if __name__ == "__main__":
    main()
