# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j) ## super() method is used to access the methods of a super class in the derived class. __init__() Calls constructor of the base class
#            OR       
#       self.i = i
#       self.j = j
#       self.k = k
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()