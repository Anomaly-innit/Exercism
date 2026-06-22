def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in text:
        if letter.islower():
            swap =  alphabet.find(letter)
            swap = alphabet[(swap + key) % 26]
            result = result + swap
        elif letter.isupper():
            letter = letter.lower()
            swap =  alphabet.find(letter)
            swap = alphabet[(swap + key) % 26]
            result = result + swap.upper()
        else:
            result = result + letter       
    return result
       
