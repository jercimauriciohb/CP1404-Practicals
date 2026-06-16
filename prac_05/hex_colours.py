
HEX_COLOURS = {"Absolute Zero": "#0048ba", "Green": "#b0bf1a"}
colour = input("Enter your colour: ").lower()

for key, value in HEX_COLOURS.items():
    if colour == key.lower():
        print(value)
