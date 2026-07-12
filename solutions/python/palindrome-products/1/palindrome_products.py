
def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    
    best = None
    pairs = []
    for i in range(max_factor, min_factor - 1, -1):
        if best is not None and i * max_factor < best:
            break
        for j in range(max_factor, i - 1, -1):
            number = i * j
            if best is not None and number < best:
                break
            if str(number) == str(number)[::-1]:
                if best is None or number > best:
                    best = number
                    pairs = [(i, j)]
                elif number == best:
                    pairs.append((i, j))
    if best is None:
        return (None, [])
    return (best, pairs)

    
def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    
    best = None
    pairs = []
    for i in range(min_factor, max_factor + 1):
        if best is not None and i * i > best:
            break
        for j in range(i, max_factor + 1):
            number = i * j
            if best is not None and number > best:
                break
            if str(number) == str(number)[::-1]:
                if best is None or number < best:
                    best = number
                    pairs = [(i, j)]
                elif number == best:
                    pairs.append((i, j))
    if best is None:
        return (None, [])
    return (best, pairs)