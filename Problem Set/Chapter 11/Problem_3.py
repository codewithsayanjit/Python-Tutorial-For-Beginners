# Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    # Class attributes
    salary = 234
    increment = 20

    # Getter method using @property
    @property       # Python automatically calls this getter method.
    def salaryAfterIncrement(self):
        # Formula:
        # New Salary = Salary + (Salary × Increment %)
        return self.salary + self.salary * (self.increment / 100)

    # Setter method using @property.setter
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Formula:
        # Increment % = ((New Salary / Old Salary) - 1) × 100
        self.increment = ((new_salary / self.salary) - 1) * 100        


# Create object
e = Employee()

# Check current salary after 20% increment
print("Salary After Increment:", e.salaryAfterIncrement)

# Set a new salary after increment
e.salaryAfterIncrement = 280.8

# Print the new increment percentage
print(f"New Increment Percentage: {e.increment:.2f}%") 