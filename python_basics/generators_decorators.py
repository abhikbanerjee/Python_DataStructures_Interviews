
# See a simple generator function


def main():
	# for i in inclusive_range(22):
	# for i in inclusive_range(2, 22):
	for i in inclusive_range(2, 22, 5):
		print(i, end= " ")
	print()

	item_counts = {"key1":2, "key2":5, "key6":9}
	print(type(item_counts))
	print(type(item_counts.values()))
	print(item_counts.values())
	print(len(item_counts))
	print(item_counts.keys())


def inclusive_range(*args):
	start = 0
	step = 1
	if len(args)<1:
		raise Exception(f"Minimum number of variables needed is 1 , got {len(args)}")
	if len(args) == 1:
		stop = args[0]
	if len(args)==2:
		(start, stop) = args
	if len(args) == 3:
		(start, stop, step) = args
	if len(args) > 3:
		raise Exception(f"Maximum number of variables allowed is 3 , got {len(args)}")

	i = start
	while i<=stop:
		yield i
		i += step

if __name__ == "__main__":
	main()



