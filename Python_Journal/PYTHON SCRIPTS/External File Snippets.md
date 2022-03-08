# External File Snippets

[[REFERENCE/External Files with Python]]

---

Basics:

open → write → close

```python
created_file = open("geeksforgeeks.txt","x")

# Check the file
print(open("geeksforgeeks.txt","r").read() == False)


# ----------
my_file = open("geeksforgeeks.txt", "w")
my_file.write("Geeksforgeeks is best for DSA")
my_file.close()

#let's read the contents of the file now
my_file = open("geeksforgeeks.txt","r")
print(my_file.read())


# ----------

my_file = open("geeksforgeeks.txt","a")
my_file.write("..>>Visit geeksforgeeks.org for more!!<<..")
my_file.close()

# reading the file
my_file = open("geeksforgeeks.txt","r")
print(my_file.read())
```

Getting Dunders for Open File:

\#dunders

[[REFERENCE/Dunders]]

```python
f = open('output.txt')
print(f)
print(f.__dict__)
f.read()
f.close()
f.closed
```

\#snippets

[[PYTHON SNIPPETS]]: open()

```python
#snippet


# Open Multiple Files in a Single Statement

items = ['dog', 'cat', 'apple', 'pear', 'lion', 'banana']
   
with open('animals.out', 'w') as animals_f, open('fruits.out', 'w') as fruits_f:
    for item in items:
        if item in ['dog', 'cat', 'lion']:
            animals_f.write(item + '\n') 

        if item in ['apple', 'pear', 'banana']:
            fruits_f.write(item + '\n')
```

