# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}") # This will print the multiplication table of n in reversed order. For example, if n = 5, it will print the multiplication table of 5 in reversed order as follows:
# 5 X 10 = 50
# 5 X 9 = 45
# 5 X 8 = 40
# 5 X 7 = 35
# 5 X 6 = 30
# 5 X 5 = 25
# 5 X 4 = 20    
# 5 X 3 = 15
# 5 X 2 = 10
# 5 X 1 = 5