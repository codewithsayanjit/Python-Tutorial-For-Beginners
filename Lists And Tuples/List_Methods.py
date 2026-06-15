'''
List methods are built-in functions that allow us to perform various operations on lists, such as adding, removing, or modifying elements. Here are some commonly used list methods: 
1. append(): Adds an element to the end of the list.
2. insert(): Inserts an element at a specified index.
3. remove(): Removes the first occurrence of a specified element from the list.
4. pop(): Removes and returns the element at a specified index (or the last element if no index is specified).
5. sort(): Sorts the elements of the list in ascending order (or in a specified order).
6. reverse(): Reverses the order of the elements in the list.
7. count(): Returns the number of occurrences of a specified element in the list.
8. index(): Returns the index of the first occurrence of a specified element in the list.
9. clear(): Removes all elements from the list, leaving it empty.
10. extend(): Extends the list by appending elements from another iterable (e.g., another list).
'''


friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Sayanjit") # Adds "Sayanjit" to the end of the list
print(friends)

l1 = [1, 34,62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3)
print(value)
print(l1)