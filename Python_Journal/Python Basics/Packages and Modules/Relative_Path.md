# Relative_Path

[Simple trick to work with relative paths in Python](https://towardsdatascience.com/simple-trick-to-work-with-relative-paths-in-python-c072cdc9acb9)

```Bash
relative_path
    ├── data
    │   └── mydata.json
    └── processes
        └── load_data.py
```

# Absolute Path

```python
# get current file directory

print(__file__)
```

```Bash
# from inside load_data.py

import json

f = open(r'C:\projects\relative_path\data\mydata.json')

data = json.load(f)
```

# Calculate dirname of **file**

```python
import os
print(os.path.dirname(__file__))

# Results in
# C:\projects\relative_path\processes
```

# Navigating Dir

```python
import os
print(os.path.join(os.path.dirname(__file__), '..', 'data', 'mydata.json'))
# results in C:\projects\relative_path\processes\..\data\mydata.json

print(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'data', 'mydata.json')))
# results in C:\projects\relative_path\data\mydata.json
```

# Navigation Troubles

```python
import os
print(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'mydata.json')))
```

# Solution

```python
import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
```

```python
import os
from config.definitions import ROOT_DIR
print(os.path.join(ROOT_DIR, 'data', 'mydata.json'))
```

