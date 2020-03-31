mapping = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# Given the mapping below, for a given phone number generate all the possible elemental permutations


def generate_phone_combinations(number: str):
	if len(number) == 0:
		return []

	def add_combinations(digit: int):
		if digit == len(number):
			final_combinations.append("".join(partial_combinations))
		else:
			mapp = mapping[int(number[digit])]
			for c in mapp:
				partial_combinations[digit] = c
				add_combinations(digit+1)

	final_combinations, partial_combinations = [], [0]*len(number)
	add_combinations(0)
	return final_combinations


def main():
	number = "23"
	# number = "23364"
	final_comb = generate_phone_combinations(number)
	# print(len(final_comb))
	print(final_comb)


if __name__ == '__main__':
	main()




