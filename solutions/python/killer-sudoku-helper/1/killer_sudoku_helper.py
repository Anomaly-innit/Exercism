from itertools import combinations as itertools_combinations

def combinations(target, size, exclude):
    valid = []
    for combo in itertools_combinations(range(1, 10), size):
        if sum(combo) == target and not any(digit in exclude for digit in combo):
            valid.append(list(combo))
    return valid