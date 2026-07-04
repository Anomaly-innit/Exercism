import re
class PhoneNumber: 
    def __init__(self, number):
        
        digits = re.sub(r"[\s().+-]", "", number)
        
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if any(c.isalpha() for c in digits):
            raise ValueError("letters not permitted")
        if not digits.isdigit():
            raise ValueError("punctuations not permitted")   
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) == 11:
            if digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            
            digits = digits[1:]   #strip here for 11-digit case
    
    
        if digits[0] == "0":
            raise ValueError("area code cannot start with zero")
        if digits[0] == "1":
            raise ValueError("area code cannot start with one")
        if digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = digits
    @property        
    def area_code(self):
        #number = PhoneNumber("2234567890")
        #self.assertEqual(number.area_code, "223")
        return self.number[:3]

    def pretty(self):
        #number = PhoneNumber("2234567890")
        #self.assertEqual(number.pretty(), "(223)-456-7890")
        pretty = f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
        return pretty
    
         
         