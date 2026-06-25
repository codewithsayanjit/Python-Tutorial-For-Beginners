'''
Operators in Python can be overloaded using dunder methods. These methods are called when a given operator is used on the objects.

Operators in Python can be overloaded using the following methods:
                p1+p2   # p1.__add__(p2)
                p1-p2   # p1.__sub__(p2)
                p1*p2   # p1.__mul__(p2)
                p1/p2   # p1.__truediv__(p2)
                p1//p2  # p1.__floordiv__(p2)
Other dunder/magic methods in Python:
                __str__() # used to set what gets displayed upon calling str(obj)
                __len__() # used to set what gets displayed upon calling len(obj)
'''

# Operator overloading allows us to define how operators
# (+, -, *, ==, etc.) behave for objects of a class.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator using __add__()
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the - operator using __sub__()
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overloading the * operator using __mul__()
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    # Overloading the == operator using __eq__()
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading the str() function using __str__()
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Creating objects
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Using overloaded operators
print("v1 =", v1)              # Calls __str__()
print("v2 =", v2)              # Calls __str__()

print("v1 + v2 =", v1 + v2)    # Calls __add__()
print("v1 - v2 =", v1 - v2)    # Calls __sub__()
print("v1 * v2 =", v1 * v2)    # Calls __mul__()

print("v1 == v2 :", v1 == v2)  # Calls __eq__()

v3 = Vector(2, 3)
print("v1 == v3 :", v1 == v3)  # True