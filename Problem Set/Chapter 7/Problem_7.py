'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''

n = int(input("Enter the number: "))
for i in range(1, n+1): # n+1 is used to include n in the loop
    print(" "* (n-i), end="") # end="" is used to print the next line in the same line
    print("*"* (2*i-1), end="") # (2*i-1 is used to print odd number of stars in each line) means 1, 3, 5, 7, 9 stars in each line
    print("") # to print the next line after printing the stars in the current line