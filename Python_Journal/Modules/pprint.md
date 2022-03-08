# pprint

[pprint — Data pretty printer — Python 3.10.2 documentation](https://docs.python.org/3/library/pprint.html)

```shell
## pprint builtin pythonmodule
import pprint


# calling pprint
pprint.pprint("Hello pretty printer")
my_printer = pprint.PrettyPrinter()
my_printer.pprint("Hello pretty printer")
```

`pprint()` method will use the default settings of the library.

When you create your own `PrettyPrinter()` object, you can override those default configurations upon creation. Now, when using the `pprint()` method from your created object, the configurations you set will be used.

```python
# Using pprint.pprint()
import pprint
coordinates = [
   {
       "name": "Location 1",
       "gps": (29.008966, 111.573724)
   },
   {
       "name": "Location 2",
       "gps": (40.1632626, 44.2935926)
   },
   {
       "name": "Location 3",
       "gps": (29.476705, 121.869339)
   }
]
pprint.pprint(coordinates, depth=1)
# [{...}, {...}, {...}]
pprint.pprint(coordinates)
"""
[{'gps': (29.008966, 111.573724), 'name': 'Location 1'},
 {'gps': (40.1632626, 44.2935926), 'name': 'Location 2'},
 {'gps': (29.476705, 121.869339), 'name': 'Location 3'}]
"""
```

```python
# Using PrettyPrinter()

import pprint
my_printer = pprint.PrettyPrinter(depth=1)
coordinates = [
   {
       "name": "Location 1",
       "gps": (29.008966, 111.573724)
   },
   {
       "name": "Location 2",
       "gps": (40.1632626, 44.2935926)
   },
   {
       "name": "Location 3",
       "gps": (29.476705, 121.869339)
   }
]
my_printer.pprint(coordinates)
# [{...}, {...}, {...}]
```

```python
# shortcut through import


from pprint import pprint
pprint([(3,5),(7,5),(4,3)])
```

Configurable Parameters

- stream (None): When you want to pretty print to a file, use the stream property. Its default behavior—with a value of None—is to use sys.stdout
- indent (1): The number of spaces to indent each line, this value can help when specific formatting is needed.
- width (80): The maximum number of characters in each line. If a line exceeds this value, then the remaining text will be wrapped on the line(s) below.
- depth (None): The number of depth levels (nested data types) to be displayed. The default is to show all data. When specified, data beyond the depth limit will be displayed as ... nested in the appropriate data type syntax.
- compact (False): When enabled, the compact property will consolidate complex data structures within lines as long as they do not exceed width limitations.
- sort_dicts (True): By default, a pretty printed dictionary will display the key-value pairs sorted by the key name. When this is set to False, the dictionary keys will be displayed by the order of insertion.

# **PrettyPrinter Instance Methods**

- PrettyPrinter.pformat(object)

   Return the formatted representation of object. This takes into account the options passed to the PrettyPrinter constructor.

- PrettyPrinter.pprint(object)

   Print the formatted representation of object on the configured stream, followed by a newline.

The following methods provide the implementations for the corresponding functions of the same names. Using these methods on an instance is slightly more efficient since new PrettyPrinter objects don’t need to be created.

- PrettyPrinter.isreadable(object)

   Determine if the formatted representation of the object is “readable,” or can be used to reconstruct the value using eval(). Note that this returns False for recursive objects. If the depth parameter of the PrettyPrinter is set and the object is deeper than allowed, this returns False.

- PrettyPrinter.isrecursive(object)

   Determine if the object requires a recursive representation.

This method is provided as a hook to allow subclasses to modify the way objects are converted to strings. The default implementation uses the internals of the saferepr() implementation.

- PrettyPrinter.format(object, context, maxlevels, level)

   Returns three values: the formatted version of object as a string, a flag indicating whether the result is readable, and a flag indicating whether recursion was detected. The first argument is the object to be presented. The second is a dictionary which contains the id() of objects that are part of the current presentation context (direct and indirect containers for object that are affecting the presentation) as the keys; if an object needs to be presented which is already represented in context, the third return value should be True. Recursive calls to the format() method should add additional entries for containers to this dictionary. The third argument, maxlevels, gives the requested limit to recursion; this will be 0 if there is no requested limit. This argument should be passed unmodified to recursive calls. The fourth argument, level, gives the current level; recursive calls should be passed a value less than that of the current call.

