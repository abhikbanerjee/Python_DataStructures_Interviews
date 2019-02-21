class Animal:

	def __init__(self, **kwargs):
		if 'type' in kwargs: self._type = kwargs['type']
		if 'name' in kwargs: self._name = kwargs['name']
		if 'sound' in kwargs: self._sound = kwargs['sound']

	def type(self, t = None):
		if t: self._type = t
		try:
			return self._type
		except AttributeError:
			return None

	def name(self, n = None):
		if n:
			self._name = n
		try:
			return self._name
		except AttributeError:
			return None

	def sound(self, s = None):
		if s:
			self._sound = s
		try:
			return self._sound
		except AttributeError:
			return None


class Duck(Animal):
	def __init__(self, **kwargs):
		self._type = 'duck'
		if 'type' in kwargs: del kwargs['type']
		super().__init__(**kwargs)


class Dog(Animal):
	def __init__(self, **kwargs):
		self._type = 'dog'
		if 'type' in kwargs: del kwargs['type']
		super().__init__(**kwargs)


def print_animal(o):
	if not isinstance(o, Animal):
		raise TypeError('print_animal() requires an Animal instance')
	print(f'The {o.type()} with name {o.name()} makes sound {o.sound()}')


def main():
	o1 = Dog(name="fluffy", sound="barks")
	o2 = Duck(name = "tomy", sound="quacks")
	print_animal(o1)
	print_animal(o2)


if __name__=="__main__":
	main()

