'''
Tuple Methods:
1. count(): Returns the number of occurrences of a specified element in the tuple.
2. index(): Returns the index of the first occurrence of a specified element in the tuple.
3. len(): Returns the number of elements in the tuple.
4. sorted(): Returns a new sorted list of the elements in the tuple (if the elements are comparable).
5. sum(): Returns the sum of all the elements in the tuple (if the elements are numeric).
6. any(): Returns True if any element of the tuple is true, otherwise returns False.
7. all(): Returns True if all elements of the tuple are true, otherwise returns False.
8. len(): Returns the number of elements in the tuple.
9. tuple(): Converts an iterable (like a list) into a tuple.
10. zip(): Combines elements from multiple iterables (like lists or tuples) into a single tuple of tuples.
'''

a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))