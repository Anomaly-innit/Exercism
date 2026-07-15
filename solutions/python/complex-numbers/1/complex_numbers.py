import math
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_part, imaginary_part)
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return other.__sub__(self)
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        real_part = (self.real*other.real + self.imaginary*other.imaginary) / (other.real**2 + other.imaginary**2)
        imaginary_part = (self.imaginary*other.real - self.real*other.imaginary) / (other.real**2 + other.imaginary**2)    
        return ComplexNumber(real_part , imaginary_part)
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return other.__truediv__(self)
    
    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        factor = math.exp(self.real)
        real_part = factor * math.cos(self.imaginary)
        imaginary_part = factor * math.sin(self.imaginary)
        return ComplexNumber(real_part, imaginary_part)
