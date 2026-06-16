'''
Dictionary Methods
| Method                  | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| `clear()`               | Removes all items from the dictionary                            |
| `copy()`                | Returns a shallow copy of the dictionary                         |
| `fromkeys()`            | Creates a new dictionary with specified keys and a default value |
| `get()`                 | Returns the value for a key; avoids `KeyError`                   |
| `items()`               | Returns key-value pairs as view objects                          |
| `keys()`                | Returns all keys as a view object                                |
| `values()`              | Returns all values as a view object                              |
| `pop()`                 | Removes and returns the value of a specified key                 |
| `popitem()`             | Removes and returns the last inserted key-value pair             |
| `setdefault()`          | Returns value of a key; inserts key if missing                   |
| `update()`              | Updates dictionary with another dictionary or iterable           |
| `__contains__()` (`in`) | Checks if a key exists                                           |

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