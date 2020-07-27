

def str_to_binary(name:str) -> None:
	res = ''.join(format(ord(i), 'b') for i in name)
	print(str(res))


str_to_binary("abhik")
str_to_binary("5")