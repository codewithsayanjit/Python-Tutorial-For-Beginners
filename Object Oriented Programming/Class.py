'''
Object Oriented Programming : 

Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented programming.
An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.
This concept focuses on using reusable code (DRY (Don't Repeat Yourself) Principle).


Modelling A Problem In OOPS : 

We identify the following in our problem.
1)Noun → Class → Employee
2)Adjective → Attributes → name, age, salary
3)Verbs → Methods → getSalary(), increment()
'''

# A class is a blueprint for creating object.

class Employee: 
    language = "Python" # This is a class attribute. An attribute that belongs to the class rather than a particular object.
    salary = 1200000

sayanjit = Employee()
sayanjit.name = "Sayanjit" # This is an instance attribute.An attribute that belongs to the Instance (object).
print(sayanjit.name, sayanjit.language, sayanjit.salary)

rohan = Employee()
rohan.name = "Rohan Pradhan"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class