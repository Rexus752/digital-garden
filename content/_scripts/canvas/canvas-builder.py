# d2 --theme=200 --layout=elk --pad=0 ./content/_scripts/canvas/canvas.d2 

import os
from pprint import pprint

with open("./content/_scripts/canvas/_index.canvas") as canvas:
    canvas = canvas.read().split("\n")

    notes = {}
    # Creates notes = {note_name: [note_color]}
    for icon_file in os.scandir("./content/icons"):
        with open(icon_file.path, "r") as icon:
            icon = icon.read()
            try:
                note_color = icon[icon.index("stroke=")+9:icon.index("stroke=")+15]
            except ValueError:
                note_color = icon[icon.index("fill=")+7:icon.index("fill=")+13]
            note_name = icon_file.path[icon_file.path.index("icons")+6:-4]
            notes[note_name] = [note_color]
    with open("./content/index.md") as index:
        note_name = index.read().split("\n")[1][7:]
        note_color = "ffffff"
        notes[note_name] = [note_color]
    print("\nnotes = {note_name: [note_color]}")
    pprint(notes)

    # Creating notes = {note_name: [note_color, icon_id, note_id]}
    for line in canvas:
        if "content/notes" in line:
            note_name = line[line.index('"file":"content')+22:line.index(".md")]
            note_id = line[9:25]
            notes[note_name].append(note_id)
        if "content/index.md" in line:
            with open("./content/index.md") as index:
                note_name = index.read().split("\n")[1][7:]
                note_id = line[9:25]
                notes[note_name].append(note_id)
        if "content/icons" in line:
            icon_id = line[9:25]
            note_name = line[line.index("content/icons")+14:line.index(".svg")]
            notes[note_name].append(icon_id)
    print("\nnotes = {note_name: [note_color, icon_id, note_id]}")
    pprint(notes)

    # Creating dict of note_id_name = {note_id: note_name, icon_id: note_name]}
    note_id_name = {}
    for note in notes:
        note_id_name[notes[note][1]] = note
        try:
            note_id_name[notes[note][2]] = note
        except IndexError:
            continue
    print("\nnote_id_name = {note_id: note_name, icon_id: note_name]}")
    pprint(note_id_name)

    # Creating dict of connections = {note_name: note_name]}
    connections = {}
    for note in notes:
        connections[note] = []
    for line in canvas:
        if "fromNode" in line:
            start_node_id = line[line.index('fromNode')+11:line.index('fromNode')+27]
            end_node_id = line[line.index('toNode')+9:line.index('toNode')+25]
            if start_node_id != '0fef56677fe589d4': # index.md
                start_node = note_id_name[start_node_id] # If this generates an error, change the index.md id
            else:
                with open("./content/index.md") as index:
                    note_name = index.read().split("\n")[1][7:]
                    start_node = note_name
                    connections[note_name] = []
            end_node = note_id_name[end_node_id]
            connections[start_node].append(end_node)
    print("\nconnections = {note_name: note_name]}")
    pprint(connections)

    with open("./content/scripts/canvas/canvas.d2", "w") as d2_file:
        d2 = "direction: right\n\n"
        with open("./content/index.md") as index:
            index_note_name = index.read().split("\n")[1][7:]
        for note in connections:
            note_name = note
            if note_name == index_note_name:
                note_link = f"https://rexus752.github.io/digital-garden"
                note_color = "#7f7f7f"
                note_connections = ""
                for connected_note in connections[note]:
                    note_connections += f'\n"{note}" -> "{connected_note}"'
                d2 += f'''"{note_name}": {{
  link: {note_link}
}}{note_connections}\n\n'''
            else:
                note_link = note_name.replace(" ", "-")
                note_icon = f"https://rexus752.github.io/digital-garden/icons/{note_link}.svg"
                note_link = f"https://rexus752.github.io/digital-garden/notes/{note_link}"
                note_color = f"#{notes[note][0]}"
                note_connections = ""
                for connected_note in connections[note]:
                    note_connections += f'\n"{note}" -> "{connected_note}"'
                d2 += f'''"{note_name}": {{
  link: {note_link}
  icon: {note_icon}
}}{note_connections}\n\n'''
        d2_file.write(d2)
