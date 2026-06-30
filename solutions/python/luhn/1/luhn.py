class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        result = []
        if len(self.card_num) <= 1:
            return False
        if not self.card_num.isdigit():
            return False
        for i, digit in enumerate(reversed(self.card_num)):
            if i % 2 == 1:
                val = int(digit) * 2
                if val > 9:
                    val -= 9
                result.append(val)
            else:
                result.append(int(digit))

        total = sum(result)      
        if total % 10 == 0:
            return True
        else: 
            return False
            