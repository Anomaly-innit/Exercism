def largest_product(series, size):
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if not series.isnumeric():
        raise ValueError("digits input must only contain digits")
    results = []
    for i in range(len(series) - size + 1):
        digits = [int(char) for char in series[i:i+size]]
        product = 1
        for digit in digits:
            product *= digit
        results.append(product)
    return max(results)