from math import ceil


def print_egyptian_fn(numr :int, denom :int) -> None:
	if numr is None or denom is None or numr >= denom:
		return
	values = []
	while numr != 0:
		bal = ceil(denom/numr)
		values.append(bal)
		numr = (numr * bal) - denom
		denom = denom * bal

	for i in range(len(values)):
		if i != len(values)-1:
			print(f"1/{values[i]}+")
		else:
			print(f"1/{values[i]}")

print_egyptian_fn(6,14)
