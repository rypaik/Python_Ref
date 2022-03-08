# Modules vs Packages

[Python Modules vs Packages - Python Geeks](https://pythongeeks.org/python-modules-vs-packages/)

[https://www.w3schools.com/python/python_modules.asp](https://www.w3schools.com/python/python_modules.asp)

MODULES

any .py file with encapsulated code (function, object)

```python
# a module single_mod.py

def display():
    print("this is a module")

if __name__ == "__main__":
    display()
```

```python
# importing module

import single_mod.py

pythongeeks.display()
```

```python
# all function or object imports

from single_mod.py import *
display()


# ------------------------------------ #

# single obejct import - more performant

from single_mod.py import display
display()


# ------------------------------------ #

# importing with alias

import single_mod as sm
sm.display()
```

---

\#dir()

```python
# get list all attributes and funcitons with 
# dir()


import single_mod

print(dir(single_mod))

pprint(dir(single_mod))
```

---

Variables in Module

```python
# mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

```python
import mymodule

a = mymodule.person1["age"]
print(a)
```

Variation

```python
# mymodule.py

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

```python
from mymodule import person1

print (person1["age"])
```

```python
# selecting multiple functions from module
from fibo import fib, fib2


# compound import
from fibo import fib as fibonacci
```

---

Executing Modules as Scripts

```python
# CLI module execution
python fibo.py <arguments>
python fibo.py 50
```

```python
# fibo.py

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Intra Package References

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

```python
from . import echo
from .. import formats
from ..filters import equalizer


# relative imports are based on the name of the current module. 
# Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.
```

---

\#pycache

[6. Modules — Python 3.10.2 documentation](https://docs.python.org/3/tutorial/modules.html#compiled-python-files)

---

[[PYTHON TODO]]: PYTHONPATH

[Python import, sys.path, and PYTHONPATH Tutorial](https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial#toc-13)

[1. Command line and environment — Python 3.10.2 documentation](https://docs.python.org/3/using/cmdline.html#environment-variables)

When a module named `spam` is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named `spam.py` in a list of directories given by the variable [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path). [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path) is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).
- [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names, with the same syntax as the shell variable `PATH`).
- The installation-dependent default (by convention including a `site-packages` directory, handled by the [`site`](https://docs.python.org/3/library/site.html#module-site) module).

\#PYTHONPATH

```python
from os import environ, pathsep

print(environ['PYTHONPATH'].split(pathsep))
```

\#site_module #sys.path

You can also use the `site` module to modify `sys.path`

```python
import site
import sys

site.addsitedir('/the/path')  # Always appends to end
print(sys.path)
```

---

# PACKAGES VS MODULES

The following are some of the distinctions between Modules and Packages:

- A Package is a directory containing numerous modules and sub-packages, whereas a Module is [a.py](http://a.py) file containing Python code.
- An **init**  .py file is required to create a package. There is no such necessity when it comes to creating modules.
- We can import all objects in a module at once by using the asterisk (*) operator but we can’t import all modules in a package at once.

### Packages and Modules and Functions

The principle is the same for functions, modules, and packages. They want to make it as simple as possible for code to be reused.

Their core idea is the same, despite the fact that they appear and operate differently.

Multiple Python statements and expressions make up a function.  Multiple Python functions make up a module and multiple Python modules make up a Package. The below image illustrates this precisely.

```python
# importing plotting subpackage from pandas package

import pandas.plotting

print(dir(pandas.plotting)[:3])
```

Directory structure of a Package

```python
# Directory structure of my_package/
my_package/
my_package/__init__.py
my_package/__main__.py
my_package/some_other_module.py
```

```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

---

## How **init** and **main** work

Names that start and end with double underscores, often called 'dunders', are special names in Python. Two of them are special names related to modules and packages: `__init__` and `__main__`. Depending on whether you are organizing your code as a package or a module, they are treated slightly differently.

We will look at the difference between a module and a package in a moment, but the main idea is this:

- When you import a package it runs the `__init__.py` file inside the package directory.
- When you execute a package (e.g. `python -m my_package`) it executes the `__main__.py` file.
- When you import a module it runs the entire file from top to bottom.
- When you execute a module ir runs the entire file from top-to-bottom *and* sets the `__name__` variable to the string `"__main__"`.

\#python_cli

`python my_module.py` - Run the file directly with Python:

`python -m my_module` - Invoke the module with `-m` flag:

`python -m package`  - imports a package at command line runtime

`python -c "import my_module"` - Import the module from another Python file

`python -c "import my_module; my_module.my_function()"` - Import and call the function defined:

