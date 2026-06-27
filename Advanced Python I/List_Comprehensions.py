# List Comprehension is an elegant way to create lists based on existing lists.


# Original list
myList = [1, 2, 9, 5, 3, 5]

# squaredList = [] 
# # for item in myList:
    # squaredList.append(item*item)

# Using List Comprehension
# For each element (i) in myList,
# calculate i * i (square of the number)
# and store it in a new list.

squaredList = [i * i for i in myList]

# Print the new list containing squared values
print(squaredList)