# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction
        
    def turn_right(self):
        current = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current + 1) % 4]
        
    def turn_left(self):
        current = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current - 1) % 4]
        
    def advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        elif self.direction == SOUTH:
            self.y_pos -= 1
        elif self.direction == EAST:
            self.x_pos += 1
        elif self.direction == WEST:
            self.x_pos -= 1
    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)
    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.turn_right()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "A":
                self.advance()