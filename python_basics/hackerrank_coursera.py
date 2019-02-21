from collections import Counter
from itertools import product


def multiset_subset(multiset):
	counts = Counter(multiset)
	for sub_counts in product(*[range(n + 1) for n in counts.values()]):
		yield Counter(dict(zip(counts.keys(), sub_counts))).elements()


def main():
	multiset = ["apple", "apple", "banana"]
	multiset_subset(multiset)


if __name__ == '__main__':
	main()