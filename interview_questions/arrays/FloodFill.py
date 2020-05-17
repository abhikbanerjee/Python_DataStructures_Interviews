
from typing import List

visited = []

def get_neighbor(r, c):
	# return [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c], [r + 1, c + 1], [r - 1, c - 1]]
	return [[r,c+1], [r,c-1], [r+1,c], [r-1,c]]

def flood_fill_helper(image, len_r, len_c, r, c, act_color, newColor):
	if r < 0 or r >= len_r:
		return
	if c < 0 or c >= len_c:
		return
	if image[r][c] != act_color:
		return
	image[r][c] = newColor
	visited.append([r, c])

	neighbors = get_neighbor(r, c)

	for v in neighbors:
		if v not in visited:
			flood_fill_helper(image, len_r, len_c, v[0], v[1], act_color, newColor)


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
	len_r = len(image)
	len_c = len(image[0])
	act_color = image[sr][sc]
	flood_fill_helper(image, len_r, len_c, sr, sc, act_color, newColor)
	return image

#Example 1
# image = [[1,1,1],
# 		 [1,1,0],
# 		 [1,0,1]]
# sr,sc, newColor = 1,1,2

#Example 2
image = [[0,0,0],
		[0,0,0]]

sr,sc, newColor = 0,0,2


print(floodFill(image, sr, sc, newColor))