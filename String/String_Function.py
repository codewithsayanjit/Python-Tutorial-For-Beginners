s = " Hello Python "

print(s.lower()) # It converts all the characters in the string to lowercase.

print(s.upper()) # It converts all the characters in the string to uppercase.

print(s.title()) # It converts the first character of each word to uppercase.

print(s.capitalize()) # It converts the first character of the string to uppercase.

print(s.strip()) # It removes any leading and trailing whitespace from the string.

print(s.replace("Python", "World")) # It replaces all occurrences of a substring with another substring.(Old value, New value)

print(s.find("P")) # It returns the index of the first occurrence of a substring.

print(s.count("o")) # It returns the number of occurrences of a substring in the string.

print(s.startswith(" He"))   # It returns True if the string starts with the specified substring, otherwise it returns False.

print(s.endswith("th"))  # It returns True if the string ends with the specified substring, otherwise it returns False.

print(s.split()) # It splits the string into a list of substrings based on the specified delimiter.

print("-".join(["Python", "Programming"])) # It joins the elements of a list into a single string with the specified delimiter.(Delimiter.join(List))

print("Python".isalpha()) # It returns True if all characters in the string are alphabetic, otherwise it returns False.

print("1234".isdigit()) # It returns True if all characters in the string are numeric, otherwise it returns False.

print("abc123".isalnum()) # It returns True if all characters in the string are alphanumeric, otherwise it returns False.

print(len(s)) # It returns the length of the string.