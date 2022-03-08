# Regex Basic

[[REFERENCE/Regex for Python]] : Reference Doc

`re.findall()`

Returns a list of strings containing matches

```python
# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']
```

`re.split()`

splits the string where there is a match and returns a list of strings where the splits have occurred

```python
import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']
```

```python
# using maxsplit

import re

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
```

`re.sub()`

re.sub(pattern, replace, string)

returns a string where matched occurrences are replaced with content of <replace> variable

```python
# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Output: abc12de23f456
```

```python
# pass count as fourth parameter  

import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, 1) 
print(new_string)

# Output:
# abc12de 23
# f45 6
```

`re.subn()`

returns a tuple of 2 items containing the new string and the number of substitutions made

```python
# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string) 
print(new_string)

# Output: ('abc12de23f456', 4)
```

`re.search()`

match = re.search(pattern, str)

method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.

```python
import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string
```

---

## MATCH

You can get methods and attributes of a match object using dir() function.

`match.group()`

returns the part of the string where there is a match

```python
import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

# Output: 801 35
```

Our pattern (\d{3}) (\d{2}) has two subgroups (\d{3}) and (\d{2}). You can get the part of the string of these parenthesized subgroups. Here's how:

> > match.group(1)
'801'

> > match.group(2)
'35'

> > match.group(1, 2)
('801', '35')

> > match.groups()
('801', '35')

`match.start(), match.end() and match.span()`

The start() function returns the index of the start of the matched substring. Similarly, end() returns the end index of the matched substring.

> > match.start()
2

> > match.end()
8

The span() function returns a tuple containing start and end index of the matched part.

> > match.span()
(2, 8)

`match.re , match.string`

The re attribute of a matched object returns a regular expression object. Similarly, string attribute returns the passed string.

> > \>>> match.re
re.compile('(\d{3}) (\d{2})')

> > \>>> match.string
'39801 356, 2102 1111'

---

Using r prefix before RegEx

When r or R prefix is used before a regular expression, it means raw string. For example, '\n' is a new line whereas r'\n' means two characters: a backslash \ followed by n.

Backlash \ is used to escape various characters including all metacharacters. However, using r prefix makes \ treat as a normal character.

```python
import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)

# Output: ['\n', '\r']
```

