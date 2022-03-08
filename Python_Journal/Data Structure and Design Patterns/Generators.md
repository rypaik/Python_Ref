# Generators

[TODO](craftdocs://open?blockId=9ADA0568-4EB7-4146-A67D-473D3A2732AE&spaceId=5245eaa1-107f-3a8d-c5b7-4e9a619103cb)

[source]([https://towardsdatascience.com/how-to-work-with-python-generators-d30d8d0af7fa](https://towardsdatascience.com/how-to-work-with-python-generators-d30d8d0af7fa))

A generator allows you to _declare a function that behaves like an iterato_r. This means you can use a generator in a for-loop or a list/dict comprehension in the same way as if you are using a list or tuple.

[[TAGS_TOC/Generators TOC]]: Advantages of Using Generators

[Separation of Concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) and [Single Responsibility](https://en.wikipedia.org/wiki/Single-responsibility_principle). I*n a generator, you can focus on how to get the data.* *In the for-loop* where you apply the generator, you can focus on what really matters i.e. *processing the data*.

W*ith generators you can mitigate memory issues* when working with large datasets.

[[TAGS_TOC/Generators TOC]]: Basic Code

the `yield` keyword, it is turned into a generator function.

*The yield statement yields* the value to the right of it to the caller. Furthermore, *it pauses the function* saving all its states, and later continues from where it paused on subsequent invocations.

As it just pauses the function you can call yield multiple times within a function. This is in huge contrast to the `**return**`statement which you can only call once as it terminates a function

```python
from typing import Iterator
def numbers_123() -> Iterator[int]:
    yield 1
    yield 2
    yield 3

for number in numbers_123():
    print(number)
```

Intermediate Example

[[TAGS_TOC/Generators TOC]]:

```python
from typing import Iterator
# This creates the generator that produces tuples of ints and floats
# with the float being the sqrt of the int. It does that for all uneven
# numbers between 0 and 99 
# soun is a generator using list comprehension

soun : Iterator[tuple[int, float]] = ((i, i**0.5) for i in range(100) if i % 2)

for number, sqrt_number in soun:
    print(f"{number=},{sqrt_number=}")
    if number > 50:
        break
```

Yields from an Iterable

```python
from typing import Iterator

def some_generator() -> Iterator[float|int]:
    yield from [1,-1,90]
    yield from (i**2 for i in range(10))
```

[TODO](craftdocs://open?blockId=9ADA0568-4EB7-4146-A67D-473D3A2732AE&spaceId=5245eaa1-107f-3a8d-c5b7-4e9a619103cb) :Run and Analyze

Example

- Download images from a server and after that detect all cats and dogs in every image

```python
from numpy.typing import NDArray
import requests
from typing import Iterator
images_url = "https://fake-images.com/api/images"

def get_urls() -> Iterator[str]:
    current_page, images_per_page = 0, 100
    grabbed_all_images = False
    while not grabbed_all_images:
        params = {"current_page": current_page, "image_per_page": images_per_page}
        image_urls = requests.get(images_url, params=params).json()
        yield from image_urls
        grabbed_all_images = len(image_urls) != images_per_page
        current_page += 1


def get_images(
    urls: Iterator[str],
    max_images: int | None = None
) -> Iterator[NDArray[float]]:
    for i, url in enumerate(urls):
        if max_images and i == max_images:
            break
        # to_numpy_array would be a function that turns the stream into a numpy array
        image_data = to_numpy_array(requests.get(url), stream=True)
        yield image_data


urls = get_urls()
for image in get_images(urls, 1000):
    cats_and_dogs = get_cats_and_dogs(image)
```

