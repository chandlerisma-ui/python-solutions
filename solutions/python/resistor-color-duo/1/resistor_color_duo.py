COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

def color_code(color):
    return COLORS.index(color)

def colors():
    return COLORS

def value(colors):
    first = color_code(colors[0])
    second = color_code(colors[1])
    return first * 10 + second

