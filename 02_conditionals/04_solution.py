fruit = "Banana"

color = input("Enter the color of banana among green, yellow and brown: ")



if fruit == "Banana":
    if color == "green":
        print("Banana is in UNRIPE")
    elif color == "yellow":
        print("Banana is RIPE")
    elif color == "brown":
        print("Banana is OVERRIPE")
    else:
        print("Invalid color!")