def square_of_sum(number):
    result = []
    for digit in range(1,number+1):
        result.append(digit)
    count = (sum(result)**2)
    return count


def sum_of_squares(number):
    result = []
    for digit in range(1, number+1):
        result.append(digit**2)
    return sum(result)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
