import itertools
def drinks_water():
    colors, nationalities, drink, pet, hobby = solve()
    return nationalities[drink.index("water")]


def owns_zebra():
    colors, nationalities, drink, pet, hobby = solve()
    return nationalities[pet.index("zebra")]

def solve():
    colors_list = ["red", "green", "ivory", "yellow", "blue"]
    nationalities_list = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
    drinks_list = ["coffee", "tea", "milk", "orange juice", "water"]
    pets_list = ["dog", "snail", "fox", "horse", "zebra"]
    hobby_list = ["dance", "paint", "reading", "football", "chess"]
    valid_colors = []
    for colors in itertools.permutations(colors_list):
        if any(colors[i] == "green" and colors[i-1] == "ivory" for i in range(1, 5)):
            valid_colors.append(colors)

    valid_combos = []
    for colors in valid_colors:
        for nationalities in itertools.permutations(nationalities_list):
            
            if not (colors.index("red") == nationalities.index("Englishman") and
                    nationalities.index("Norwegian") == 0 and
                    abs(nationalities.index("Norwegian") - colors.index("blue")) == 1):
                continue
                
            for drink in itertools.permutations(drinks_list):
                if (colors.index("green") == drink.index("coffee") and
                        nationalities.index("Ukrainian") == drink.index("tea") and
                        drink.index("milk") == 2):
        
                    for pet in itertools.permutations(pets_list):
                        for hobby in itertools.permutations(hobby_list):
                            if (nationalities.index("Spaniard") == pet.index("dog") and
                                    hobby.index("dance") == pet.index("snail") and
                                    colors.index("yellow") == hobby.index("paint") and
                                    abs(hobby.index("paint") - pet.index("horse")) == 1 and
                                    nationalities.index("Japanese") == hobby.index("chess") and
                                    abs(hobby.index("reading") - pet.index("fox")) == 1 and
                                    hobby.index("football") == drink.index("orange juice")):
                                valid_combos.append((colors, nationalities, drink, pet, hobby))
    return valid_combos[0]

    

    