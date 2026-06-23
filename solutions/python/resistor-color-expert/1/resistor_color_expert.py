def format_number(number):
    if number >= 1000000000:
        value = number / 1000000000
        suffix = "gigaohms"
    elif number >= 1000000:
        value = number / 1000000
        suffix = "megaohms"
    elif number >= 1000:
        value = number / 1000
        suffix = "kiloohms"
    else:
        value = number
        suffix = "ohms"
    
    if value == int(value):
        value = int(value)
    
    return str(value) + " " + suffix
def resistor_label(colors):
    COLORS = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
    TOLERANCE = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
}
    number = 0
    numbe_two = 0
    if len(colors) == 1:
        return "0 ohms"
    elif len(colors) == 4:
        number =  ((COLORS.index(colors[0])*10) + COLORS.index(colors[1])) * 10**COLORS.index(colors[2])
        return format_number(number) + " " + TOLERANCE[colors[-1]]   
    
    elif len(colors) == 5:
        number_two =  ((COLORS.index(colors[0])*100) + (COLORS.index(colors[1])* 10) + (COLORS.index(colors[2]))) * 10**COLORS.index(colors[3])
        return format_number(number_two) + " " + TOLERANCE[colors[-1]]
        
