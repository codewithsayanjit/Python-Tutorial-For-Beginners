name = "Sayanjit"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[2] # start from index 2 and print the character at index 2
print(character1)


name1 = "Sayanjit"

# Positive index starts from 0 (Left to right) and negative index starts from -1 (right to left)
    
print(name1[-4: -1]) # start from index -4 all the way till -1 (excluding -1)
print(name1[1:4]) # start from index 1 all the way till 4 (excluding 4)

print(name1[:4]) # is same as print(name1[0:4])
print(name1[1:]) # is same as print(name1[1:7]) because if we do not specify the end index it will take the length of the string as the end index. So, it will print from index 1 to the end of the string.