# Classes - Different Input Parameters

```other
class Portal():

# class Portal: works
# class Portal(args): error args: not defined


    def __init__(self, *args):
        try:
            self.args = dict(args)
        except TypeError:
            print(TypeError)
            # do something if invalid parameters


obj = Portal(("Name", "Matt"), ("Age", 19), ("occupation", "student"))
print(obj.args) #returns dictionary

print(obj.args[0]) # throws up keyerror
print(obj.name) # throws up an attributeError
print(obj.args[name]) # NameError
```

```other
class anotherClass():
    def __init__(self, params):
        self.name = params.get('name')
        self.age = params.get('age')
        self.occupation = params.get('occupation')



obj = anotherClass({
        "name":"Matt",
        "age" :19,
        "occupation": "student"
        })
print(obj.name)
```

[[PYTHON TODO]]: Move to Functions

```other
def func(d):
      
    for key in d:
        print("key:", key, "Value:", d[key])
          
# Driver's code
D = {'a':1, 'b':2, 'c':3}
func(D)
```

```other
# Python program to demonstrate
# passing dictionary as kwargs


def display(**name):
	
	print (name["fname"]+" "+name["mname"]+" "+name["lname"])

def main():
	
	# passing dictionary key-value
	# pair as arguments
	display(fname ="John",
			mname ="F.",
			lname ="Kennedy")
# Driver's code
main()
```

```other
def display(x = 0, y = 0, **name):
      
    print (name["fname"]+" "+name["mname"]+" "+name["lname"])
    print ("x =", x)
    print ("y =", y)
  
def main():
    # passing dictionary key-value 
    # pair with other arguments
    display(2, fname ="John", mname ="F.", lname ="Kennedy")
      
# Driver's code
main()
```

