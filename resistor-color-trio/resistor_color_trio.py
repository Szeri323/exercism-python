def label(colors):
    colors_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    value = colors_dict[colors[0]] * 10 + colors_dict[colors[1]]
    multiplier = "0"
    result = str(value)
    if(colors_dict[colors[2]]=="black"):
        result += " ohms"
    elif(colors_dict[colors[2]] == "brown"):
        result += "0 ohms"
    elif(colors_dict[colors[2]] == "red"):
        multiplier *= colors_dict[colors[2]]
    return str(value) + multiplier + ("ohm" if value == 1 else "ohms")

print(label(["orange", "orange", "red"]))
