# Variable Scoping

Search Order for named variables

- the innermost scope, which is searched first, contains the local names
- the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
- the next-to-last scope contains the current module’s global names
- the outermost scope (searched last) is the namespace containing built-in names

Local Stays Local then “bubble down”

**Global Variable**

```python
global_variable = [1, 2, 3]   # global variable

def function1():
    print(global_variable)
    # [1, 2, 3]

function1()
```

```python
# variables in functions are subject to a local scope and does not conflict with global variables

global_variable = [1, 2, 3]   # global variable

def function2():
    global_variable = [2, 3, 4]   # local variable
    print(global_variable)
    # [2, 3, 4]
    print(hex(id(global_variable)))
    # 0x7f32763a4780

function2()
print(global_variable)
# [1, 2, 3]
print(hex(id(global_variable)))
# 0x7f32763f7880
```

Global Keyword

```python
global_variable = [1, 2, 3]   # global variable

def function3():
    global global_variable
    global_variable = [3, 4, 5]
    print(global_variable)
    # [3, 4, 5]
    print(hex(id(global_variable)))
    # 0x7f32763a4780

function3()
print(global_variable)
# [3, 4, 5]
print(hex(id(global_variable)))
# 0x7f32763a4780
```

```python
def function4():
    global new_global_variable
    new_global_variable = "A new global variable"
    print(new_global_variable)
    # A new global variable
    print(hex(id(new_global_variable)))
    # 0x7f32763a25d0

function4()
print(new_global_variable)
# A new global variable
print(hex(id(new_global_variable)))
# 0x7f32763a25d0
```

Nested Function and Non Local Keyword

```python
def outer_function1():
    variable = 1

    def inner_function1():
        variable = 2
        print(f"inner_function: {variable}")

    inner_function1()
    print(f"outer_function: {variable}")

outer_function1()
# The output of the variable:
# inner_function: 2
# outer_function: 1


# variable in inner_function1 is a different object than the variable in outer_function1.
```

the *nonlocal* keyword causes the variable to refer to the previously bound variable in the closest scope and prevent the variable from binding locally.

```python
def outer_function2():
    variable = 1

    def inner_function2():
        nonlocal variable
        variable = 2
        print(f"inner_function: {variable}")

    inner_function2()
    print(f"outer_function: {variable}")

outer_function2()
# The output of the variable:
# inner_function: 2
# outer_function: 2
```

**GLOBAL VS NONLOCAL**

the *nonlocal* keyword enables access only to the next closest scope outside of the local scope, whereas the *global* keyword allows access to the global scope.

the change of variable *x* in the *innermost* function only affects the variable x in the *inner* function, the next closest scope.

```python
x = "hello world"

def outer_nonlocal():

    x = 0

    def inner():

        x = 1

        def innermost():
            nonlocal x
            x = 2
            print(f"innermost: {x}")

        innermost()
        print(f"inner: {x}")

    inner()
    print(f"outer_nonlocal: {x}")

outer_nonlocal()
print(f"global: {x}")
# The output of x:
# innermost: 2
# inner: 2
# outer_nonlocal: 0
# global: hello world
```

```python
y = "hello world"

def outer_global():

    y = 0

    def inner():

        y = 1

        def innermost():
            global y
            y = 2
            print(f"innermost: {y}")

        innermost()
        print(f"inner: {y}")

    inner()
    print(f"outer_global: {y}")

outer_global()
print(f"global: {y}")
# The output of y:
# innermost: 2
# inner: 1
# outer_global: 0
# global: 2
```

