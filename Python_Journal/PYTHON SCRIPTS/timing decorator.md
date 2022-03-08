# timing decorator

[timeit versus timing decorator](https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator)

```python
from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap




@timing
def f(a):
    for i in range(a):
        i = i+1
    return i


f(10000)
```

