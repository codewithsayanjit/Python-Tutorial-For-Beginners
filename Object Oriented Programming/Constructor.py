'''
__init__() Constructor :

__init__() is a special method which is first run as soon as the object is created.
__init__() method is also known as constructor.
It takes ‘self’ argument and can also take further arguments.
'''

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


sayanjit = Employee("sayanjit", 1300000, "JavaScript") 
# sayanjit.name = "sayanjit"
print(sayanjit.name, sayanjit.salary, sayanjit.language)

rohan = Employee("Rohan", 1000000, "Python")
print(rohan.name, rohan.salary, rohan.language)