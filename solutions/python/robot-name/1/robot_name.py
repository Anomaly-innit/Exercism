import random
import string
class Robot:
    used_names = set()
    def __init__(self):
        self.generate_name()
    def generate_name(self):
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        digits = ''.join(random.choice(string.digits) for _ in range(3))
        
        while letters + digits in Robot.used_names:
            letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            digits = ''.join(random.choice(string.digits) for _ in range(3))
        
        self.name = letters + digits
        Robot.used_names.add(self.name)

    def reset(self):
        self.generate_name()