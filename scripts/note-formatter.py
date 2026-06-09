import re
import os

FOLDER_PATH = "/home/manuel/Manuel/obsidian/digital-garden/content"
COLOR_HEADINGS = True

char_dictionary = {
    # LaTeX from ChatGPT
    "\\( ": "$",
    " \\)": "$",
    "\\[": "$$",
    "\\]": "$$",
    "'": "'",
    "′": "'",
    "\u201c": "\"",
    "\u201d": "\"",
    "−": "-",
    "…": "...",
    ". . .": "\\ldots",
    "𝑀": "M",
    "𝑁": "N",
    "`a ": "à ",
    "`e ": "è ",
    "´e ": "é ",
    "`E ": "È ",
    "´E ": "É ",
    "`i ": "ì ",
    "`ı ": "ì ",
    "`o ": "ò ",
    "`u ": "ù ",
    "¨o": "ö",
    "∈": "\\in",
    "⊆": "\\subseteq",
    "⊊": "\\subsetneq",
    "×": "\\times",
    "∅": "\\emptyset",
    "∁": "\\complement",
    "∪": "\\cup",
    "∩": "\\cap",
    "·": "\\cdot",
    "⊕": "\\oplus",
    "∀": "\\forall",
    "∃": "\\exists",
    "⟨": "\\langle",
    "⟩": "\\rangle",
    "∧": "\\land",
    "¯∧": "\\overline{\\land}",
    "∨": "\\lor",
    "¯∨": "\\overline{\\lor}",
    "¬": "\\lnot",
    "∼": "\\sim",
    "≠": "\\ne",
    "≤": "\\le",
    "≾": "\\precsim",
    "≈": "\\approx",
    "≥": "\\ge",
    "≡": "\\equiv",
    "|=": "\\vDash",
    "→": "\\to",
    "↔": "\\iff",
    "χ": "\\chi"
}

callouts_dict = {
    "premessa": [False, "#FFFFFF"],
    "fonti": [False, "#FFFFFF"],
    "esempio": [True, "#7F7FFF"],
    "osservazione": [False, "#7F7F7F"],
    "trucco": [False, "#FFFFFF"],
    "consiglio": [False, "#3FBFFF"],
    "attenzione": [False, "#FFBF7F"],
    "esercizio": [False, "#FFFFFF"],
    "soluzione": [True, "#7F7F7F"],
    "vantaggi": [False, "#7FFF7F"],
    "svantaggi": [False, "#FF7F7F"],
    "assioma": [False, "#BF7FFF"],
    "definizione": [False, "#FF7FFF"],
    "notazione": [False, "#7FBFFF"],
    "teorema": [False, "#FF3F3F"],
    "proposizione": [False, "#FF7F7F"],
    "lemma": [False, "#FFBFBF"],
    "corollario": [False, "#FFCF7F"],
    "congettura": [False, "#BF3F3F"],
    "dimostrazione": [True, "#7FFF7F"],
    "principio": [False, "#7FFFFF"],
    "proprieta": [False, "#FFFF7F"],
    "algoritmo": [False, "#FF3F3F"],
    "sintassi": [False, "#FFFF7F"]
}

def replace_chars(f):
    for key in char_dictionary:
        f = f.replace(key, char_dictionary[key])
    return f

def edit_callouts_folding(f):
    for key in callouts_dict:
        if callouts_dict[key][0] is True:
            f = f.replace(f"[!{key}] ", f"[!{key}]- ")
            f = f.replace(f"[!{key}]+ ", f"[!{key}]- ")
        elif callouts_dict[key][0] is False:
            f = f.replace(f"[!{key}] ", f"[!{key}]+ ")
            f = f.replace(f"[!{key}]- ", f"[!{key}]+ ")
    return f

def remove_multiple_empty_lines(f):
    while f.find("\n\n\n") != -1:
        f = f.replace("\n\n\n", "\n\n")
    return f

def replace_headings_with_tags(f):
    result = []
    in_code_block = False
    for line in f.split("\n"):
        if line.startswith("```"):
            in_code_block = not in_code_block
        if not in_code_block:
            line = re.sub(r'^#{6} ', '<h6> ', line)
            line = re.sub(r'^#{5} ', '<h5> ', line)
            line = re.sub(r'^#{4} ', '<h4> ', line)
            line = re.sub(r'^#{3} ', '<h3> ', line)
            line = re.sub(r'^#{2} ', '<h2> ', line)
            line = re.sub(r'^#{1} ', '<h1> ', line)
        result.append(line)
    return '\n'.join(result)

def remove_heading_numbers(f):
    lines = f.split("\n")
    result = []
    for line in lines:
        if line.startswith("<h"):
            try:
                line = line[:4] + line.split(" - ", 1)[1:][0]
            except IndexError:
                pass
        result.append(line)
    return '\n'.join(result)

def check_heading_numbers(f, FILE_NAME):
    f0 = f
    last_heading = 0
    while True:
        try:
            heading_pos = f0.find("<h") + 2
            heading = int(f0[heading_pos])
            if heading > last_heading + 1:
                raise Exception(f"heading di livello {heading} non corretto nel file {FILE_NAME}.\n\nContenuto:\n{f0[:heading_pos]}")
            else:
                last_heading = heading
                f0 = f0[heading_pos:]
        except ValueError:
            break

def number_headings(f):
    counters = {i: 0 for i in range(1, 7)}
    result = []
    lines = f.split("\n")
    for line in lines:
        if not line:
            result.append(line)
            continue
        match = re.match(r'<h([1-6])>(.*)', line)
        if match:
            level = int(match.group(1))
            title = match.group(2).strip()
            counters[level] += 1
            for i in range(level + 1, 7):
                counters[i] = 0
            numbering = ('#' * level) + ' '
            numbering += '.'.join(str(counters[i]) for i in range(1, level + 1))
            result.append(f"{numbering} - {title}")
        else:
            result.append(line)
    return '\n'.join(result)

def color_callout_titles(f):
    lines = f.split("\n")
    result = []
    for line in lines:
        for key in callouts_dict:
            if line.startswith(f"> [!{key}]") and "\\color" not in line:
                line = line.replace(" $", f" $\\color{{#{callouts_dict[key][1][1:]}}} ")
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            if file.endswith(".md"):
                FILE_PATH = os.path.join(root, file)
                FILE_NAME = file
                print(f"Formattando il file '{FILE_PATH}'...")
                try:
                    with open(FILE_PATH, mode='r') as f:
                        content = f.read()

                    content = replace_chars(content)

                    if not FILE_NAME.startswith("Quartz") and not FILE_NAME.startswith("Configurazione del mio Giardino Digitale"):
                        content = edit_callouts_folding(content)

                    content = remove_multiple_empty_lines(content)

                    content = replace_headings_with_tags(content)
                    content = remove_heading_numbers(content)
                    check_heading_numbers(content, FILE_NAME)
                    content = number_headings(content)

                    content = color_callout_titles(content)

                    content = content.replace("(content/", "(")

                    while content.endswith("\n\n"):
                        content = content[:-1]

                    with open(FILE_PATH, mode='w') as f:
                        f.write(content)
                    print(f"File '{FILE_PATH}' formattato con successo.")

                except FileNotFoundError:
                    print(f"File '{FILE_PATH}' non trovato.")
                except Exception as e:
                    print(f"Errore nel file '{FILE_PATH}': {e}")
