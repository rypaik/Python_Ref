# Async in python  - ASYNCIO

[Asyncio: Understanding Async / Await in Python](https://www.youtube.com/watch?v=bs9tlDFWWdQ)

[Asynchronous vs Multithreading and Multiprocessing Programming (The Main Difference)](https://www.youtube.com/watch?v=0vFgKr5bjWI&t=10s)

[AsyncIO & Asynchronous Programming in Python](https://www.youtube.com/watch?v=6RbJYN7SoRs)

[Python Asynchronous Programming - AsyncIO & Async/Await](https://www.youtube.com/watch?v=t5Bo1Je9EmE)

```other
# basic sync program
def foo():
	return


foo()
print("Finished Loading def of foo() and executing")
```

```other
# basic async program
import asyncio

# 1. make a coroutine

async def main():
	print('coroutine')

	#4 call the function to wait on - not really async
	# await('this calls the wait function')

	# 4 truly async
	task = asyncio.create_task(foo('text'))
	await asyncio.sleep(0.5)
   #	await = task
	print('finished')


# 3 make another function
async def foo(txt):
	print(txt)
	await asyncio.sleep(10)


# 2. creates an event loop
asycino.run(main())
```

```other
# Full sample of async


import asyncio

async def fetch_data():
	print('start fetchign')
	away asyncio.sleep(2)
	print('done fetching')
	return {'data': 1}


async def print_numbers():
	for i in range(10):
		print(i)
		await asyncio.sleep(0.25)

async def main():
	task1 = asyncio.create_task(fetch_data())
	task2 = asyncio.create_task(print_numbers())

	value = await task1
	print(value)
	await task2


asyncio.run(main())
```

