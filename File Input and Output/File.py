'''
The random-access memory is volatile, and all its contents are lost once a program terminates. In order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.

# There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)
Python has a lot of functions for reading, updating, and deleting files.

# Modes Of Opening A File
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode 

'''


'''
a = "a very long string with emails"
emails = []
3 seconds
'''

# open("filename", "mode of opening(read mode by default)")
f = open("file.txt", "r") # Python has an open() function for opening files. It takes 2 parameters: filename and mode.
data = f.read() # Read its contents
print(data) # Print its contents
f.close() # Close the file