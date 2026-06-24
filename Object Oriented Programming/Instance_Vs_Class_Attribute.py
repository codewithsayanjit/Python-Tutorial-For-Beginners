# An attribute that belongs to the Instance (object).

class Employee: 
    language = "Python" # This is a class attribute.An attribute that belongs to the class rather than a particular object.
    salary = 1200000


sayanjit = Employee()
sayanjit.name = "Sayanjit"
sayanjit.language = "JavaScript" # This is an instance attribute.An attribute that belongs to the Instance (object).
# Note: Instance attributes take preference over class attributes during assignment & retrieval.
print(sayanjit.name,sayanjit.language, sayanjit.salary)