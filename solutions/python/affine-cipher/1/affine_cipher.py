import re
import math
def encode(plain_text, a, b):
    if math.gcd(a,26) != 1:
        raise ValueError("a and m must be coprime.")
    cleaned_text = re.sub(r"[^a-z0-9]", "", plain_text.lower())
    result = ""
    for char in cleaned_text:
        if char.isdigit():
            result += char
        else:
            i = ord(char) - ord("a")
            l = (a*i + b) % 26
            d = chr(l + ord("a"))
            result += d
    chunks = [result[i:i+5] for i in range(0, len(result), 5)]
    return " ".join(chunks)


def decode(ciphered_text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    cleaned_text = re.sub(r"[^a-z0-9]", "", ciphered_text.lower())
    a_inv = pow(a, -1, 26)
    
    result = ""
    for char in cleaned_text:
        if char.isdigit():
            result += char
        else:
            y = ord(char) - ord("a")
            d = (a_inv * (y - b)) % 26
            result += chr(d + ord("a"))
    return result