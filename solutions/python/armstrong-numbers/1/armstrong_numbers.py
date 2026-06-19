def is_armstrong_number(number):
    digit = 0
    count = 0
    sum = 0
    number1 = number
    number2 = number
    while number > 0:
         digit = number % 10 
         number = number // 10
         count += 1
    while number1 > 0:
        digit = number1 % 10 
        number1 = number1 // 10
        sum = sum + digit ** count
    if number2 == sum:
        return True
    else: return False
    
            
