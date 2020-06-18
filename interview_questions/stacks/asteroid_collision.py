# Ref - https://leetcode.com/problems/asteroid-collision/

from typing import List

# Asteroid Collision problem, size is represented value and direction by sign (+ve is right and -ve is left)
# Asteroids may collide, and if same size both explode, or the larger one remains,
# Asteroids travelling in same direction never collide - LC 735
def asteroid_collision(asteroids):
	asteroid_stack = []
	flag = True
	# while flag:
	for asteroid in asteroids:
		flag = True
		if len(asteroid_stack) == 0:
			asteroid_stack.append(asteroid)
			continue
		prev_val = asteroid_stack[-1]
		if sign(prev_val) == sign(asteroid):
			asteroid_stack.append(asteroid)
			flag = False
		elif sign(prev_val) == -1 and sign(asteroid) == 1:
			asteroid_stack.append(asteroid)
			flag = False
		while flag:
			if len(asteroid_stack)==0:
				flag = False
				continue
			prev_val = asteroid_stack.pop()
			if abs(prev_val) > abs(asteroid):
				val_to_append = prev_val
			elif abs(prev_val) == abs(asteroid):
				continue
			else:
				val_to_append = asteroid
			if sign(asteroid_stack[-1]) == sign(val_to_append) or (sign(asteroid_stack[-1]) == -1 and sign(val_to_append) == 1):
				flag = False
				asteroid_stack.append(val_to_append)
			else:
				val = asteroid_stack.pop()
				if abs(val)>abs(val_to_append):
					val_to_append = val
	return asteroid_stack


def sign(x: int) -> int:
	if x<0:
		return -1
	else:
		return 1


def asteroid_collision_amit(asteroids: List[int]) -> List[int]:
	neg_elem = []
	st = []
	for asteroid in asteroids:
		if len(st) == 0:
			if asteroid < 0:
				neg_elem.append(asteroid)
			else:
				st.append(asteroid)
		elif asteroid < 0:
			last_elem = st[-1]
			if abs(last_elem) == abs(asteroid):
				st.pop()
			else:
				while st and (abs(last_elem) <= abs(asteroid)):
					st.pop()
					if abs(last_elem) == abs(asteroid):
						break
					if st:
						last_elem = st[-1]
				if abs(last_elem) < abs(asteroid):
					neg_elem.append(asteroid)
		else:
			st.append(asteroid)
	if len(neg_elem)>0:
		return (neg_elem+st)
	else:
		return st


asteroids1 = [5,10,-5]
asteroids2 = [8,-8]
asteroids3 = [10,2,-5]
asteroids4 = [-1,-1,1,2]
asteroids5 = [-2,2,1,-2]
asteroids6 = [1,2,1,-2]


print(asteroid_collision_amit(asteroids1))
print(asteroid_collision_amit(asteroids2))
print(asteroid_collision_amit(asteroids3))
print(asteroid_collision_amit(asteroids4))
print(asteroid_collision_amit(asteroids5))
print(asteroid_collision_amit(asteroids6))
