COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

TOLERANCE = {"grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%",
             "green": "±0.5%", "brown": "±1%", "red": "±2%",
             "gold": "±5%", "silver": "±10%"}

def color_code(color):
    return COLORS.index(color)

def colors():
    return COLORS

def format_value(val):
    return int(val) if val == int(val) else val

def resistor_label(colors):
    giga = 10 ** 9
    mega = 10 ** 6
    kilo = 10 ** 3

    if len(colors) == 1:
        value = 0
        tol_color = None

    elif len(colors) == 4:
        v1 = color_code(colors[0])
        v2 = color_code(colors[1])
        multiplier = color_code(colors[2])
        tol_color = colors[3]
        value = (v1 * 10 + v2) * (10 ** multiplier)

    elif len(colors) == 5:
        v1 = color_code(colors[0])
        v2 = color_code(colors[1])
        v3 = color_code(colors[2])
        multiplier = color_code(colors[3])
        tol_color = colors[4]
        value = (v1 * 100 + v2 * 10 + v3) * (10 ** multiplier)

    if value >= giga:
        label = f"{format_value(value / giga)} gigaohms"
    elif value >= mega:
        label = f"{format_value(value / mega)} megaohms"
    elif value >= kilo:
        label = f"{format_value(value / kilo)} kiloohms"
    else:
        label = f"{value} ohms"

    if tol_color is None:
        return label
    return f"{label} {TOLERANCE[tol_color]}"