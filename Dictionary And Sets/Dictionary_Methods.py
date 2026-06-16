'''
items(): Returns a list of (key,value) tuples.
keys(): Returns a list containing dictionary's keys.
update({"friends":}): Updates the dictionary with supplied key-value pairs.
get("name"): Returns the value of the specified keys.
'''

marks = {
    "Sayanjit": 55,
    "Shubham": 56,
    "Rohan": 23,
    30: "Dipayan"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sayanjit": 99, "Renuka": 100})
print(marks)

print(marks.get("Sayanjit2")) # Prints None
# print(marks["Sayanjit2"]) # Returns an error