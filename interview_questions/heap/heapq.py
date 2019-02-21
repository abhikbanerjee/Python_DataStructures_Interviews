import queue as Q
import heapq

def priority_queue():

	pq = Q.PriorityQueue()

	pq.put(2)
	pq.put(5)
	pq.put(1)
	pq.put(3)
	print('****************************')
	print("queue size 1 - ", pq.qsize())
	print("Priority Queue Elements - 1 ")
	while not pq.empty():
		print(pq.get())

	print("queue size 1 - ", pq.qsize())

	# work with a tuple inside a priority queue
	pq.put((2, 'two'))
	pq.put((8, 'eight'))
	pq.put((5, 'five'))
	pq.put((3, 'three'))
	pq.put((1, 'one'))
	pq.put((2, 'two'))

	print('****************************')
	print("queue size 2 - ", pq.qsize())
	print("Priority Queue Elements - 2")
	while not pq.empty():
		print(pq.get())

	print("queue size 2 - ", pq.qsize())

	print('****************************')
	h = []
	heapq.heappush(h, 4)
	heapq.heappush(h, 1)
	heapq.heappush(h, 8)
	heapq.heappush(h, 11)
	heapq.heappush(h, 5)

	print("heap size 3 - ", len(h))
	print("Heap Queue Elements - 1")
	for x in range(len(h)):
		print(heapq.heappop(h))
	print('****************************')


def main():
	priority_queue()

if __name__ == '__main__':
	main()