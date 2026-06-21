# A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file.

# Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "bad", "ganda"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)