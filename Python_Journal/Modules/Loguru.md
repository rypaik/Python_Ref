# Loguru

[Overview — loguru documentation](https://loguru.readthedocs.io/en/stable/overview.html)

[loguru](https://pypi.org/project/loguru/)

[GitHub - Delgan/loguru: Python logging made (stupidly) simple](https://github.com/Delgan/loguru)

[API Reference — loguru documentation](https://loguru.readthedocs.io/en/stable/api.html)

```python
# Basic Starting


from loguru import logger

logger.debug("Simple Logging")


# no handler, no formatter, no filter - one function
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module"m level="INFO")


# sending log  to a file
logger.add("file_{time}.log", rotation="1 week")


#string formatting using braces
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")



# logging with colors
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
```

```python
# Exceptions catching in threads or main
@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)
```

```python
# Fully Descriptive

logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)
```

