# Functions - Builtin

[[Classes - Decorators/Classes - Overview]]: Access Instance Variable

getattr()

To access instance variables in Classes

**#lambda**

lambda argumets : expression

```python
def add(x,y)
	return x + y

# calling function
add(2,3)



# lambda function
add = lambda x, y : x+y
print add(2,3)

type(add)
# type: function
```

**#map()**

map(funciton_object, iterable1, iterable2,…)

```python
def multiply2(x):
  return x * 2
    
map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]
```

```python
# map + lambda
map(lambda x : x*2, [1, 2, 3, 4]) #Output [2, 4, 6, 8]
```

map(lambda) over a dictionary

```python
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
  
map(lambda x : x['name'], dict_a) # Output: ['python', 'java']
  
map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]

map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]
```

Multiple Iterables to the Map Function

```python
list_a = [1, 2, 3]
list_b = [10, 20, 30]
  
map(lambda x, y: x + y, list_a, list_b) 
# Output: [11, 22, 33]
```

```python
map_output = map(lambda x: x*2, [1, 2, 3, 4])
print(map_output) # Output: map object: <map object at 0x04D6BAB0>

list_map_output = list(map_output)

print(list_map_output) # Output: [2, 4, 6, 8]
```

**#filter()**

filter(function_object, iterable)

```python
# filter out only even numbers
a = [1, 2, 3, 4, 5, 6]
filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]
```

```python
# filter lis of dicts

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

filter(lambda x : x['name'] == 'python', dict_a) 

# Output: [{'name': 'python', 'points': 10}]
```

```python
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b)

print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c')]
```

\#zip()

zip takes in iterables and returns list of tuples

```python
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b)

print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
```

```python
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b)

print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c')]
```

Unzip - `zip(*listP_of_tuples)`

```python
zipper_list = [(1, 'a'), (2, 'b'), (3, 'c')]
 
 list_a, list_b = zip(*zipper_list)
 print list_a # (1, 2, 3)
 print list_b # ('a', 'b', 'c')
```

ZIP in PYTHON3

In Python3, `zip` method returns a zip object instead of a `list`. This zip object is an `iterator`. `Iterators` are lazily evaluated

```python
list_a = [1, 2, 3]
list_b = [4, 5, 6]

zipped = zip(a, b) # Output: Zip Object. <zip at 0x4c10a30>

len(zipped) # TypeError: object of type 'zip' has no len()

zipped[0] # TypeError: 'zip' object is not subscriptable

list_c = list(zipped) 
#Output: [(1, 4), (2, 5), (3, 6)]

list_d = list(zipped) 
# Output []... Output is empty list becuase by the above statement zip got exhausted.
```

