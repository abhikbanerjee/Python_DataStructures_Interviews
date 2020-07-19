from collections import deque


# Implement a Least Recently Used Cache - LC 146
class LRUCache:
	def __init__(self, size=5):
		self.queue = deque()
		self.lru_set = set()
		self.cache_size = size

	def get_value(self, value):
		if value in self.lru_set:
			# The value tried to search in cache is present, update the queue by moving it at the most recent location
			# find and delete the earlier entry in the dequeue
			self.queue.remove(value)
			self.queue.append(value)
		else:
			# The element is not present, fetch the element and update the set and queue accordingly
			if len(self.queue) == self.cache_size:
				# pop the element least recent
				self.pop_value()
			self.lru_set.add(value)
			self.queue.append(value)

	def pop_value(self):
		val = self.queue.popleft()
		self.lru_set.remove(val)


def main():
	# create an LRU cache and try some push and pop operations
	lru_cache = LRUCache()
	lru_cache.get_value(4)
	lru_cache.get_value(6)
	lru_cache.get_value(2)
	print("LRU Cache Queue - ", lru_cache.queue)
	print("LRU Cache Set Size - ", len(lru_cache.lru_set))
	lru_cache.get_value(4)
	print("LRU Cache Queue - ", lru_cache.queue)
	print("LRU Cache Set Size - ", len(lru_cache.lru_set))
	lru_cache.get_value(7)
	print("LRU Cache Queue - ", lru_cache.queue)
	print("LRU Cache Set Size - ", len(lru_cache.lru_set))
	lru_cache.get_value(2)
	print("LRU Cache Queue - ", lru_cache.queue)
	print("LRU Cache Set Size - ", len(lru_cache.lru_set))
	lru_cache.get_value(11)
	print("LRU Cache Queue - ", lru_cache.queue)
	print("LRU Cache Set Size - ", len(lru_cache.lru_set))
	lru_cache.get_value(12) # the max size is reached so the least Recently used element needs to be removed
	print("LRU Cache Queue - ", lru_cache.queue)
	print("LRU Cache Set Size - ", len(lru_cache.lru_set))

if __name__=="__main__":
	main()