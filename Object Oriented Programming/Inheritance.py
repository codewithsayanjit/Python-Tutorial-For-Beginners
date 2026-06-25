'''
Inheritance is a way of creating a new class from an existing class.

Types Of Inheritance : 

1) Single inheritance : Single inheritance occurs when child class inherits only a single parent class.
2) Multiple inheritance : Multiple Inheritance occurs when the child class inherits from more than one parent classes. 
3) Multilevel inheritance : When a child class becomes a parent for another child class.
'''


class Employee: # Employee is the parent (base) class.
    company = "ITC"

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee): # Child Class
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
a.name = "Rohan"
a.salary = 50000

b = Programmer()
b.name = "Sayanjit"
b.salary = 80000
b.language = "Python"

print(a.company)
print(b.company)

a.show()
b.show() # inherited  # Programmer does not have its own show() method. Python looks in the parent class Employee and finds it.
b.showLanguage()  # own method