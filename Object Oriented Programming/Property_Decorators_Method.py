'''
@property Decorators : ---
Consider the following class:
class Employee:
    @property
    def name(self):
        return self.ename
    
If e = Employee() is an object of class employee, we can print(e.name) to print the ename by internally calling
name() function.

# The method name with '@property' decorator is called getter method.

We can define a function + @ name.setter decorator like below:
@name.setter
def name(self,value):
    self.ename = value
'''


class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property              # @property allows a method to be accessed like an attribute.
    def name(self):      # Getter 
        return f"{self.fname} {self.lname}"

    @name.setter            # This is called automatically when you assign
    def name(self, value):    # Setter
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()

e.a = 45

e.name = "Sayanjit Jana"    # Calls setter automatically

print(e.fname, e.lname)

print(e.name)            # Calls getter automatically

e.show()                 # Class method called