
#!/usr/bin/env python3

import argparse
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
    parser = argparse.ArgumentParser(
        description="Genera un SVG da un file D2 e rimuove il primo rect."
    )

    parser.add_argument(
        "input",
        type=Path,
        help="File D2 di input",
    )

    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="File SVG di output (predefinito: stesso nome del file D2)",
    )

    parser.add_argument(
        "--layout",
        choices=["dagre", "elk"],
        default="dagre",
        help="Motore di layout da utilizzare (predefinito: dagre)",
    )

    args = parser.parse_args()

    input_path = args.input

    if not input_path.is_file():
        parser.error(f"file non trovato: {input_path}")

    output_path = args.output or input_path.with_suffix(".svg")

    # Generazione SVG tramite D2
    try:
        subprocess.run(
            [
                "d2",
                "--bundle",
                "--theme=200",
                f"--layout={args.layout}",
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

    print(f"Layout: {args.layout}")
    print(f"D2:     {input_path}")
    print(f"SVG:    {output_path}")


if __name__ == "__main__":
    main()
