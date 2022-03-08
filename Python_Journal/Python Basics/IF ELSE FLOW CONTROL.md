# IF ELSE FLOW CONTROL

[source]([https://towardsdatascience.com/python-if-else-statement-in-one-line-ternary-operator-explained-eca2be64b7cc](https://towardsdatascience.com/python-if-else-statement-in-one-line-ternary-operator-explained-eca2be64b7cc))

IF ELSE

```python
age = 19

if age < 18:
    print('Go home.')
else:
    print('Welcome!')
```

IF ELSE ELIF

```python
age = 17

if age < 16:
    print('Go home.')
elif 16 <= age < 18:
    print('Not sure...')
else:
    print('Welcome!')
```

TERNARY OPERATOR PRIMER

```python
# a if condition else b

# a if condiiton1 else b if condition2 else c
```

SINGLE LINE IF NO ELSE

```python
age = 17

if age < 18: print("Still a minor")



# another use
def print_stuff():
    print('Go home.')
    print('.......')
    print('Now!')
    
age = 17    
    
if age < 18: print_stuff()
```

SINGLE LINE IF ELSE

```python
age = 19
outcome = 'Go home.' if age < 18 else 'Welcome!'
print(outcome)
```

SINGLE LINE IF ELIF ELSE STATEMENT

```python
age = 17
outcome = 'Go home.' if age < 16 else 'Not sure...' if 16 <= age < 18 else 'Welcome'
print(outcome)
```

SINGLE LINE CONDITIONAL FOR LIST OPERATIONS

```python
# [a if condition else b for element in array]

['+' if i > 5 else '-' for i in range(1, 11)]
```

EXAMPLE: DID STUDENT PASS

```python
# list of dictionaries - each student is a dictionary object with 2 keys

students = [
    {'name': 'Bob', 'score': 42},
    {'name': 'Kelly', 'score': 58},
    {'name': 'Austin', 'score': 99},
    {'name': 'Kyle', 'score': 31}
]


outcomes = []
for student in students:
    if student['score'] > 50:
        outcomes.append(f"{student['name']} passed the exam!")
    else:
        outcomes.append(f"{student['name']} failed the exam!")
        
print(outcomes)


# short version - identical results
outcomes = [f"{student['name']} passed the exam!" if student['score'] > 50 else f"{student['name']} failed the exam!" for student in students]
print(outcomes)
```

