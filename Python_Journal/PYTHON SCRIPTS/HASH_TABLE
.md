# HASH_TABLE

IF ELSE LOOKUP

```python
# Get the user input
character = input('Enter your character type: ').strip()

# If-else sequence
if character == 'Wizard':
  do_magic()
elif character == 'Gladiator':
  fight_opponent()
elif character == 'Doctor':
  heal_wounds()
elif character == 'Horse':
  run_fast()
elif character == 'Horseman':
  ride_horse()
elif character == 'Dragon':
  breathe_fire()
else:
  print('Invalid character type')
```

HASH TABLE - DICTIONARY OR MAP VERSION

```python
# Character hash table (aka map or dictionary)
characters_table = {
  'Wizard': do_magic,
  'Gladiator': fight_opponent,
  'Doctor': heal_wounds,
  'Horse': run_fast,
  'Horseman': ride_horse,
  'Dragon': breathe_fire
}

# Get user input
character = input('Enter your character type').strip()
# Get the action from the hash table
action = characters_table.get(character)
# Check if the table actually contains the action
if action is None:
  print('Invalid character type')
else:
  # If the action is not None, execute it
  action()
```

