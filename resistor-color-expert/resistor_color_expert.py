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
        value_1 = colors_dict[colors[0]]
        return f"{value_1} ohms"
    if len(colors) == 4:
        value_1 = colors_dict[colors[0]]
        value_2 = colors_dict[colors[1]]
        multiplier = colors_dict[colors[2]]
        value = (10 * value_1 + value_2) * 10 ** multiplier
        if value_2 == 0 :
            if value >= 1_000_000_000:
                prefix = "giga"
                value //= 1_000_000_000
            elif value >= 1_000_000:
                prefix = "mega"
                value //= 1_000_000 
            elif value >= 1_000:
                prefix = "kilo"
                value //= 1_000
            else:
                prefix = ""
        else:
            if value >= 1_000_000_000:
                prefix = "giga"
                value /= 1_000_000_000
            elif value >= 1_000_000:
                prefix = "mega"
                value /= 1_000_000 
            elif value >= 1_000:
                prefix = "kilo"
                value /= 1_000
            else:
                prefix = ""
        if str(value).endswith(".0"):
            value = str(value).replace(".0", "")
        tolerance = tolerance_dict[colors[3]]
        return f"{value} {prefix}ohms ±{tolerance}%"
    if len(colors) == 5:
        value_1 = colors_dict[colors[0]]
        value_2 = colors_dict[colors[1]]
        value_3 = colors_dict[colors[2]]
        multiplier = colors_dict[colors[3]]
        value = (100 * value_1 + 10 * value_2 + value_3) * 10 ** multiplier
        
        if value_3 == 0 :
            if value >= 1_000_000_000:
                prefix = "giga"
                value //= 1_000_000_000
            elif value >= 1_000_000:
                prefix = "mega"
                value //= 1_000_000 
            elif value >= 1_000:
                prefix = "kilo"
                value //= 1_000
            else:
                prefix = ""
        else:
            if value >= 1_000_000_000:
                prefix = "giga"
                value /= 1_000_000_000
            elif value >= 1_000_000:
                prefix = "mega"
                value /= 1_000_000 
            elif value >= 1_000:
                prefix = "kilo"
                value /= 1_000
            else:
                prefix = ""
        tolerance = tolerance_dict[colors[4]]
        return f"{value} {prefix}ohms ±{tolerance}%"

print(resistor_label(["red", "blue", "red", "green"]))