

# Find the Greedy approach for the maximum balanced string - LC:
def balanced_string_split(s: str) -> int:
	if s is None or len(s) < 2:
		return 0
	# count is the running counter which uses greedy approach to count the R and L characters seen
	# bal_count is the final balance counts to be returned which in a greedy approach will be the max ,
	count = 0
	bal_count = 0
	for i in range(len(s)):
		# We increment the count as soon as we see a L and decrement as soon as we see a R
		if s[i] == "L":
			count += 1
		if s[i] == "R":
			count -= 1
		# as soon as we see a 0 for count we increment the balance count value
		if count == 0:
			bal_count += 1
	return bal_count


inp1 = "RLRRLLRLRL"
inp2 = "RLLLLRRRLR"
inp3 = "LLLLRRRR"
inp4 = "RLRRRLLRLL"

print(balanced_string_split(inp1))
print(" ")
print(balanced_string_split(inp2))
print(" ")
print(balanced_string_split(inp3))
print(" ")
print(balanced_string_split(inp4))
print(" ")