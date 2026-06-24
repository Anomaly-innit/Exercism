def answer(question):
    words = question.split()
    total = 0
    operation = None
    expecting = "number"
    found_number = False
    for word in words:
        word = word.rstrip('?')
        if word.lstrip('-').isdigit():
            if expecting == "operation":
                raise ValueError("syntax error")
            num = int(word)
            if operation is None:
                total = num
            elif operation == "plus":
                total += num
            elif operation == "minus":
                total -= num
            elif operation == "multiplied":
                total *= num
            elif operation == "divided":
                total /= num
            expecting = "operation"
            found_number = True
        elif word in ("plus", "minus", "multiplied", "divided"):
            if expecting == "number":
                raise ValueError("syntax error")
            operation = word
            expecting = "number"
        elif word in ("What", "is", "by"):
            pass
        else:
            raise ValueError("unknown operation")
    if expecting == "number" and operation != None:
        raise ValueError("syntax error")
    elif found_number == False:
        raise ValueError("syntax error")
    return total
            
        
