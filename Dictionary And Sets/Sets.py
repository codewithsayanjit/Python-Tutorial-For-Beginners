'''
Sets in Python are a collection of unique elements. They are unordered, meaning that the elements do not have a specific order. Sets are mutable, which means you can add or remove elements from a set after it has been created. However, the elements themselves must be immutable (like numbers, strings, or tuples).

Set is a collection of non-repetitive elements.
Properties Of Sets
1) Sets are unordered => Element’s order doesn’t matter
2) Sets are unindexed => Cannot access elements by index
3) There is no way to change items in sets.
4) Sets cannot contain duplicate values.
'''

e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 


print(s)