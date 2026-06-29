def primes(limit):
    
    
    numbers = list(range(2, limit + 1))  

    for num in numbers:
        
        for multiple in range(num*2, limit+1, num):
            if multiple in numbers:
                numbers.remove(multiple)

    return numbers