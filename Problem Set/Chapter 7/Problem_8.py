'''
Write a program to print the following star pattern:
*
**
*** for n = 3

'''
 
n = int(input("Enter the number: "))
for i in range(1, n+1): # n+1 is used to include n in the loop
    print("*"* i, end="")  # end="" is used to print the next line in the same line
    print("") # to print the next line after printing the stars in the current line