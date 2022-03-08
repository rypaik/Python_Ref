# Lists

A versatile sequential data structure in Python. Use [ , , , ].  A list could hold any type of data: numerical, or strings or other types. Different data types can be mixed in a single list. List is mutable

```python
list_1 = [1, 2, 3]

list_2 = ['Hello', 'World']

list_3 = [1, 2, 3, 'Apple', 'orange']


# nesting lists
list_4 = [list_1, list_2]

# [[1, 2, 3], ['Hello', 'World']]
```

![Image](Lists.assets/Image.bin)

List Basics

```python
list_3[2]

# test 
list_4[0,1]
list_4[1,1]
```

```python
# 
list_3[:3]
```

List Slicing

[start : stop : steps]

which means that slicing will start from index start

will go up to stop in step of steps.

Default value of start is 0, stop is last index of list

and for step it is 1

```python
# Let us first create a list to demonstrate slicing
# lst contains all number from 1 to 10
lst =list(range(1, 11))
print (lst)
	
# below list has numbers from 2 to 5
lst1_5 = lst[1 : 5]
print (lst1_5)
	
# below list has numbers from 6 to 8
lst5_8 = lst[5 : 8]
print (lst5_8)
	
# below list has numbers from 2 to 10
lst1_ = lst[1 : ]
print (lst1_)
	
# below list has numbers from 1 to 5
lst_5 = lst[: 5]
print (lst_5)
	
# below list has numbers from 2 to 8 in step 2
lst1_8_2 = lst[1 : 8 : 2]
print (lst1_8_2)
	
# below list has numbers from 10 to 1
lst_rev = lst[ : : -1]
print (lst_rev)
	
# below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9 : 4 : -2]
print (lst_rev_9_5_2)
```

---

## List Comprehension

Shorter syntax when you want to create a new list based on the values of an existing list.

newList **=** **[** expression(element) **for** element **in** oldList **if** condition **]**

```python
# Empty list
List = []

# Traditional approach of iterating
for character in 'Geeks 4 Geeks!':
	List.append(character)

# Display list
print(List)



# LIST COMPREHENSION
# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!']

# Displaying list
print(List)
```

NESTED LIST COMPREHENSIONS

```python
matrix = []

for i in range(3):
	
	# Append an empty sublist inside the list
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print(matrix)



# LIST COMPREHENSION VERSION
# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)
```

```python
# display even elements from list of random numbers
# Assign matrix
twoDMatrix = [[10, 20, 30],
				[40, 50, 60],
				[70, 80, 90]]

# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]

print(trans)
```

LIST COMPREHENSION LAMBDA ^70230B02-7D77-4543-87C5-45DA9EF4A82C

```python
# using lambda to print table of 10
numbers = []

for i in range(1, 6):
	numbers.append(i*10)

print(numbers)



# List Comprehension
numbers= [i*10 for i in range(1,6)]

print(numbers)



# Lambda and List Comprehension
numbers = list(map(lambda i: i*10, [i for i in range(1,6)]))

print(numbers)
```

CONDITIONALS - LIST COMPREHENSION

```python
# Getting square of even numbers from 1 to 10
squares = [n**2 for n in range(1, 11) if n%2==0]

# Display square of even numbers
print(squares)
```

```python
# Toggle Case of Each Char in String
# Initializing string
string = 'Geeks4Geeks'

# Toggle case of each character
List = list(map(lambda i: chr(ord(i)^32), string))

# Display list
print(List)
```

```python
# Reverse Each String in Tuple

List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]

# Display list
print(List)
```

```python
# sum of digits of all odd elements in list
# Explicit function
def digitSum(n):
	dsum = 0
	for ele in str(n):
		dsum += int(ele)
	return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)
```

