YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

numbers = {
    "ONES": 1, "TWOS": 2, "THREES": 3,
    "FOURS": 4, "FIVES": 5, "SIXES": 6
}

def score(dice, category):
    if category in numbers:
        number = numbers[category]
        return number * dice.count(number)
        
    elif category == "CHOICE":
        return sum(dice)
        
    elif category == "FOUR_OF_A_KIND":
        for value in set(dice):
            if dice.count(value) >= 4:
                return value * 4
        return 0
        
    elif category == "FULL_HOUSE":
        counts = [dice.count(value) for value in set(dice)]
        if sorted(counts) == [2, 3]:
            return sum(dice)
        return 0

    elif category == "YACHT":
        counts = [dice.count(value) for value in set(dice)]
        if sorted(counts) == [5]:
            return 50
        return 0
        
    elif category == "LITTLE_STRAIGHT":
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    
    elif category == "BIG_STRAIGHT":
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0