roman_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


def roman_to_int(self, s: str) -> int:
	new_str = "".join(reversed(s))
	sum = roman_int[new_str[0]]
	for ch in range(1, len(new_str)):
		if roman_int[new_str[ch]] < roman_int[new_str[ch - 1]]:
			sum -= roman_int[new_str[ch]]
		else:
			sum += roman_int[new_str[ch]]
	return sum


