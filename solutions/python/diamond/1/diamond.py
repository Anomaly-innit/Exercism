def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    max = alphabet.index(letter)
    width = 2 * max + 1
    result = []
    for i in range(max + 1):
        alphabet_letter = alphabet[i]
        if alphabet_letter == "A":
            result.append(" " * max + alphabet_letter + " " * max)
        else :
            result.append(" " * (max-i) +  alphabet_letter + " " * (2*i-1) +  alphabet_letter + " " * (max-i))
    reverse_result = result[:-1][::-1]       
    result = result + reverse_result
    return result
        
    
    
            