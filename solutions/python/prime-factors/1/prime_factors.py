def factors(value):
    i = 2
    result = []
    while value > 1:
        if value % i == 0:
            value //= i
            result.append(i)
        else:
            i+=1
    return result