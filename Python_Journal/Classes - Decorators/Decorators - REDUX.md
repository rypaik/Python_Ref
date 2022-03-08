# Decorators - REDUX

### [[Links/PYTHON LINKS]] PAGE

[[TAGS_TOC/Decorators]] - Basic

### First Class Objects

In Python, functions are [**first class objects**](https://www.geeksforgeeks.org/first-class-functions-python/) that mean that functions in Python can be used or passed as arguments.

**Properties of first class functions:**

- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, …

A [decorator](https://www.geeksforgeeks.org/decorators-in-python/) feature in Python wraps in a function, appends several functionalities to existing code and then returns it. Methods and functions are known to be callable as they can be called. Therefore, a decorator is also a callable that returns callable. This is also known as **metaprogramming** as at compile time a section of program alters another section of the program.

---

[[TAGS_TOC/Functions TOC]] - As Objects - Passing

**Example 1: Treating the functions as objects.** ^F2DCE817-F275-4B8F-9883-1451D029C4E6

```python
# Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))

# pass paramter in with new object (function) instance
```

**Example 2: Passing the function as an argument** ^396556ED-E9DE-41EF-9D10-954AD1D85953

```python
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)
```

**Example 3: Returning functions from another function.**

```python
# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15(10))
```

[[PYTHON TODO]] - Classes and Member Function

custom class member function call with dot notation ^BBD773E2-48A2-4418-BD25-D3D2BBCD260B

---

## Decorators

As stated above the decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

TAGS

[[TAGS_TOC/Polymorphism]]

[[TAGS_TOC/Decorators]] - Basic Code

[LINK TO FILE](/Corsair_1TB/)

```python
# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")

# equivalnet to 
@ftbu_decorator
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)



# calling the function
function_to_be_used()


# try 
function_called = ftbu_decoratort(function_to_be used)
function_called()
```

## another Decorator Example

```python
# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
	
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
	def inner1(*args, **kwargs):

		# storing time before function execution
		begin = time.time()
		
		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)

	return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

# calling the function.
factorial(10)
```

\#staticmethod

```python
class TemperatureConverter:
    KEVIN = 'K',
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9*c/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5*(f-32)/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5*(f+459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9*k/5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TemperatureConverter.CELSIUS:
            symbol = '°C'
        elif unit == TemperatureConverter.KEVIN:
            symbol = '°K'

        return f'{value}{symbol}'
```

### Class Methods vs Static Methods (Decorators)

| **Class Methods**                                           | **Static Methods**                                                  |
| ----------------------------------------------------------- | ------------------------------------------------------------------- |
| Python implicitly pass the `cls` argument to class methods. | Python doesn’t implicitly pass the `cls` argument to static methods |
| Class methods **can** access and modify the class state.    | Static methods **cannot** access or modify the class state.         |
| Use `@classmethod` decorators to define class methods       | Use `@staticmethod` decorators to define static methods.            |

[[TAGS_TOC/Decorators]] - @property

[[Classes - Decorators/Decorators - REDUX#^BA763DD5-C023-466B-B28E-4CC5FEA02CEF]] decorator is a built-in decorator in Python for the [property() function](https://www.tutorialsteacher.com/python/property-function). Use `@property` decorator on any method in the [class](https://www.tutorialsteacher.com/python/python-class) to use the method as a property.

You can use the following three [decorators](https://www.tutorialsteacher.com/python/decorators) to define a property:

- @property: Declares the method as a property. ^BA763DD5-C023-466B-B28E-4CC5FEA02CEF
- @.setter: Specifies the setter method for a property that sets the value to a property.
- @.deleter: Specifies the delete method as a property that deletes a property.
```other
# Python program to illustrate the use of
# @property decorator

# Defining class
class Portal:

	# Defining __init__ method
	def __init__(self):
		self.__name =''
	
	# Using @property decorator
	@property
	
	# Getter method
	def name(self):
		return self.__name
	
	# Setter method
	@name.setter
	def name(self, val):
		self.__name = val

	# Deleter method
	@name.deleter
	def name(self):
	del self.__name

# Creating object
p = Portal();

# Setting name
p.name = 'GeeksforGeeks'

# Prints name
print (p.name)

# Deletes name
del p.name

# As name is deleted above this
# will throw an error
print (p.name)
```

```other
class Portal(student):
```

