import os


def string_concatenate(my_str: str):
	if not my_str:
		return "invalid input"
	char_count = {}
	char_list = []
	result = []
	i = 0
	while i< len(my_str):
		ch = my_str[i]
		if ch not in char_count:
			char_count[ch] = 1
			char_list.append(ch)
		else:
			char_count[ch] += 1
		i += 1
	# Loop over the list
	for k in char_list:
		num_count = char_count[k]
		if num_count % 2 == 1:
			result.append(k)

	if len(result)==0:
		return "Empty String"
	else:
		return "".join(result)


def superReducedString(my_str:str):
	while not is_reduced(my_str):
		res = []
		i=0
		while i < len(my_str):
			if i == len(my_str)-1:
				res.append(my_str[len(my_str)-1])
				break
			if my_str[i] != my_str[i+1]:
				res.append(my_str[i])
				i += 1
			else:
				i += 2
		my_str = "".join(res)

	if len(my_str) == 0:
		return "Empty String"
	else:
		return "".join(my_str)


def is_reduced(str_to_check):
	if len(str_to_check)==1:
		return True
	check = True
	for i in range(0, len(str_to_check)-1):
		if str_to_check[i] == str_to_check[i+1]:
			check = False
			break

	return check


#test the function
# print(string_concatenate("aabbccc"))
# print(string_concatenate("aabbbcccddb"))
# print(string_concatenate("aaabbcccdd"))
# print(string_concatenate("aabbbcccddd"))
# print(string_concatenate("zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"))

#Test Case 4
# op = string_concat("zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh")
#
# if op == "tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh":
# 	print("test Case Passed")
# else:
# 	print("test Case Failed")

#Test Case 5
# print(string_concat("ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx"))
#Test case 6
# print(superReducedString("ggppppuurrjjooddwwyyllmmvvffddmmppxxaabbddddooppxxgghhhhvvnneeqqyyttbbffvvjjiiaammmmddddhhyywwqqiijj"))
#
#
# print(superReducedString("mwkommokwmxjivkkvijxshscbbcshsgwdyqqydwgzpnlzzlnpzvfeaiiaefvyeqjccjqeymhqhiihqhmhaomkkmoahhddymmyddh"))
# print(string_concat("zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"))