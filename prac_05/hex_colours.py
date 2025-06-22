"""
CP1404/CP5632 Practical
Hex colour lookup
"""

COLOUR_NAMES_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


def main():
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        if colour_name in COLOUR_NAMES_TO_HEX:
            print(f"{colour_name} has hex code {COLOUR_NAMES_TO_HEX[colour_name]}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()
