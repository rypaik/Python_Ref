# Decorator Snippets

```python
# decorator to handle *args and **kwargs
def mul_decorator(func):
    def wrapper(*args, **kwargs):
        print('function', func.__name__, 'called with args - ', /
              args, 'and kwargs - ', kwargs)
        result = func(*args, **kwargs)
        print('function', func.__name__, 'returns', result)
        return result
    return wrapper
  
  
@mul_decorator
def mul(a, b):
    return a * b
mul(3, 3)
mul(3, b = 6)
```

```python
# func will be func = type(func) -> <class 'function'>
@type
def func(): 
    return 42
  
print(func)
  
# print doesn't return anything, so func == None
@print
def func2(): 
    return 42
  
# Prints None
print(func2)
```

```python
# usign built in functions as 


# func will be func = type(func) -> <class 'function'>
@type
def func(): 
    return 42
  
print(func)


  
# print doesn't return anything, so func == None
@print
def func2(): 
    return 42
  
# Prints None
print(func2)
```

```python
# replace decorated object with somethign else

# Creating a decorator
class function_1:
    def __init__(self, func):
        self.func = func
        self.stats = []
  
    def __call__(self, *args, **kwargs):
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            self.stats.append((args, kwargs, e))
            raise e
        else:
            self.stats.append((args, kwargs, result))
            return result
  
    @classmethod
    def function_2(cls, func):
        return cls(func)
  
  
@function_1.function_2
def func(x, y):
    return x / y
  
print(func(6, 2))
  
print(func(x = 6, y = 4))
  
func(5, 0)
print(func.stats)
print(func)
```

```python
def dict_from_func(func):
    return {func.__name__: func}
  
  
activity = {}
  
@activity.update
@dict_from_func
def mul(a, b):
    return a * b
  
  
@activity.update
@dict_from_func
def add(a, b):
    return a + b
  
  
print(mul)
print(activity)
print(activity['mul'](2, 5))
```

