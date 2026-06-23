def label(colors):
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
    number = 0
    if len(colors) > 2:
        number =  ((COLORS.index(colors[0])*10) + COLORS.index(colors[1])) * 10**COLORS.index(colors[2])
        if number < 1000:
            return str(number) + " ohms"
        elif 1000000 > number >= 1000 :
            return str(number // 1000) + " kiloohms"
        elif 1000000000 > number >= 1000000:
            return str(number // 1000000) + " megaohms"
        elif number >= 1000000000:
            return str(number // 1000000000) + " gigaohms"
    else:
        return (COLORS.index(colors[0])*10) + COLORS.index(colors[1])
