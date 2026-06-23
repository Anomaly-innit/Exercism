def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for d in digits:
        if d < 0 or d  >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    total = 0
    for i, number in enumerate(digits):
        total = total +  (number*input_base**(len(digits) - 1 - i))
    result = []
    while total > 0:
        result.append(total % output_base)
        total = total // output_base
    result.reverse()
    if result == []:
        return [0]
    return result
