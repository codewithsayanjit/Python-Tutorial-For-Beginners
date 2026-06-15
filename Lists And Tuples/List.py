# Python lists are containers to store a set of values of any data type.It can store value of any data type.
#  Python lists are mutable, meaning we can modify, add, or remove their elements after creation without changing the list's unique memory identity. 

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])
print(friends[1:]) # From index 1 to end
print(friends[:4]) # From start to index 4 (not included)