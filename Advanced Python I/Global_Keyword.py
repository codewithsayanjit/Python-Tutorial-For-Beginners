# 'global' keyword is used to modify the variable outside of the current scope.

# Global variable
a = 89

def fun():
    # Local variable (different from global a)
    a = 3
    print("Inside function:", a)

fun()

# Global variable remains unchanged
print("Outside function:", a)