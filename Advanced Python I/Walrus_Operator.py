# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression.

# Using walrus operator 
if (n := len([1, 2, 3, 4, 7])) > 3:     # Think of := as "assign and return the value at the same time."
    print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)
    
 # Using Without walrus operator    
n = len([1, 2, 3, 4, 7])

if n > 3:
    print(f"List is too long ({n} elements, expected <= 3)")