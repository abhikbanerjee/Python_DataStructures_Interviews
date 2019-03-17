# Refe - https://leetcode.com/problems/asteroid-collision/


def asteroid_collision(asteroids):
	asteroid_lists = []
	flag = True
	while len(asteroid_lists)!=0 or flag:
		for asteroid in asteroids:
			if len(asteroid_lists) ==0:
				asteroid_lists.append(asteroid)
			else:
				last_asteroid = asteroid_lists[len(asteroid_lists)-1]
				if asteroid < 0 and last_asteroid > 0 :
					# they are travelling in opposite direction
					popped_asteroid = asteroid_lists.pop()
					if -1*popped_asteroid != asteroid:
						max_val = asteroid if abs(popped_asteroid) < abs(asteroid) else popped_asteroid
						last_asteroid = asteroid_lists[len(asteroid_lists) - 1]
						asteroid_lists.append(max_val)
				else:
					asteroid_lists.append(asteroid)
	return asteroid_lists

asteroids1 = [5,10,-5]
asteroids2 = [8,-8]
asteroids3 = [10,2,-5]
asteroids4 = [-1,-1,1,2]

print(asteroid_collision(asteroids1))
print(asteroid_collision(asteroids2))
print(asteroid_collision(asteroids3))
print(asteroid_collision(asteroids4))
