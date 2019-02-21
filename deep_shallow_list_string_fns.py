import itertools
import random
import statistics

ab = [4,1,67,33,56,90]
print(sorted(ab))

cd = ['Abhik', 'aly', 'shekhar','Linkedin']
cards = ["Ace", "King", "Queen","Jack"]

print(sorted(cd))
print(sorted(cd, key= lambda word: word.lower()))

ab_map = {34:'Abhik', 22:'ally', 2:'alisha', 15:'surbhi'}
print(sorted(ab_map.values()))

print(random.random())
print(random.randrange(3))

print(random.randrange(1,7))
print(random.choice(cd))

print(random.sample(range(100), 5))

random.shuffle(cards)
print(cards)

for x in itertools.count(20):
	if x<100:
		print(x)

for y in itertools.cycle("Abhik"):
	print(y)

# Check for Shallow and Deep copy in python, check for the ids
a = [1,2,3,4]
a1 = [1,2,3,4]
c = [1,2,3,4,5,6,7]
b = a
print(type(b), " - ", id(b), " - ", id(a))
b1= list(a)
print(type(b1), " - ", id(b1), " - ", id(a))

# check the reverse in-place function vs the iterator reversed function
a.reverse()
print(a)
print([x for x in reversed(a1)])

# rotate a list from position k
k = 2
print("Rotated List - ", c[k:]+c[:k])
