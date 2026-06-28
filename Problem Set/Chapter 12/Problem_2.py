# Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [19, 20, 34, 74, 55, 6 ,79 , 28]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)