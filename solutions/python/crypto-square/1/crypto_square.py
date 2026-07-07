import re
import math
def cipher_text(plain_text):
    
    text = re.sub(r'[^a-z0-9]', '', plain_text.lower())
    if text == "":
        return ""
        
    c = math.ceil(math.sqrt(len(text)))
    r = math.ceil(len(text) / c)
    padded = text.ljust(r * c)
    rows = []
    
    for i in range(0, len(padded), c):
        rows.append(padded[i:i+c])    
        
    columns = list(zip(*rows))
    chunks = ["".join(col) for col in columns]
    return " ".join(chunks)