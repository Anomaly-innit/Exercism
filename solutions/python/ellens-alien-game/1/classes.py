"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created = 0
    
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1
        
    def hit(self):        
        self.health -= 1
        
    def is_alive(self):   
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
        
    def collision_detection(self,other):
        pass
    
def new_aliens_collection(positions):
    return [Alien(x, y) for x, y in positions]
        



         