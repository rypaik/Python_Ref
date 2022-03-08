# Classes - Inheritance

\#inheritance

\#snippets

### Inheritance Code

```python
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)

class Person(object):
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True

# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())
```

```python
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person( object ):	

		# __init__ is known as the constructor		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)

# child class
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				# invoking the __init__ of the parent class
				Person.__init__(self, name, idnumber)

				
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")	

# calling a function of the class Person using its instance
a.display()
```

```python
# Python program to demonstrate error if we
# forget to invoke __init__() of the parent.

class A:
	def __init__(self, n = 'Rahul'):
			self.name = n
class B(A):
	def __init__(self, roll):
			self.roll = roll


# error fix


# object = B(23)
print (object.name)
```

Classes Inheritance - Multiple Inheritance

```python
# Python example to show the working of multiple
# inheritance
class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")

class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"		
		print("Base2")

class Derived(Base1, Base2):
	def __init__(self):
		
		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")
		
	def printStrs(self):
		print(self.str1, self.str2)
		

ob = Derived()
ob.printStrs()
```

```python
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Base(object):
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):
	
	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
	
	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address		

# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
```

```python
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Base(object):
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):
	
	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
	
	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address		

# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
```

