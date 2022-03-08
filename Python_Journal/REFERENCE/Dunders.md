# Dunders

```python
# in python - get dunders of an class object (instance)
dir(object)
```

Uses for Class Dunders

   Initialization of new objects

   Object representation

   Enable iteration

   Operator overloading (comparison)

   Operator overloading (addition)

   Method invocation

   Context manager support (with statement)

[Enriching Your Python Classes With Dunder (Magic, Special) Methods – dbader.org](https://dbader.org/blog/python-dunder-methods)

\#TODO:

[[TAGS_TOC/Dunders TOC]]: __init__ , __str__ , __repr__ ,

```python
# OBJECTS


# initialization - __init__

class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []


# object representation __str__  __repr__

class Account:
    # ... (see above)

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)


# Calling - Accessing Built-in Dunders for Classes
acc = Account('bob', 10)
# or 
# self.__class__.__name__


str(acc)
# 'Account of bob with starting amount: 10'

print(acc)
# "Account of bob with starting amount: 10"

repr(acc)
# "Account('bob', 10)"
```

