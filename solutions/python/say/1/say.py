ones = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen"
    }
tens = {
    2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }

scales = ["", " thousand", " million", " billion"]

def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"

    chunks = []
    while number > 0:
        chunk = number % 1000       
        chunks.append(chunk)
        number = number // 1000     

    parts = []
    for i, chunk in enumerate(chunks):
        if chunk != 0:
            words = say_under_1000(chunk) + scales[i]
            parts.append(words)
    return " ".join(reversed(parts))
    
def say_under_100(number):    
    result = ""
    if number < 20:
        result += ones[number]
    
    elif number < 100:
        result+=tens[number//10]
        if number % 10 != 0:
            result+="-" + ones[number%10]
    return result       
    
def say_under_1000(number):
    if number < 100:
        return say_under_100(number)
        
    result = ones[number // 100] + " hundred"
    remainder = number % 100
    if remainder != 0:
        result += " " + say_under_100(remainder)
    return result

