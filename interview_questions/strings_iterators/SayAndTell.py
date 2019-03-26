import itertools


def find_say_and_tell_n(s: str = "1", n:int = 5) -> str:

		for i in range(0,n-1):
			s = "".join([(str(len(list(v)))) + str(k) for k,v in (itertools.groupby(s))])

		return s


print(find_say_and_tell_n("1", 5))



