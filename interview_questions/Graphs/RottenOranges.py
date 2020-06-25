from typing import List


# Oranges can rot surrounding oranges every minute like a BFS, find the total time when all oranges get affected or can't be reached
# then return -1 -> LC:994
def oranges_rotting(grid: List[List[int]]) -> int:
	# check if grid is empty or None
	if grid is None or len(grid ) <1:
		return 0
	# initialize Fresh and Rotten Oranges
	fresh = set()
	rotten = set()
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				fresh.add((i ,j))
			if grid[i][j] == 2:
				rotten.add((i ,j))
	# Start infecting surrounding oranges and incrementing time
	directions = [(0 ,1), (1 ,0), (0 ,-1), (-1 ,0)]
	minutes = 0
	while len(fresh) > 0:
		# initialize a new list for current ingfection step
		current_rotten = set()
		for ro in rotten:
			curr_rot_i = ro[0]
			curr_rot_j = ro[1]
			for direction in directions:
				new_rot_i = curr_rot_i + direction[0]
				new_rot_j = curr_rot_j + direction[1]
				if (new_rot_i, new_rot_j) in fresh:
					fresh.remove((new_rot_i, new_rot_j))
					current_rotten.add((new_rot_i, new_rot_j))
		if len(current_rotten) == 0:
			# We may have 1 or more oranges which cant be infected
			return -1
		else:
			rotten = current_rotten
			minutes += 1
	return minutes


grid_oranges = [[2,1,1],[1,1,0],[0,1,1]]
print(oranges_rotting(grid_oranges))