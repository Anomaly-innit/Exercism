def translate_word(word):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
        word = word + "ay"
        return word
    
    elif word[0] in consonants:
        c = 0
        while word[c] in consonants and word[c:c+2] != "qu" and word[c] != "y" :
            c += 1
        if word[c:c+2] == "qu":
            word = word[c+2:] + word[:c+2] + "ay"
        elif word[c:].startswith("y") and c == 0:
            word = word[c+1:] + word[:c] + "y" + "ay"
        else:
            word = word[c:] + word[:c] + "ay"
        return word
        
def translate(text):
    words = text.split()
    results = []
    for word in words:
        translated = translate_word(word)
        results.append(translated)
    return " ".join(results)