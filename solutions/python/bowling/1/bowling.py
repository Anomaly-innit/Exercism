class BowlingGame:
    def __init__(self): 
        self.rolls = []
        self.frame_number = 1
        self.frame_rolls = []
        self.game_over = False
        
    def roll(self, pins):
        if self.game_over:
            raise IndexError("cannot roll after game is over")
        if pins < 0 or pins > 10:
            raise ValueError("invalid number of pins")
    
        if self.frame_number < 10:
            if len(self.frame_rolls) == 1 and self.frame_rolls[0] + pins > 10:
                raise ValueError("two rolls in a frame cannot exceed 10")
                
            self.frame_rolls.append(pins)
            self.rolls.append(pins)
            
            if pins == 10 or len(self.frame_rolls) == 2:
                self.frame_number += 1
                self.frame_rolls = []
                 
        else:  # frame_number == 10
            if len(self.frame_rolls) == 1:
                first = self.frame_rolls[0]
                if first != 10 and first + pins > 10:
                    raise ValueError("two rolls in a frame cannot exceed 10")
            elif len(self.frame_rolls) == 2:
                first, second = self.frame_rolls
                if first == 10 and second != 10 and second + pins > 10:
                    raise ValueError("two rolls after a strike in the tenth frame cannot exceed 10")
        
            self.frame_rolls.append(pins)
            self.rolls.append(pins)
        
            if len(self.frame_rolls) == 2:
                first, second = self.frame_rolls
                if first != 10 and first + second < 10:
                    self.game_over = True
            elif len(self.frame_rolls) == 3:
                self.game_over = True   
                    
    def score(self):
        total = 0
        i = 0
        for frame in range(10):
            if self.rolls[i] == 10:
                total += 10 + self.rolls[i+1] + self.rolls[i+2]
                i +=1
            elif self.rolls[i] + self.rolls[i+1] == 10:
                total += 10 + self.rolls[i+2]
                i += 2
            else:
                total += self.rolls[i] + self.rolls[i+1]
                i += 2
        return total
