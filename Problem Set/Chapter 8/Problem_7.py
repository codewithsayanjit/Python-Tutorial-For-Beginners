# Write a python function to remove a given word from a list and strip it at the same time.


def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word)) # strip() removes characters present in "an" from the beginning and end only.
    return n


l = ["Sayanjit", "Rohan", "Shubham", "an"]

print(rem(l, "an"))