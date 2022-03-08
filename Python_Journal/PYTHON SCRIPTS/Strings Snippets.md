# Strings Snippets

Python has the following data types built-in by default, in these categories:

| **Text Type:**  | `str`                              |
| --------------- | ---------------------------------- |
| Numeric Types:  | `int`, `float`, `complex`          |
| Sequence Types: | `list`, `tuple`, `range`           |
| Mapping Type:   | `dict`                             |
| Set Types:      | `set`, `frozenset`                 |
| Boolean Type:   | `bool`                             |
| Binary Types:   | `bytes`, `bytearray`, `memoryview` |

**Strings**

```python
from pprint import pprint

message00 = 'can use single or double quotes'


message = """this string 
retains the spacing"""
print(message)


# getting the object attirbutes
pprint(dir(message))





# len()
print(len(message))

# slicing strings
print(message[1])
print(message[:5])
print(message[:-1])

# upper()
print(message.upper())

# lower()
print(message.lower())

# find()
print(message.find('string'))


# count()
print(message.count('t'))
```

