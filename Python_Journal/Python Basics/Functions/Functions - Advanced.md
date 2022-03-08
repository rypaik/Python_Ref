# Functions - Advanced

## @Lamda Function

Lambda Function - arguments : expression ^8E43D51E-3812-4E43-9A27-D6B9667D2413

```python
string = 'Hello Lamda'

# returns a function object
print(lambda string: string)




x = "HitAndRun"
# prints x
(lambda x : print(x))(x)
```

```python
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
	return y*y*y

# lambda version
lambda_cube = lambda y: y*y*y


# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))
```

Lambda Function with List Comprehension ^FF3F0875-7283-4F5A-B4CE-182BFC5FCE9E

```python
tables = [lambda x = x: x*10 for x in range(1, 11)]

for table in tables:
	print(table())
```

Lambda Function with if-else ^524CC823-DE86-4650-A810-ACD9597C26BF

```python
# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b

print(Max(1, 2))
```

Lambda Function with Multiple Statements ^7CF8123A-60C6-4898-A8BD-02705B9343FD

```python
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)
```

Lambda Function with filter() ^817CBC4D-BE4E-45A4-A424-60DC1AEF23CA

```python
# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)
```

```python
# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age>18, ages))

print(adults)
```

Lambda Function with map()

```python
# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)
```

```python
# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

print(uppered_animals)
```

Lambda Function with reduce()

```python
# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

print(uppered_animals)
```

```python
# python code to demonstrate working of reduce()
# with a lambda function

# importing functools for reduce()
import functools

# initializing list
lis = [ 1 , 3, 5, 6, 2, ]

# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))
```

---

Function Argument Unpacking

