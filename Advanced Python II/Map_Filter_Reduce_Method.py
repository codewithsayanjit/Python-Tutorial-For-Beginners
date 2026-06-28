# Import reduce() from the functools module
from functools import reduce

# -------------------------
# MAP EXAMPLE
# -------------------------
# map() applies a function to each element of an iterable.
'''
Map applies a function to all the items in an input_list.
Syntax:
    map(function, input_list)
'''


# List of numbers
l = [1, 2, 3, 4, 5]

# Lambda function to calculate the square of a number
square = lambda x: x * x

# Apply square() to every element in the list
sqList = map(square, l)

# Convert the map object into a list and print it
print("Squared List:", list(sqList))

# Output: [1, 4, 9, 16, 25]


# -------------------------
# FILTER EXAMPLE
# -------------------------
# filter() selects elements that satisfy a condition.
'''
Filter creates a list of items for which the function returns true.
Syntax:
    list(filter(function))
'''


# Function to check whether a number is even
def even(n):
    return n % 2 == 0

# Filter only even numbers from the list
onlyEven = filter(even, l)

# Convert the filter object into a list and print it
print("Even Numbers:", list(onlyEven))

# Output: [2, 4]


# -------------------------
# REDUCE EXAMPLE
# -------------------------
# reduce() repeatedly applies a function to the elements of an iterable until a single value remains.
'''
Reduce applies a rolling computation to sequential pair of elements.
from functools import reduce
val = reduce(function, list1)
If the function computes sum of two numbers and the list is [1,2,3,4]
'''


# Function to calculate the sum of two numbers
def add(a, b):
    return a + b

# Lambda function to calculate the product of two numbers
mul = lambda x, y: x * y

# Find the sum of all elements in the list
print("Sum of List:", reduce(add, l))

# Find the product of all elements in the list
print("Product of List:", reduce(mul, l))

# Output:
# Sum of List: 15
# Product of List: 120