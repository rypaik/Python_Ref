# timeit

TIMEIT ALTERNATIVES

[pretty-timeit](https://pypi.org/project/pretty-timeit/)

[timeit-plus](https://pypi.org/project/timeit-plus/)

[pytest-timeit](https://pypi.org/project/pytest-timeit/)



---

[timeit — Measure execution time of small code snippets — Python 3.10.2 documentation](https://docs.python.org/3/library/timeit.html)

[Timeit in Python with Examples - GeeksforGeeks](https://www.geeksforgeeks.org/timeit-python-examples/)

[Python Timeit() with Examples](https://www.guru99.com/timeit-python-examples.html)

timeit parameters

Python Parameters

- `stmt` — String containing the code snippets for your test case.
- `setup` — Initial code that will be executed once.
- `timer` — The timer instance. It is defaulted to `time.perf_counter()`, which returns a float.
- `number` — Number of executions to be carried out. The default value is 1,000,000.
- `globals` — Specifies a namespace in which to execute the code.

**Convenience Functions**

timeit.timeit(stmt='pass', setup='pass', timer=, number=1000000, globals=None)¶

timeit.repeat(stmt='pass', setup='pass', timer=, repeat=5, number=1000000, globals=None)¶

timeit.default_timer()

**Public Class**

class timeit.Timer(stmt='pass', setup='pass', timer=, globals=None)¶

   timeit(number=1000000) - Time number executions of the main statement

   autorange(callback=None) - Automatically determine how many times to call timeit().

   repeat(repeat=5, number=1000000) - Call timeit() a few times.

   print_exc(file=None) - Helper to print a traceback from the timed code.

```python
t = Timer(...)       # outside the try/except
try:
    t.timeit(...)    # or t.repeat(...)
except Exception:
    t.print_exc()
```

Bash Parameters

- `-n` — Number of execution
- `-r` — Number of repetitions for the timer. The default is five.
- `-s` — The initial statement that will be executed once initially.
- `-p` — Set to measure process time instead of wall clock time.
- `-u` — Time unit for the output. You can choose nsec, usec, msec, or sec.
- `-v` — Print raw timing results.

```Bash
# CLI

python -m timeit "'-'.join([str(i) for i in range(100)])"

python -m timeit -n 20000 -u sec -v "'-'.join([str(i) for i in range(100)])"
```

# Python

```python
# 

execution_time = timeit.timeit(code, number)
```

```python
import timeit
 
# Setup is run only once
setup_code = '''
import numpy as np
a = np.arange(0, 1000)
print(a.shape)
def print_subarrays(a):
    op = []
    for i in range(a.shape[0]):
        op.append(a[:i])
'''
 
main_block = '''
print_subarrays(a)
'''
 
# Main Block is run 1000 times
print('Best execution Time among 1000 iterations:', timeit.timeit(setup=setup_code, stmt=main_block, number=1000))
```

```Bash
import timeit

# running CLI funciton in .timeit()
result = timeit.timeit("'-'.join([str(i) for i in range(100)])", number=20000)


# .repeat()
result = timeit.repeat("'-'.join([str(i) for i in range(100)])", number=20000


# FUNCTIONAL
def test():
    return '-'.join([str(i) for i in range(100)])

if __name__ == '__main__':
    result = timeit.timeit("test()", setup="from __main__ import test", number=20000)    

print(result)
```

```Bash
# globals option exectues code within the current global namespace
result = timeit.timeit("test()", number=20000, globals=globals())
print(result)
```

---

```python
#Import timeit module
import timeit

# Use semicolon for multiple statements.
print(timeit.repeat("x = 2; x *= 2", number=100000000))
print(timeit.repeat("x = 1; x *= 4", number=100000000))
```

```python
#Import timeit module
import timeit

def func1():
   return 1

def func2():
   return sum([-1, 0, 1, 1])

# Test methods.
print(func1())
print(func2())

# Pass setup argument to call methods.
print(timeit.repeat("func1()", setup="from __main__ import func1"))
print(timeit.repeat("func2()", setup="from __main__ import func2")
```

```python
import timeit
 
start_time = timeit.default_timer()
function_1()
time_1 = timeit.default_timer() - start_time
 
start_time = timeit.default_timer()
function_2()
time_2 = timeit.default_timer() - start_time
 
print('Function 1 took', time_1)
print('Function 2 took', time_2)
```

```python
import timeit
import numpy as np
 
def time_range(size):
    for i in range(size):
        pass
 
def time_arange(size):
    np.arange(size)
 
if __name__ == '__main__':
    # For smaller arrays
    print('Array size: 1000')
 
    start_time = timeit.default_timer();
    time_range(1000)
    range_time_1 = timeit.default_timer() - start_time
 
    start_time = timeit.default_timer();
    time_arange(1000)
    arange_time_1 = timeit.default_timer() - start_time
 
    # For large arrays
    print('Array size: 1000000')
 
    start_time = timeit.default_timer();
    time_range(1000000)
    range_time_2 = timeit.default_timer() - start_time
 
    start_time = timeit.default_timer();
    time_arange(1000000)
    arange_time_2 = timeit.default_timer() - start_time
 
    print(f'size 1000: range() took {range_time_1}')
    print(f'size 1000: arange() took {arange_time_1}')
    print(f'size 1000000: range() took {range_time_2}')
    print(f'size 1000000: arange() took {arange_time_2}')
```

```python
# importing the required modules
import timeit

# binary search function
def binary_search(mylist, find):
	while len(mylist) > 0:
		mid = (len(mylist))//2
		if mylist[mid] == find:
			return True
		elif mylist[mid] < find:
			mylist = mylist[:mid]
		else:
			mylist = mylist[mid + 1:]
	return False


# linear search function
def linear_search(mylist, find):
	for x in mylist:
		if x == find:
			return True
	return False


# compute binary search time
def binary_time():
	SETUP_CODE = '''
from __main__ import binary_search
from random import randint'''

	TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
binary_search(mylist, find)'''
	
	# timeit.repeat statement
	times = timeit.repeat(setup = SETUP_CODE,
						stmt = TEST_CODE,
						repeat = 3,
						number = 10000)

	# printing minimum exec. time
	print('Binary search time: {}'.format(min(times)))	


# compute linear search time
def linear_time():
	SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''
	
	TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
linear_search(mylist, find)
	'''
	# timeit.repeat statement
	times = timeit.repeat(setup = SETUP_CODE,
						stmt = TEST_CODE,
						repeat = 3,
						number = 10000)

	# printing minimum exec. time
	print('Linear search time: {}'.format(min(times)))

if __name__ == "__main__":
	linear_time()
	binary_time()
```

[Python Timeit() with Examples](https://www.guru99.com/timeit-python-examples.html)

```python
# Calling from shell Command line
$ python3 -m timeit '"-".join(str(n) for n in range(100))'

# -m is to use timeit as a module
```

```python
# From Python Interface in Shell
>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
0.3018611848820001
>>> timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
0.2727368790656328
>>> timeit.timeit('"-".join(map(str, range(100)))', number=10000)


>>> timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
```

```python
# Multiple lines with Triple quote


import timeit
import_module = "import random"
testcode = ''' 
def test(): 
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module))
```

```python
# default_timer()
# testing timeit()
 
import timeit
import random
 
def test(): 
    return random.randint(10, 100)
 
starttime = timeit.default_timer()
print("The start time is :",starttime)
test()
print("The time difference is :", timeit.default_timer() - starttime)
```

```python
# timeit.repeat()
import timeit
import_module = "import random"
testcode = ''' 
def test(): 
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))
```

