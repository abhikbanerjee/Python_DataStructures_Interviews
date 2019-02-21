from collections import defaultdict

#define an empty dict
my_dict1 = {"abhik":"2", "hello":"world"}
my_dict2 = dict.fromkeys(["abhik","surbhi", "alisha"])
my_dict3 = dict(x="abhik", y="surbhi")

my_set1 = set(("2", "5", "5", "6"))
my_set2 = {"2", "5", "5", "6"}

print(my_set1)
print(my_set2)

# print(my_dict2)

def call_iterator(li):
	"""
	basic usages of iterators
	:param li: list element to use iter and next methods on
	:return: Null
	"""
	counte = iter(li)
	print(next(counte))
	print(next(counte))
	print(next(counte))
	print(next(counte))
	# print(next(counte))


class MyIterators:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <=20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration


def main():

	# Call the iterator on the list object
	# l1 = [2,4,5,7]
	# call_iterator(l1)

	# Create an iterator and next objects from the MyIterator class
	myclass = MyIterators()
	myiter = iter(myclass)
	# for i in range(100):
	# 	print("Value = ", next(myiter))

if __name__=="__main__":
	main()