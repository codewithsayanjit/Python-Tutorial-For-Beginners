s = {1, 2, 3}

s.add(4) # Add an element to the set
s.update([5, 6]) # Update the set with multiple elements from an iterable (like a list)
s.remove(2) # Remove an element from the set; raises KeyError if the element is not found
s.discard(10) # Remove an element from the set if it is present; does nothing if the element is not found

print("Set:", s) # Sets are unordered, so the output may not be in the same order as the input
print("Union:", s.union({7, 8})) # Union of sets combines all unique elements from both sets
print("Intersection:", s.intersection({3, 4, 9})) # Intersection of sets returns only the elements that are present in both sets
print("Difference:", s.difference({3, 4})) # Difference of sets returns elements that are in the first set but not in the second set
print("Symmetric Difference:", s.symmetric_difference({4, 5, 9})) # Symmetric difference of sets returns elements that are in either set but not in both
print("Subset:", {1}.issubset(s)) # Check if the first set is a subset of the second set.Checks whether all elements of Set A are present in Set B.
print("Superset:", s.issuperset({1})) # Check if the first set is a superset of the second set.Checks whether Set A contains all elements of Set B.
print("Disjoint:", s.isdisjoint({10, 11})) # Check if the two sets have no elements in common

'''
issubset()    → Small set inside Big set?
issuperset()  → Big set contains Small set?
isdisjoint()  → No common elements?
'''
