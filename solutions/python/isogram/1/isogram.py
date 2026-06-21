def is_isogram(string):
    i = 0
    string = string.lower()
    
    for char in string:
        count = string.count(char)
        if count > 1 and char != " " and char != "-": 
            return False
        
    return True
        