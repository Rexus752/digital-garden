import re
import os

FOLDER_PATH = "/home/manuel/Manuel/obsidian/digital-garden/content"
OLD_FILES_PATH = "/home/manuel/Manuel/obsidian/digital-garden/private/_formatted"
COLOR_HEADINGS = True

char_dictionary = {
    # LaTeX from ChatGPT
    "\\( ": "$",
    " \\)": "$",
    "\\[": "$$",
    "\\]": "$$",

    "’": "'",
    "′": "'",
    "“": "\"",
    "”": "\"",
    "−": "-",
    "…": "...",
    ". . .": "\\ldots",

    "𝑀": "M",
    "𝑁": "N",

    # Con gli spazi, per evitare di sostituire i caratteri all'interno di una parola
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
    # name: [default_folded?, color]

    # Generici
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

    # Per la matematica
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

    # Per l'informatica
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


def replace_headings_with_tags(f): #? Used to distinguish from other hash marks
    f = f.replace("\n###### ", "\n<h6> ")
    f = f.replace("\n##### ", "\n<h5> ")
    f = f.replace("\n#### ", "\n<h4> ")
    f = f.replace("\n### ", "\n<h3> ")
    f = f.replace("\n## ", "\n<h2> ")
    f = f.replace("\n# ", "\n<h1> ")
    return f


def remove_heading_numbers(f):
    # Separiamo il documento per righe
    lines = f.split("\n")
    result = []
    for line in lines:
        if line.startswith("<h"):
            try:
                line = line[:4] + line.split(" - ", 1)[1:][0]
            except IndexError:
                pass
        result.append(line)
    # Uniamo le righe risultanti
    return '\n'.join(result)


def check_heading_numbers(f, FILE_NAME): # Farla riscrivere da ChatGPT
    f0 = f # Lavoro su una variabile a parte per salvare il file formattato finora
    last_heading = 0 # Inizializzazione del valore dell'ultimo heading visitato
    while True:
        try:
            heading_pos = f0.find("<h") + 2 # Posizione del tag <h*>
            heading = int(f0[heading_pos]) # Estrazione del numero dell'heading
            if heading > last_heading + 1: # Controllo della correttezza dell'heading
                raise Exception(f"heading di livello {heading} non corretto nel file {FILE_NAME}.\n\nContenuto:\n{f0[:heading_pos]}")
            else:
                last_heading = heading
                f0 = f0[heading_pos:]
        except ValueError:
            break


def number_headings(f):
    # Inizializziamo i contatori per tutti gli heading da h1 a h6
    counters = {i: 0 for i in range(1, 7)}
    # Lista che conterrà il risultato
    result = []
    # Separiamo il documento per righe
    lines = f.split("\n")
    for line in lines:
        # Se la riga è vuota, la aggiungiamo solamente al risultato
        if not line:
            result.append(line)
            continue
        # Pattern per riconoscere heading da <h1> a <h6>
        match = re.match(r'<h([1-6])>(.*)', line)
        if match:
            level = int(match.group(1))  # Livello dell'heading (da 1 a 6)
            title = match.group(2).strip()  # Titolo senza il tag HTML
            """
            if title == "Indice": # L'indice non va numerato
                result.append(f"# Indice")
                continue
            if title == "Fonti": # Fonti non va numerato
                result.append(f"# Fonti")
                continue
            """
            # Incrementiamo il contatore corrente per il livello
            counters[level] += 1
            # Reset dei contatori dei livelli inferiori
            for i in range(level + 1, 7):
                counters[i] = 0
            # Costruiamo la numerazione
            numbering = ('#' * level) + ' '
            numbering += '.'.join(str(counters[i]) for i in range(1, level + 1) if counters[i] > 0)
            # Aggiungiamo la linea formattata al risultato
            result.append(f"{numbering} - {title}")
        else:
            # Se non è un heading, aggiungiamo la riga così com'è
            result.append(line)
    # Uniamo le righe risultanti
    return '\n'.join(result)


def refactor_index(f):
    # Rimuoviamo l'indice attuale
    f = re.sub(r"# Indice[\s\S]*?# 1 -", "# Indice\n\n# 1 -", f)
    # Separiamo il documento per righe
    lines = f.split("\n")
    index = [""] # Lista che conterrà l'indice
    for line in lines:
        if line.startswith("#"): # Se la riga è un heading
            if line.startswith("# Indice"): # Non aggiungiamo l'indice all'indice
                continue
            if line.startswith("#include") or line.startswith("#define"): # Non aggiungiamo le macro all'indice
                continue
            # Sostituiamo i cancelletti con i tab e aggiungiamo il grassetto
            line = line.replace("###### ", "\t\t\t\t\t\t- **")
            line = line.replace("##### ", "\t\t\t\t\t- **")
            line = line.replace("#### ", "\t\t\t\t- **")
            line = line.replace("### ", "\t\t\t- **")
            line = line.replace("## ", "\t\t- **")
            line = line.replace("# ", "\t- **")
            line += "**" # Chiudiamo il grassetto
            line = line[1:] # Rimuoviamo il primo tab
            index.append(line)
    index = "\n".join(index)
    new_file = ""
    for line in lines:
        new_file += line + "\n"
        if line.startswith("# Indice"):
            new_file += index + "\n"
    return new_file


def color_callout_titles(f):
    # Separiamo il documento per righe
    lines = f.split("\n")
    result = []
    for line in lines:
        for key in callouts_dict:
            if line.startswith(f"> [!{key}]") and "\\color" not in line:
                line = line.replace(" $", f" $\\color{{#{callouts_dict[key][1][1:]}}} ")
        result.append(line)
    # Uniamo le righe risultanti
    return '\n'.join(result)


if __name__ == '__main__':
    # Deletes the old formatted files
    for root, dirs, files in os.walk("{OLD_FILES_PATH}"):
        for file in files:
            if file.endswith(".md") and file.startswith("OG_"):
                os.remove(os.path.join(root, file))

    # For each file in this folder and subfolders
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            if file.endswith(".md") and not file.startswith("OG_"):
                FILE_PATH = os.path.join(root, file)
                print(f"Formattando il file '{FILE_PATH}'...")

                try:
                    with open(f"{FILE_PATH}", mode='r') as file:
                        content = file.read()
                        FILE_NAME = FILE_PATH.split("/")[-1]
                        with open(f"{OLD_FILES_PATH}/OG_{FILE_NAME}", mode='w') as og_file:
                            # "OG" at the beginning of the old file name for distinguishing in Obsidian file linking
                            og_file.write(content)
                        content = replace_chars(content)
                        if not FILE_NAME.startswith("Quartz") and not FILE_NAME.startswith("Configurazione del mio Giardino Digitale"):
                            content = edit_callouts_folding(content)
                        content = remove_multiple_empty_lines(content)

                        # Heading numbering
                        content = replace_headings_with_tags(content)
                        content = remove_heading_numbers(content)
                        check_heading_numbers(content, FILE_NAME)
                        content = number_headings(content)

                        # Index refactorization
                        # content = refactor_index(content)

                        # Color titles of the callouts
                        content = color_callout_titles(content)

                        # Remove initial "content" in links
                        content = content.replace("(content/", "(")

                        # Removes multiple empty lines at the end of the file
                        while content.endswith("\n\n"):
                            content = content[:-1]

                        with open(f"{FILE_PATH}", mode='w') as new_file:

                            new_file.write(content)

                            print(f"File '{FILE_PATH}' formattato con successo. Il file originale si trova nella cartella '{OLD_FILES_PATH}/'.")
                except FileNotFoundError:
                    print(f"File '{FILE_PATH}' non trovato. Assicurati di aver inserito il percorso correttamente.")
