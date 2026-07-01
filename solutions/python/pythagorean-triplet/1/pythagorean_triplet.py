def triplets_with_sum(number):
    result = []
    for a in range(1, number // 3): 
        c = ((number - a) + (a**2 / (number - a))) / 2
        b = (number - a) - c

        
        if a < b < c and b == int(b) and c == int(c):
            result.append([int(a),int(b),int(c)])
    return result
                
