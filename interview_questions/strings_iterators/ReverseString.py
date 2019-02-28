

def reverse_string(str_to_reverse):
	i,j = 0, len(str_to_reverse)-1
	rev = [0] * len(str_to_reverse)

	while j > -1:
		rev[i] = str_to_reverse[j]
		j -= 1
		i += 1

	return "".join(rev)


print(reverse_string("Abhik"))