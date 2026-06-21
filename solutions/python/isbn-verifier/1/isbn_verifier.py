def is_valid(isbn):
    i = 10
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    sum = 0
    
    for number in isbn:
        if number.isdigit():
            sum += int(number) *  i
            i-=1
        elif isbn.endswith("X"):
            number = 10
            sum += int(number) *  i
            i-=1
        elif isbn.count("X") > 0 and not isbn.endswith("X"):
            return False
        else: return False
    
        
    if sum % 11 == 0:
        return True
    else:
        return False
        
