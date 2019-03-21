# Refe - https://leetcode.com/problems/asteroid-collision/


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

asteroids1 = [5,10,-5]
asteroids2 = [8,-8]
asteroids3 = [10,2,-5]
asteroids4 = [-1,-1,1,2]

# print(asteroid_collision(asteroids1))
# print(asteroid_collision(asteroids2))
print(asteroid_collision(asteroids3))
print(asteroid_collision(asteroids4))
