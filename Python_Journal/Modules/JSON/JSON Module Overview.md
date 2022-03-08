# JSON Module Overview

JSON Decoding in Python

| **JSON** | **PYTHON** |
| -------- | ---------- |
| object   | dict       |
| array    | list       |
| string   | str        |
| int      | int        |
| real     | float      |
| true     | True       |
| false    | False      |
| Null     | None       |

![Image](JSON%20Module%20Overview.assets/Image.bin)

> **json.loads()** takes in a string and returns a json object.

> **json.dumps()** takes in a json object and returns a string.

> **json.load** it to encode it into json while **json.dumps** decode it into string.

```python
import json

# json.loads
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])



# json.dump
import json
a = {'lalalala': 3}
myString = json.dumps(a)
print (myString)
```

