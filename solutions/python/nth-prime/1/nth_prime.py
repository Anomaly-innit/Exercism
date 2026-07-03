def prime(number):
    if number <= 0:
        raise ValueError("there is no zeroth prime")
    count = 0
    i = 1
    result = 0
    while count < number:
        i+=1
        if is_prime(i):
            count += 1
    result +=i
    return result
    
def is_prime(num):
    prime = True
    for digit in range(2, int(num**0.5) + 1):
        if num % digit == 0:
            prime = False
            return prime
    return True