import re
def abbreviate(words):
    words = words.replace("-", " ")
    clean = re.sub(r"[^a-zA-Z\s]", "", words)
    clean = clean.split()

    result = ""
    for word in clean:
        result += word[0]
    return result.upper()
    
