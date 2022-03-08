# Pathlib Module

# Benefits of Pathlib

- cross-platform path support (allows unix paths across all platforms)
```python

```

- smart path joining with the “/” operator
- lots of useful tools (Path.iterdir(), Path.stem, [Path.name](http://Path.name), Path.suffix, Path.is_file(), Path.is_dir(), etc….)
- more readable than os.path module
- supported path datatype by many packages (FastAPI, Pydantic, Pandas, etc..)

path.is_file()

path.is_dir()

path.iterdir()

path.name

[TODO](craftdocs://open?blockId=9ADA0568-4EB7-4146-A67D-473D3A2732AE&spaceId=5245eaa1-107f-3a8d-c5b7-4e9a619103cb): test and run - pathlib snippet

FIND FILES IN FOLDER TREE

```python
from pathlib import Path

def find_files(name: str, path: Path):
	# if path is not a directory we do not need to iterate
	if all ((path, path.is_file(), name in path.name)):
		yield path
	
	# if path is a folder iterate over all contained folders and files
	elif path and path.is_dir():
		for p in path. iterdir():
			# "yield from" is required for recursive generator functions (our find files)
			yield from find_files (name=name, path=p. absolute())

for path in find_files("example", Path(".")):
print(path)
```

calling this snippet

???

## Creating File within Non-Existing Folder

```python
p1 = th("./docs/")
p2 = Path("./docs/getting-started/page-1.md")
print (p2. relative_to(p1))
```

## Find Relative Paths from Full ones

```python
# path.relative_to()

p1 = Path("./docs/")
p2 = Path("./docs/getting-started/page-1.md")
print(p2.relative_to(p1))
```

