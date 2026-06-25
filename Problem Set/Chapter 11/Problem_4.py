# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

'''
A complex number is written as:    a+bi     
where:
    a = Real part
    b = Imaginary part
    i = √(-1)

Example: 1+2i
Real part = 1, Imaginary part = 2
'''


class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, complex2):
        return Complex(self.r + complex2.r, self.i + complex2.i)
    
    def __mul__(self, complex2):
        real_part = self.r * complex2.r - self.i * complex2.i
        imaginary_part = self.r * complex2.i + self.i * complex2.r
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    # Without __str__, Python would print something like: <__main__.Complex object at 0x...>
        
        
complex1 = Complex(1, 2)
complex2 = Complex(3, 4)
print(complex1  + complex2)
print(complex1 * complex2)