# What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0) # 20.0 is a float, but it is equal to 20 (int) in Python. So, it will not be added to the set.
s.add('20') # length of s after these operations?

print(len(s))