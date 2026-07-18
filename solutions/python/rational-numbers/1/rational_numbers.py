import math
class Rational:
    def __init__(self, numer, denom):
        g = math.gcd(numer, denom)
        numer = numer // g
        denom = denom // g
        if denom < 0:
            numer = -numer
            denom = -denom
        self.numer = numer
        self.denom = denom
    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom =  self.denom * other.denom
        return Rational(numer, denom)
        
    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)
        
    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                numer = self.numer ** power
                denom = self.denom ** power
            else:
                m = abs(power)
                numer = self.denom ** m
                denom = self.numer ** m
            return Rational(numer, denom)
        else:
            return (self.numer ** power) / (self.denom ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)