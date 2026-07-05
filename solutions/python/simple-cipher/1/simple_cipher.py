import random
import string
class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        self.key = key    
    
    def encode(self, text):
        result = ""
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]
            amount = ord(key_char) - ord("a")
            result += self.shift_letter(char, amount)
        return result
        
    def decode(self, text):
        result = ""
        for i, char in enumerate(text):
            key_char = self.key[i % len(self.key)]
            amount = ord(key_char) - ord("a")
            result += self.shift_letter(char, -amount)
        return result
           
    def shift_letter(self, letter, amount):
        position = ord(letter) - ord("a")
        shifted_position = (position + amount) % 26
        new_letter = chr(shifted_position + ord("a")) 
        return new_letter