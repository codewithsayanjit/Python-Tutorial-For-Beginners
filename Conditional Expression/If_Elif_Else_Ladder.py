'''If else and elif statements are a multiway decision taken by our program due to certain conditions in our
code. 
If elif else ladder is a way to check multiple conditions in our code. It is a way to check for multiple conditions and execute a block of code based on the first condition that is true.
'''

a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")


print("End of Program")