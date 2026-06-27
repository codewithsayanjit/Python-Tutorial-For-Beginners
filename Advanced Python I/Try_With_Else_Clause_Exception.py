# Exception Handling with try-except-else

try:
    # Take input from the user and convert it to an integer
    a = int(input("Hey, Enter a number: "))

    # Print the number if conversion is successful
    print(a)

# This block runs if any exception occurs
except Exception as e:
    print("An error occurred:")
    print(e)

# This block runs only if no exception occurs in the try block
else:
    print("I am inside else")