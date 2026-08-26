COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

def color_code(color):
    return COLORS.index(color)

def colors():
    return COLORS

def label(colors):
    giga = 10 ** 9
    mega = 10 ** 6
    kilo = 10 ** 3
    first = color_code(colors[0])
    second = color_code(colors[1])
    third = color_code(colors[2])
    value = (first * 10 + second) * (10 ** third)

    if value >= giga:
        return f"{value//giga} gigaohms"
    elif value >= mega:
        return f"{value//mega} megaohms"
    elif value >= kilo:
        return f"{value//kilo} kiloohms"
    else:
        return f"{value} ohms"


