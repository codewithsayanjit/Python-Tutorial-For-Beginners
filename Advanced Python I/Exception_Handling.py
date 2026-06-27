#  There are many built-in exceptions which are raised in python when something goes wrong.

# try-except is used for Exception Handling.
# It prevents the program from crashing when an error occurs.

try:
    # Take input from the user and convert it to an integer
    a = int(input("Hey, Enter a number: "))

    # If conversion is successful, print the number
    print(a)

# This block runs only if a ValueError occurs
# ValueError happens when int() cannot convert the input . Example: "abc", "hello", "12.5"
except ValueError as v:  # We can raise custom exceptions using the raise keyword in python
    print("Heyyyy")      # Custom error message
    print(v)             # Prints the actual error message

# This block catches any other exception
# that is not handled by the previous except block
except Exception as e:
    print(e)

# This statement runs whether an exception occurs or not
print("Thank You")