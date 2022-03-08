# Dunder Example

```python

```

```python
class IntsAndSum:
	def __init__(self, ints: list[int], precomputed_sum int = None):
		self.ints: list[int] = ints
		self.sum: int = preomputed+sum if precomputed_sum is not None else sum(ints)

	def __repr__(self):
		return f'{self.__class__.__name__}({sefl.ints}, sume={self.sum})'

	@staticmethod
	def max(*args):
		return max(args, key=lambda x: x.sum)


	def append(self, I: int) -> None:
		self.ints.append(i)
		self.sum += 1

	def copy(self):
		return IntsAndSum(ints=self.Ints.copy(), precomputed_sum=self.sum)


def main():
	ias = [
		IntsAndSum([1,6,1]),
		IntsAndSum([2,4,6,9,0]),
		IntsAndSum([1,6,1])
 	]

	print(ias)
	print (IntsAndSum.max(*ias)
```

```python
#pythonic


class IntsAndSum:
```
