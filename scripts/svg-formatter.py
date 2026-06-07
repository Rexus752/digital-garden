from pprint import pprint

icon_name = "Infiniti e infinitesimi"

with open(f"./content/_icons/{icon_name}.svg") as svg:
    svg = svg.read().split("<")
    new_svg = f'<svg\n    xmlns="http://www.w3.org/2000/svg"\n    viewBox="0 0 640 640"\n    fill="#ffffff"\n  stroke-width="2"\n>\n    <{svg[2]}\n    <{svg[3]}\n<{svg[4]}'
    with open(f"./content/_icons/{icon_name}.svg", "w") as new_file:
        new_file.write(new_svg)