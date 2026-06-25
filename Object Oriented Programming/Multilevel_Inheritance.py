# Multilevel inheritance : When a child class becomes a parent for another child class.

class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o1 = Programmer()
print(o1.a, o1.b)


o2 = Manager()
print(o2.a, o2.b, o2.c)