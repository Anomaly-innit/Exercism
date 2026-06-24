Plain =  "abcdefghijklmnopqrstuvwxyz"
Cipher = "zyxwvutsrqponmlkjihgfedcba"
def encode(plain_text):
    encoded = ""
    plain_text = plain_text.strip()
    for i, letter in enumerate(plain_text):
        if letter.isalpha():
            index = Plain.find(letter.lower())
            encoded = encoded + Cipher[index]
        elif letter.isdigit():
            encoded = encoded + letter
    groups = []
    for i in range(0, len(encoded), 5):
        groups.append(encoded[i:i+5])
    return " ".join(groups)    

def decode(ciphered_text):
    decoded = ""
    ciphered_text = ciphered_text.strip()
    for letter in ciphered_text:
        if letter.isalpha():
            index = Cipher.find(letter.lower())
            decoded = decoded + Plain[index]
        elif letter.isdigit(): 
            decoded = decoded + letter
    return decoded
        