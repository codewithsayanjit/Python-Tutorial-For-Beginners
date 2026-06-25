# Multiple inheritance : Multiple Inheritance occurs when the child class inherits from more than one parent classes. 

class Employee:
    company = "ITC"
    name = "Sayanjit"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show() # Programmer does not have its own show() method. Python looks in the parent class Employee and Coder finds it.
b.printLanguages() # # Programmer does not have its own printLanguage() method. Python looks in the parent class Employee and Coder then finds it.
b.showLanguage()