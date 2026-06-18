# A for loop can have an optional else block. The else block is executed when the loop exhausts, meaning that it has iterated through all the items in the sequence. If the loop is terminated by a break statement, the else block will not be executed.

l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!