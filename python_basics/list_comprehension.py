
# List Comprehension examples , conditions

l1 = [x for x in range(2,10)]

print("L1 - ", l1)

l2 = [x*2 for x in range(6)]

print("L2 - ", l2)

l3 = [x**2 for x in range(6) if x % 2 == 0]

print("L3 - ", l3)

# flatten a 2D list into a 1 D list
k = [[1,2,3], [4,5,6]]

l4 = [x for row in k for x in row]

print("L4 - ", l4)

# apply square in a 2 d list to elements

l5 = [[y**2 for y in row] for row in k]
print("L5 - ", l5)

# Create tuples from list comprehensions
X = ['A', 'B', 'C']
Y = ['a', 'b', 'c']

l6 = [(x,y) for x in X for y in Y]
print("L6 - ", l6)