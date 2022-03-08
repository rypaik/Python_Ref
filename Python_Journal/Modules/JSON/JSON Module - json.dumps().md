# JSON Module - json.dumps()

[You Must Know Python JSON Dumps, But Maybe Not All Aspects](https://towardsdatascience.com/you-must-know-python-json-dumps-but-maybe-not-all-aspects-fa8d98a76aa0)

```python
# json.dumps() in steps


import json


my_dict = {
    'name': 'Chris',
    'age': 33
}


# --------------------------------- #

# Writing to a JSON file
with open('my.json', 'w') as f:
    json.dump(my_dict, f)

# --------------------------------- #


# audoindent
json.dumps(my_dict, indent=2)


# --------------------------------- #

# customized separators
json.dumps(my_dict, separators=(',', ':'))

# or
json.dumps(
  my_dict, 
  separators=('', ' => '), 
  indent=2
)

# --------------------------------- #

# Sort Keys
json.dumps({
    'c': 1,
    'b': 2,
    'a': 3
}, sort_keys=True)



# --------------------------------- #

# Skip non-basic key types
json.dumps({
    'name': 'Chris',
    (1,2): 'I am a tuple'
}, skipkeys=True)



# --------------------------------- #

# Non-ASCII Characters
json.dumps({
    'name': 'Chris',
    (1,2): 'I am a tuple'
})



# --------------------------------- #
# Circular Check
my_dict = {
    'dictionary': None
}

my_dict['dictionary'] = my_dict

# returns ValueError: circular reference

# Fix
json.dumps(my_dict, check_circular=False)



# --------------------------------- #

# Allow NAN


json.dumps({
    'my_number': np.nan
}, allow_nan=False)


# --------------------------------- #


# Customised JSON Encoder

# Throws TypeError
from datetime import datetimemy_dict = {
    'alarm_name': 'get up',
    'alarm_time': datetime(2021, 12, 3, 7)
}


# custom class
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, obj)

json.dumps(my_dict, cls=DateTimeEncoder, indent=2)
```

