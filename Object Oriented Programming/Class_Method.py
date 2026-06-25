# A class method is a method which is bound to the class and not the object of the class

class Employee:
    a = 1
    
    @classmethod # @classmethod decorator is used to create a class method. cls refers to the class (Employee) Not to the object (e)
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()
print(e.a,)