# PYTHON DUNDERS WITH CLASS

```code
# #  declare our own string class
# class String:
      
#     # magic method to initiate object
#     def __init__(self, string):
#         self.string = string
        
#     # print our string object without this declared prints
#     # <__main__.String instance at 0x103194148>
#     def __repr__(self):
#         return 'Object: {}'.format(self.string)
          
# # Driver Code
# if __name__ == '__main__':
      
#     # object creation
#     string1 = String('Hello')
  
#     # print object location
#     print(string1)



    
### Class Value Pointer
# declare our own string class
class String:
      
    # magic method to initiate object
    def __init__(self, string):
        self.string = string 
          
    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
          
    def __add__(self, other):
        return self.string + other
  
# Driver Code
if __name__ == '__main__':
      
    # object creation
    string1 = String('Hello')
      
    # concatenate String object and a string
    print(string1 +' Geeks')
    
    
    
    
    # SPECIAL METHODS 
    ## Special Methods in defining and using classes (objects)
    
nums = [1, 2, 3, 4, 5]
print(len(nums)) #5
print(nums.__len__()) #5


# def pass_thru(str):
#     pass


# print(pass_thru.__len__("test"))
# returns attribute error 'function' object has no attribute '__len__'





# Turning an Attribute into a Property
class ClassWithRegularAttributes:
    def __init__(self, someParameter, anotherParam):
        self.someAttribute = someParameter
        self.anotherParam = anotherParam
        
obj = ClassWithRegularAttributes('some initial value','next value')
print(obj.someAttribute)  # Prints 'some initial value'
print(obj.anotherParam)
obj.someAttribute = 'changed value'
print(obj.someAttribute)  # Prints 'changed value'
del obj.someAttribute  # Deletes the someAttribute attribute.
# print(obj.someAttribute˜) # Attribute deleted, throws up a syntax error


#GETTERS and SETTERS
class ClassWithBadProperty:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property  # READ ONLY PROPERTY
    def someAttribute(self):  # This is the "getter" method.
        # We forgot the _ underscore in `self._someAttribute here`, causing
        # us to use the property and call the getter method again:
       
        # return self.someAttribute  # This calls the getter again!
       
       #should
        return self.__someAttribute  # This calls the getter again!
    @someAttribute.setter
    def someAttribute(self, value):  # This is the "setter" method.
        self._someAttribute = value

obj = ClassWithBadProperty()
print(obj.someAttribute)  # Error because the getter calls the getter.





#Read-Only Properties
#Your objects might need some read-only properties that can't be set with the assignment operator =. You can make a property read-only by omitting the setter and deleter methods.
@property
def total(self):
    """Total value (in knuts) of all the coins in this WizCoin object."""
    return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
    
    # Note that there is no setter or deleter method for `total`.

# >>> import wizcoin
# >>> purse = wizcoin.WizCoin(2, 5, 10)
# >>> purse.total
# 1141
# >>> purse.total = 1000
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute
```

```other
class IntsAndSum:
    def __init__(self, ints: list[int], precomputed_sum: int = None):
        self.ints: list[int] = ints
        self.sum: int = precomputed_sum if precomputed_sum is not None else sum(ints)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.ints}, sum={self.sum})'

    # not needed, defined __gt__ instead, use builtin max
    # @staticmethod
    # def max(*args):
    #     return max(args, key=lambda x: x.sum)

    def append(self, i: int) -> None:
        self.ints.append(i)
        self.sum += i

    def copy(self):
        return IntsAndSum(ints=self.ints.copy(), precomputed_sum=self.sum)
    #
    # def __gt__(self, other):
    #     return self.sum > other.sum

    def __lt__(self, other):
        return self.sum < other.sum

def main():
    ias = [
        IntsAndSum([1, 6, 1]),
        IntsAndSum([2, 5, 1, 1, 0]),
        IntsAndSum([0, 1, 0])
    ]
    print(ias)
    # print(IntsAndSum.max(*ias))
    print("\n".join(dir(0)))
    print(max(ias))


if __name__ == '__main__':
    main()
```

[TODO](craftdocs://open?blockId=9ADA0568-4EB7-4146-A67D-473D3A2732AE&spaceId=5245eaa1-107f-3a8d-c5b7-4e9a619103cb)

[Dunders in custom classes](https://towardsdatascience.com/how-to-write-awesome-python-classes-f2e1f05e51a9)

```python
from datetime import datetime, timedelta
from typing import Iterable
from math import ceil


class DateTimeRange:
    def __init__(self, start: datetime, end_:datetime, step:timedelta = timedelta(seconds=1)):
        self._start = start
        self._end = end_
        self._step = step

    def __iter__(self) -> Iterable[datetime]:
        point = self._start
        while point < self._end:
            yield point
            point += self._step

    def __len__(self) -> int:
        return ceil((self._end - self._start) / self._step)

    def __contains__(self, item: datetime) -> bool:
        mod = divmod(item - self._start, self._step)
        return item >= self._start and item < self._end and mod[1] == timedelta(0)

    def __getitem__(self, item: int) -> datetime:
        n_steps = item if item >= 0 else len(self) + item
        return_value = self._start + n_steps * self._step
        if return_value not in self:
            raise IndexError()

        return return_value
   
    def __str__(self):
        return f"Datetime Range [{self._start}, {self._end}) with step {self._step}"

# Usage
my_range = DateTimeRange(datetime(2021,1,1), datetime(2021,12,1), timedelta(days=12))
print(my_range)
assert len(my_range) == len(list(my_range))
my_range[-2] in my_range
my_range[2] + timedelta(seconds=12) in my_range
for r in my_range:
    do_something(r)
```

\#dunders

```python
# A simple Python function to check
# whether x is even or odd
 
 
def evenOdd(x):
    """Function to check if the number is even or odd"""
     
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
print(evenOdd.__doc__)
```

