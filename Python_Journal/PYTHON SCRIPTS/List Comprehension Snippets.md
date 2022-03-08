# List Comprehension Snippets

Iterating with Python Lamdas ^A2F55FAF-F7B8-410E-9BA3-1183CE15B663

@LIst Iterating  with Lamdas

```python
# Iterating With Python Lambdas

# list of numbers
l1 = [4, 2, 13, 21, 5]

# list of square of numbers
# lambda function is used to iterate
# over list l1
l2 = list(map(lambda v: v ** 2, l1))

# print list
print(l2)
```

@List Comprehension and For Loop

```python
# Maesuring Difference between For loop and list comprehension
# Import required module
import time


# define function to implement for loop
def for_loop(n):
	result = []
	for i in range(n):
		result.append(i**2)
	return result


# define function to implement list comprehension
def list_comprehension(n):
	return [i**2 for i in range(n)]


# Driver Code

# Calculate time takens by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for_loop:',round(end-begin,2))

# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for list_comprehension:',round(end-begin,2))
```

