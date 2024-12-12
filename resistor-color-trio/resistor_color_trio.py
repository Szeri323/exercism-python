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

    value = 0
    zeros = 0
    if second != 0:
        value = first * 10 + second
        zeros = third
    else:
        value = first
        zeros = third + 1 
    if value == 0:
        zeros = 0
    number = str(value)
    zeros_str = zeros * "0"
    if zeros > 2:
        number += zeros % 3 * "0"
        if zeros >= 3 and zeros <= 5:
            number += " kilo"
        if zeros >= 6 and zeros <= 8:
            number += " mega"
        if zeros >= 9 and zeros <= 11:
            number += " giga"
    else:
        number += zeros_str + " ohms"
        return number

    number += "ohms"
    return number

