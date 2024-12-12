def color_to_number(color):
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
    return colors_dict[color]

def label(colors):
    first = color_to_number(colors[0])
    second = color_to_number(colors[1])
    third = color_to_number(colors[2])

    value = (10 * first + second) * 10 ** third
    if value > 1_000_000_000:
        prefix = "giga"
        value //= 1_000_000_000
    elif value > 1_000_000:
        prefix = "mega"
        value //= 1_000_000 
    elif value > 1_000:
        prefix = "kilo"
        value //= 1_000
    else:
        prefix = ""
    return f"{value} {prefix}ohms"

