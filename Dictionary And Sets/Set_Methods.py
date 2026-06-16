s = {1, 2, 3}

s.add(4)
s.update([5, 6])
s.remove(2)
s.discard(10)

print("Set:", s) # Sets are unordered, so the output may not be in the same order as the input
print("Union:", s.union({7, 8})) # Union of sets combines all unique elements from both sets
print("Intersection:", s.intersection({3, 4, 9})) # Intersection of sets returns only the elements that are present in both sets
print("Difference:", s.difference({3, 4})) # Difference of sets returns elements that are in the first set but not in the second set
print("Symmetric Difference:", s.symmetric_difference({4, 5, 9})) # Symmetric difference of sets returns elements that are in either set but not in both
print("Subset:", {1}.issubset(s)) # Check if the first set is a subset of the second set
print("Superset:", s.issuperset({1})) # Check if the first set is a superset of the second set
print("Disjoint:", s.isdisjoint({10, 11})) # Check if the two sets have no elements in common