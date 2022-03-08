# Functions Basic

> Syntax:

> def function_name(parameters):

> """docstring"""
statement(s)
return expression

```python
# Declaring Function adn Calling

 
def fun():
  print("Welcome to Fun")

# call a Function
fun()

# ----------------------- # 
# Function Arguments
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
# Driver code to call the function
evenOdd(2)
evenOdd(3)



# ----------------------- # 

# default arguments

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 
 
# Driver code (We call myFun() with only
# argument)
myFun(10)




# ----------------------- # 
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
 
 
# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')



# ----------------------- #
# *args for variable number of arguments
 
 
def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')



# ----------------------- #
*kwargs for variable number of keyword arguments 
 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


# ---------------------- #
# return a value from func
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2
 
 
print(square_value(2))
print(square_value(-4))
```

## Pass by Reference or Pass by Value

Every variable name is a reference.

When we pass a variable to a function, a new reference to the object is created

```python
# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20
 
 
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

# [20, 11, 12, 13, 14, 15]




# ------------------------- #

def myFun(x):
    x[0]=33 					# modifies passed list
    x = [20, 30, 40] 		# new object declared
    x[0]= 1				 	# modifies new object x
    return x					# must return to set this object outside of function
 
 
# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)
n
#[10, 11, 12, 13, 14, 15]
```

## Lambda (Anonymous) Functions

```python
# Python code to illustrate the cube of a number
# using lambda function
 
 
def cube(x): return x*x*x
 
cube_v2 = lambda x : x*x*x
 
# print(cube(7))
# print(cube_v2(7))
```

## Embedded Functions

```python
# Python program to
# demonstrate accessing of
# variables of nested functions
 
def f1():
    s = 'I love Python Functions'
     
    def f2():
        print(s)
         
    f2()
 
# Driver's code
f1()
```

# *args and **kwargs

*args - in function definitions is used to pass variable number of non0-key worded arguments to a function

**kwargs

(*) operator to unpack a list??

```python
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print (arg)
   
myFun('Hello', 'Welcome', 'to', 'Python')




# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
myFun('Hello', 'Welcome', 'to', 'Python')
```

