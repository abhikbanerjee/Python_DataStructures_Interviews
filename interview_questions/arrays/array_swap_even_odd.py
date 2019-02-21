
def odd_even_swap(li: list):
	lower_bound = 0
	upper_bound = len(li)-1

	while lower_bound<upper_bound:
		if li[lower_bound]%2 == 0:
			li[lower_bound], li[upper_bound] = li[upper_bound], li[lower_bound]
			upper_bound -= 1
		else:
			lower_bound += 1
	return li


def main():
	li = [2, 5, 7, 9, 11, 13, 12, 16]
	li_odd_even = odd_even_swap(li)
	print(li_odd_even)


if __name__ == "__main__":
	main()