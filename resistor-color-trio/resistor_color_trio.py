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
    value = 0
    zeros = 0
    if colors_dict[colors[1]] != 0 :
        value = colors_dict[colors[0]] * 10 + colors_dict[colors[1]]
        zeros = colors_dict[colors[2]]
    else:
        value = colors_dict[colors[0]]
        zeros = colors_dict[colors[2]] + 1 
    if value == 0:
        zeros = 0
    number = str(value)
    zeros_str = zeros * "0"
    if zeros > 2:
        if zeros >= 3 and zeros <= 5:
            if zeros == 4:
                number += "0"
            if zeros == 5:
                number += "00"
            number += " kilo"
        if zeros >= 6 and zeros <= 8:
            if zeros == 7:
                number += "0"
            if zeros == 8:
                number += "00"
            number += " mega"
        if zeros >= 9 and zeros <= 11:
            if zeros == 10:
                number += "0"
            if zeros == 11:
                number += "00"
            number += " giga"
    else:
        number += zeros_str + " ohms"
        return number

    number += "ohms"
    return number

print(label(["orange", "orange", "orange"]))
print(label(["red", "black", "red"]))
print(label(["blue", "green", "yellow"]))
print(label(["yellow", "violet", "yellow"]))
