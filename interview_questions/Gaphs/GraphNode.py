

class GraphNode:

	def __init__(self, item:str, visited=False ):
		self.item = item
		self.visited = visited
		self.children = []

