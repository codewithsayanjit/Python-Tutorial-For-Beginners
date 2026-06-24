# Self refers to the instance of the class. It is automatically passed with a function call from an object.

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self): #self refers to the current object (instance) of the class.
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():  #Does not receive self . Cannot access instance attributes directly . Behaves like a normal function inside a class
        print("Good morning")


sayanjit = Employee()
sayanjit.greet()
sayanjit.getInfo() # => Employee.getInfo(sayanjit)
