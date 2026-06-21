def steps(number): 
    i = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    while number != 1:
        i += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
    return i