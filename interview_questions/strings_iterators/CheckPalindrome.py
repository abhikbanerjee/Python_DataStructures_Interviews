

def is_palindrome(str_to_check):
	str_len = len(str_to_check)
	# initialize 2 pointers to read from front and back
	i,j = 0, len(str_to_check)-1

	while i<j:
		if not str_to_check[i].isalnum():
			i +=1
			continue
		if not str_to_check[j].isalnum():
			j -=1
			continue
		#check the alphanumeric characters are the same
		if str_to_check[i] != str_to_check[j]:
			return False

		i += 1
		j -= 1
	#checked all the characters and it breaks when i equals to j or i is greater than j
	return True


def main():
	str_name = "HellolleH"
	str_name1 = "Abhik"
	str_name2 = "He%%$$ll&&oll***eH"


	flag = is_palindrome(str_name)
	if flag:
		print("The String is a palindrome")
	else:
		print("The String is Not a palindrome")

if __name__=="__main__":
	main()