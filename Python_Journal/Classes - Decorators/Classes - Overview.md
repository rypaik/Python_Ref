# Classes - Overview

## [[TAGS_TOC/Classes TOC]] : Class methods

Traditional Class Methods work on instances created by Class calls

![Python_Classes_and_Objects__Guide__–_PYnative.png](Classes%20-%20Overview.assets/Python_Classes_and_Objects__Guide__%E2%80%93_PYnative.png)

In [Object-oriented programming](https://pynative.com/python/object-oriented-programming/), when we design a class, we use the following three methods

- [Instance method](https://pynative.com/python-instance-methods/) performs a set of actions on the data/value provided by the instance variables. If we use instance variables inside a method, such methods are called instance methods.
- [Class method](https://pynative.com/python-class-method/) is method that is called on the class itself, not on a specific object instance. Therefore, it belongs to a class level, and all class instances share a class method.
- [Static method](https://pynative.com/python-static-method/) is a general utility method that performs a task in isolation. This method doesn’t have access to the instance and class variable.
- [https://pynative.com/wp-content/uploads/2021/08/python_class_method_vs_static_method_vs_instance_method.png](https://pynative.com/wp-content/uploads/2021/08/python_class_method_vs_static_method_vs_instance_method.png)

   ![Class Methods]([https://pynative.com/wp-content/uploads/2021/08/python_class_method_vs_static_method_vs_instance_method.png](https://pynative.com/wp-content/uploads/2021/08/python_class_method_vs_static_method_vs_instance_method.png))

| Instance Methods                                        | Class Methods                                                                    | Static Methods                                      |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| Bound to object of a class                              | Bound to the class                                                               | Bound to the class                                  |
| Can modify an Object State                              | Can Modify a Class State                                                         | Can’t modify class or object state                  |
| Can Access and modify both class and instance variables | Can only access Class variable                                                   | Can’t Access or modify class and instance Variables |
|                                                         | Used to create factory methods                                                   |                                                     |
| USES                                                    |                                                                                  |                                                     |
| Useful in modifying instance variables                  | makes changes that would apply across all the class objects using class variable | utilty such as conversion                           |
|                                                         |                                                                                  |                                                     |

   ## [[TAGS_TOC/Classes TOC]]: Constructor

   [[Classes - Decorators/Classes - Constructors and Destructors]]

![Python_Destructors_With_Examples__Complete_Guide__–_PYnative.png](Classes%20-%20Overview.assets/Python_Destructors_With_Examples__Complete_Guide__%E2%80%93_PYnative.png)

```other
# __new__ and __init__


# Internally, the __new__ is the method that creates the object
# And, using the __init__() method we can implement constructor to initialize the object.

# <object-name> = <class-name>(<arguments>)  

class class_name:
    '''This is a docstring. I have created a new class'''
    <statement 1>
    <statement 2>
    .
    .
    <statement N>



# CLASS ATTRIBUTES
# - Instance variables: The instance variables are attributes attached to an instance of a class. We define instance variables in the constructor ( the __init__() method of a class).
    
# - Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.
```

   ### Class Attributes

   n Class, attributes can be defined into two parts:

   - [**Instance variables**](https://pynative.com/python-instance-variables/): The instance variables are attributes attached to an instance of a class. We define instance variables in the constructor ( the `__init__()` method of a class).
   - [**Class Variables**](https://pynative.com/python-class-variables/): A class variable is a variable that is declared inside of class, but outside of any instance method or `__init__()` method.

| Instance Variables                                    | Class Variables                                                                                   |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Bound to Object                                       | Bound to Class                                                                                    |
| declared inside the  **init()** method                | Declared inside of class bout outside of any method                                               |
| not shared by objects, every object has it’s own copy | shared by all objects of a class, values are note varied from object to object instance of class  |
|                                                       | Only one copy of the static variable will be created and shared between all objects of the class. |

   ### Accessing Attributes

   - An instance attribute can be accessed or modified by using the dot notation: `instance_name.attribute_name`.
   - A class variable is accessed or modified using the class name
   - [**Self keyword accesses the instance variable and instance method of the object**](https://pynative.com/python-constructors/#h-self-keyword-in-python)

```other
class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name)

# Modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# Modify class variables by calling class not instance
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)
```

   ### [[TAGS_TOC/Classes TOC]]: Properties

[Classes and Objects in Python](https://pynative.com/python-classes-and-objects/)

![Image.png](Classes%20-%20Overview.assets/Image.png)

[[TAGS_TOC/Classes TOC]]: Access Properties and Assign Values

```python
# class methods demo
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name

s1 = Student("Harry", 12)

# call instance methods
s1.show()
s1.change_age(14)

# call class method
Student.modify_school_name('XYZ School')
# call instance methods
s1.show()
```

[[TAGS_TOC/Classes TOC]]: Modify Object Properties

Obj.PROPERTY = value

```python
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
obj = Fruit("Apple", "red")

# Modifying Object Properties
obj.name = "strawberry"

# calling the instance method using the object obj
obj.show()
# Output Fruit is strawberry and Color is red
```

[[TAGS_TOC/Classes TOC]]: Deleting Object Properties

```python
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
obj = Fruit("Apple", "red")

# Deleting Object Properties
del obj.name

# Accessing object properties after deleting
print(obj.name)
# Output: AttributeError: 'Fruit' object has no attribute 'name'
```

[[TAGS_TOC/Classes TOC]]: Delete Objects

del object_name

```python
class Employee:
    depatment = "IT"

    def show(self):
        print("Department is ", self.depatment)

emp = Employee()
emp.show()

# delete object
del emp

# Accessing after delete object
emp.show()
# Output : NameError: name 'emp' is not defined
```

   [[Classes - Decorators/Classes - Properties]]: Details

   Accessing Properties (attributes_ and assigning value

   - An instance attribute can be accessed or modified by using the dot notation: instance_name.attribute_name.
   - A class variable is accessed or modified using the class name

---

   ## [[TAGS_TOC/Classes TOC]]: Instance Methods

   **The instance method performs a set of actions on the data/value provided by the instance variables.**

   - A instance method is bound to the [object](https://pynative.com/python-classes-and-objects/) of the class.
   - It can access or modify the object state by changing the value of a instance variables

   Diagram of Instance Methods

---

   [[TAGS_TOC/Classes TOC]]: Declaring Instnace Methods

   Declaring Class and Instance Methods

```other
class Student:
    # constructor to initialize instance variables
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):
		 # self refers to the calling object
        print('Name:', self.name, 'Age:', self.age)
```

---

   [[TAGS_TOC/Classes TOC]]: Instance - Calling Instance Method

```other
# Using Classes and Calling Instance Methods


# create first object
print('First Student')
emma = Student("Jessa", 14)
# call instance method
emma.show()

# create second object
print('Second Student')
kelly = Student("Kelly", 16)
# call instance method
kelly.show()
```

---

   [[TAGS_TOC/Classes TOC]]: Instance - Modifying Instance Varables Inside Instance Method

```other
class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age)

    # instance method to modify instance variable
    def update(self, roll_number, age):
        self.roll_no = roll_number
        self.age = age

# create object
print('class VIII')
stud = Student(20, "Emma", 14)
# call instance method
stud.show()

# Modify instance variables
print('class IX')
stud.update(35, 15)
stud.show()
```

---

   [[TAGS_TOC/Classes TOC]]: Instance - Dynamically Add Instance Method to Object

```other
import types

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create new method
def welcome(self):
    print("Hello", self.name, "Welcome to Class IX")


# create object
s1 = Student("Jessa", 15)

# Add instance method to object
s1.welcome = types.MethodType(welcome, s1)
s1.show()

# call newly added method
s1.welcome()
```

   [[TAGS_TOC/Classes TOC]]: Instance - Dynamically Delete Instance Method

```other
class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

    # instance method
    def percentage(self, sub1, sub2):
        print('Percentage:', (sub1 + sub2) / 2)

emma = Student('Emma', 14)
emma.show()
emma.percentage(67, 62)

# Delete the method from class using del operator
# del emma.percentage

# Again calling percentage() method
# It will raise error
emma.percentage(67, 62)


# use delattr(object,name)
# delete instance method percentage() using delattr()
delattr(emma, 'percentage')
emma.show()

# Again calling percentage() method
# It will raise error
emma.percentage(67, 62)
```

---

   # Class Methods

   Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method. The class method has a cls parameter which refers to the class.

   - A class method is bound to the class and not the object of the class. It can access only class variables.
   - It can modify the class state by changing the value of a class variable that would apply across all the class objects.

   In method implementation, if we use only class variables, we should declare such methods as class methods. The class method has a cls as the first parameter, which refers to the class.

   Class methods are used when we are dealing with factory methods. Factory methods are those methods that return a class object for different use cases. Thus, factory methods create concrete implementations of a common interface.

   Class Method Diagram

---

   ## Creating Class Method with @classmethod Decorator

```other
from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

jessa = Student('Jessa', 20)
jessa.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()
```

   - [classmethod is a builtin funciton decorator](craftdocs://open?blockId=993C8677-9222-47C4-B553-8FB45A5E5B6B&spaceId=5245eaa1-107f-3a8d-c5b7-4e9a619103cb)
   - class method can only access the class attributes not the instance attributes

   ## Create class method using classmethod() function

```other
class School:
    # class variable
    name = 'ABC School'

    def school_name(cls):
        print('School Name is :', cls.name)

# create class method
School.school_name = classmethod(School.school_name)

# call class method
School.school_name()
```

   ## Access Class Variable in Class Methods

```python
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, self.age, 'School:', Student.school_name)

jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('XYZ School')
jessa.show()
```

