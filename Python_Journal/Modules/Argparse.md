# Argparse

Using `argparse` is how you let the user of your program provide values for variables at runtime. It’s a means of communication between the writer of a program and the user.

```python
# videos.py
import argparse

parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('indir', type=str, help='Input dir for videos')
parser.add_argument('outdir', type=str, help='Output dir for image')

args = parser.parse_args()

print(args.indir)
```

in shell pass the args

\>>> python videos.py /videos /images

## positional argument

```python
parser.add_argument('indir', type=str, help='Input dir for videos')
```

## optional arguments

Optional arguments are created just like positional arguments except that they have a `'--'` double dash at the start of their name or ‘-' a single dash

```python
parser.add_argument('-m', '--my_optional')
```

## Get Descriptions of Arguments

\>>> python videos.py —help

FULL EXAMPLE

```python
# my_example.py
import argparseparser = argparse.ArgumentParser(description='My example explanation')

parser.add_argument(
    '--my_optional',
    default=2,
    help='provide an integer (default: 2)'
)

my_namespace = parser.parse_args()
print(my_namespace.my_optional)
```

in shell

\>>> python my_example.py

\>>> python my_example.py —my_optional=3

