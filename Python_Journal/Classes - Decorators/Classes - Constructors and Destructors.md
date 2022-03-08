# Classes - Constructors and Destructors

[[TAGS_TOC/Classes TOC]]**: Constructors**

Default Constructor

```python
class Employee:

    def display(self):
        print('Inside Display')

emp = Employee()
emp.display()
```

[[TAGS_TOC/Classes TOC]]: Non-Parameterized Constructor - constructor without arguments

```python
class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)

# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()
```

[[TAGS_TOC/Classes TOC]]: Parameterized Constructors - constructors with arguments

```python
class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display object
    def show(self):
        print(self.name, self.age, self.salary)

# creating object of the Employee class
emma = Employee('Emma', 23, 7500)
emma.show()

kelly = Employee('Kelly', 25, 8500)
kelly.show()
```

[[TAGS_TOC/Classes TOC]]: Constructors with default Values

```python
class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)

# creating object of the Student class
emma = Student('Emma')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()
```

[[TAGS_TOC/Classes TOC]]: Self Keyword in Python

Using `self`, we can **access the** [**instance variable**](https://pynative.com/python-instance-variables/)** and instance method** of the object.

**The first argument `self` refers to the current object.**

Whenever we call an instance method through an object, the Python compiler implicitly passes object reference as the first argument commonly known as self.

```python
class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self points to the current object
    def show(self):
        # access instance variable using self
        print(self.name, self.age)

# creating first object
emma = Student('Emma', 12)
emma.show()

# creating Second object
kelly = Student('Kelly', 13)
kelly.show()
```

[[TAGS_TOC/Classes TOC]]: Constructor Overloading

**Python does not support constructor overloading**. If we define multiple constructors then, the interpreter will considers only the last constructor and throws an error if the sequence of the arguments doesn’t match as per the last constructor.

```python
class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age

# creating first object
emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)
```

[[TAGS_TOC/Classes TOC]]: Constructor Chaining (Class Inheritance)

Constructor chaining is the process of calling one constructor from another constructor. Constructor chaining is useful when you want to invoke multiple constructors, one after another, by initializing only one instance.

In Python, **constructor chaining is convenient when we are dealing with** [**inheritance**](https://pynative.com/python-inheritance/)****. When an instance of a child class is initialized, the constructors of all the parent classes are first invoked and then, in the end, the constructor of the child class is invoked.

Using the `super()` method we can invoke the parent class constructor from a child class.

```python
class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine

class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed

class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range

# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')
```

[[TAGS_TOC/Classes TOC]]: Class Variables - Counting number of objects of a Class

The constructor executes when we create the object of the class. For every object, the constructor is called only once. So for counting the number of objects of a class, we can add a counter in the constructor, which increments by one after each object creation.

```python
class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine

class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed

class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range

# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')


# OUTPUTS
# The number of employee: 3
```

[[TAGS_TOC/Classes TOC]]: Constructor Return Value
A constructor is implicitly called at the time of object instantiation. Thus, it has the sole purpose of initializing the instance variables.

The `__init__()` is required to return None. We can not return something else. If we try to return a non-None value from the `__init__()` method, it will raise TypeError.

```python
class Test:

    def __init__(self, i):
        self.id = i
        return True

d = Test(10)


# RETURNS TypeError
TypeError: __init__() should return None, not 'bool'
```

[[TAGS_TOC/Classes TOC]]: Destructors

destructor is not called manually but completely automatic. **destructor gets called in the following two cases**

- When an object goes out of scope or
- The reference counter of the object reaches 0.
- The `__del__` method is called for any object when the reference count for that object becomes zero.
- The reference count for that object becomes zero when the application ends, or we delete all references manually using the `del` keyword.
- The destructor will not invoke when we delete object reference. It will only invoke when all references to the objects get deleted.

![Python_Destructors_With_Examples__Complete_Guide__–_PYnative.png](Classes%20-%20Constructors%20and%20Destructors.assets/Python_Destructors_With_Examples__Complete_Guide__%E2%80%93_PYnative.png)

In Python, The special method `del()` is used to define a destructor. For example, when we execute `del object_name` destructor gets called automatically and the object gets garbage collected.

```python
class Student:

    # constructor
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('Object initialized')

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')

# create object
s1 = Student('Emma')
s1.show()

# delete object
del s1
```

```python
# garbage collection - destruction
import time

class Student:

    # constructor
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Object destroyed')

# create object
s1 = Student('Emma')
# create new reference
# both reference points to the same object
s2 = s1
s1.show()

# delete object reference s1
del s1

# add sleep and observe the output
time.sleep(5)
print('After sleep')
s2.show()
```

### Examples of Destructor Errors

### Circular Referencing

```python
import time


class Vehicle():
    def __init__(self, id, car):
        self.id = id;
        # saving reference of Car object
        self.dealer = car;
        print('Vehicle', self.id, 'created');

    def __del__(self):
        print('Vehicle', self.id, 'destroyed');


class Car():
    def __init__(self, id):
        self.id = id;
        # saving Vehicle class object in 'dealer' variable
        # Sending reference of Car object ('self') for Vehicle object
        self.dealer = Vehicle(id, self);
        print('Car', self.id, 'created')

    def __del__(self):
        print('Car', self.id, 'destroyed')


# create car object
c = Car(12)
# delete car object
del c
# ideally destructor must execute now

# to observe the behavior
time.sleep(8)
```

### Exception in `init` Method and Destructor

```python
class Vehicle:
    def __init__(self, speed):
        if speed > 240:
            raise Exception('Not Allowed');
        self.speed = speed;

    def __del__(self):
        print('Release resources')

# creating an object
car = Vehicle(350);
# to delete the object explicitly
# Throws Error because exception didn't allow for creation of class instance
del car
```

