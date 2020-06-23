from interview_questions.Graphs.GraphNode import GraphNode
from collections import deque

queue = deque()


class Graph:
	def __init__(self):
		self.graph = []

	def create_graph(self):
		g1 = GraphNode("1")
		g2 = GraphNode("2")
		g3 = GraphNode("3")
		g4 = GraphNode("4")
		g5 = GraphNode("5")
		g6 = GraphNode("6")

		g1.children = [g2, g5, g6]
		g2.children = [g4, g5]
		g3.children = [g2]
		g4.children = [g3, g5]

		self.graph = [g1, g2, g3, g4, g5, g6]
		print("Created a simple graph")


def depth_first_search(graphnode: GraphNode):
	if not graphnode:
		return
	if not graphnode.visited:
		print(str(graphnode.item))
		graphnode.visited = True
		children = graphnode.children
		for child in children:
			depth_first_search(child)
	return


def breadth_first_search(graphnode: GraphNode):
	if not graphnode:
		return
	# add the graphnode to the queue
	queue.append(graphnode)
	while len(queue) != 0:
		grph_nd = queue.popleft()
		if not grph_nd.visited:
			print(str(grph_nd.item))
			grph_nd.visited = True
			children = grph_nd.children
			# add the children to the queue
			for child in children:
				queue.append(child)
	return


def main():
	#create a simple graph before calling the DFS and BFS
	g = Graph()
	g.create_graph()

	#Call the DFS
	# depth_first_search(g.graph[0])

	# Call the BFS
	breadth_first_search(g.graph[0])

if __name__ == "__main__":
	main()
