# How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c", end="") # This will print "c" without a new line at the end, so the next print statement will continue on the same line.
print("d", end="") # end="" prevents the print function to print a new line at the end. By default, end="\n" which means it will print a new line at the end.