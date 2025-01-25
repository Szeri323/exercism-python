def resistor_label(colors):
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
    tolerance_dict = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }
    if len(colors) == 1:
        return f"{colors_dict[colors[0]]} ohms"
    if len(colors) == 2:
        return f"{colors_dict[colors[0]] + colors_dict[colors[1]]} ohms"
    if len(colors) > 3:
        *values, multiplier, tolerance = colors
    else:
        values, multiplier, tolerance = colors
        values = [values]
    val = ""
    prefix = ""
    for value in values:
        val += str(colors_dict[value])
    val = int(val) * 10 ** colors_dict[multiplier]
    
    level = 0

    while val >= 1000:
        val /= 1000
        level += 1
    if level == 1:
        prefix = "kilo"
    elif level == 2:
        prefix = "mega"
    elif level == 3:
        prefix = "giga"
    if val - int(val) == 0:
        val = int(val)
    return f"{val} {prefix}ohms ±{tolerance_dict[tolerance]}%"
