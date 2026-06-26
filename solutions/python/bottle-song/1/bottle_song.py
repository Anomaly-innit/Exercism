def recite(start, take=1):
    count = [("ten", 10),
             ("nine", 9),
             ("eight", 8),
             ("seven", 7),
             ("six", 6),
             ("five", 5),
             ("four", 4),
             ("three", 3),
             ("two", 2),
             ("one", 1),
             ("no", 0)
            ]
    
    result = []
    
    
    for number in range(start, start - take, -1):
            result.extend([f"{count[10 - number][0].title()} green {'bottle' if number == 1 else 'bottles'} hanging on the wall,",
                           f"{count[10 - number][0].title()} green {'bottle' if number == 1 else 'bottles'} hanging on the wall,",
                           f"And if one green bottle should accidentally fall,",
                           f"There'll be {count[11 - number][0] } green {'bottle' if number - 1 == 1 else 'bottles'} hanging on the wall.",
                           ])
            if number != start - take + 1:
                result.append("")
                       
    return result