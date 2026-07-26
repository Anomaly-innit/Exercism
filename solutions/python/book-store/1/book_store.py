from collections import Counter
def group_price(size):
    discounts = {1: 0, 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25}
    return size * 800 * (1 - discounts[size])

def total(basket):
    counts = Counter(basket)
    groups = []
    while any(c > 0 for c in counts.values()):
        group_size = sum(1 for c in counts.values() if c > 0)

        groups.append(group_size)
        for book in counts:
            if counts[book] > 0:
                counts[book] -= 1
                
    while groups.count(5) > 0 and groups.count(3) > 0:
        groups.remove(5)
        groups.remove(3)
        groups.append(4)
        groups.append(4)
         
    return sum(group_price(g) for g in groups)