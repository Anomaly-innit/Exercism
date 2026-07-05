allergies = {
            "eggs" : 1,
            "peanuts" : 2,
            "shellfish" : 4,
            "strawberries" : 8,
            "tomatoes" : 16,
            "chocolate" : 32,
            "pollen" : 64,
            "cats" : 128  
        }

class Allergies:

    def __init__(self, score):
        self.score = score
        
    def allergic_to(self, item):
        self.item = item
        if self.score & allergies[item] != 0:
            return True
        return False
            

    @property
    def lst(self):
        result = []
        for item in allergies:
            if self.score & allergies[item] != 0:
                result.append(item)
        return result