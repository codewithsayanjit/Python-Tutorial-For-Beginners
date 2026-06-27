# The 'enumerate' function adds counter to an iterable and returns it.

l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1


# This can be simplified using enumerate function
# enumerate() returns both:
# 1. index (position)
# 2. item (value at that position)

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")