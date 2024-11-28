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
    multiplier = colors_dict[colors[2]] * '0'
    return str(value) + multiplier

print(label(["orange", "orange", "orange"]))
