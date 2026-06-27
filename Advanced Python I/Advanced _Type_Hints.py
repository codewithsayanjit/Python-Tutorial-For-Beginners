'''
Types Definitions In Python :       Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.
'''

# Variable type hint
age: int = 25

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Alice"))


'''
Advanced Type Hints:  Python's typing module provides more advanced type hints, such as List, Tuple, Dict and Union.
'''

from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type
identifier: Union[int, str] = "ID123"
