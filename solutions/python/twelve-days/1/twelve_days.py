def recite(start_verse, end_verse):
    gifts = [
    ("first", "a Partridge in a Pear Tree"),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings"),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth", "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming")
]
    result = []
    
    for verse in range(start_verse, end_verse + 1):  
        expected = ""
        for gift in range(verse, 0, -1): 
            
            if gift == 1 and verse > 1:
                expected += "and " + gifts[0][1]
            elif verse == 1:
                expected += gifts[gift-1][1] 
            else:
                expected += gifts[gift-1][1]  + ", "
                
        result.append(f"On the {gifts[verse-1][0]} day of Christmas my true love gave to me: {expected}.")
    return result
            
        
        
            
