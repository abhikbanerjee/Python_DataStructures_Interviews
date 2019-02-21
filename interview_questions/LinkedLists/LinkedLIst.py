from interview_questions.LinkedLists.listnode import ListNode


class LinkedList:
	def __init__(self):
		self.head = None

	def push_node(self, data):
		temp_node = ListNode(data)
		temp_node.next = self.head
		self.head = temp_node

	def reverse_list(self):
		prev = None
		curr = self.head
		while curr is not None:
			next_nd = curr.next
			curr.next = prev
			prev = curr
			curr = next_nd
		self.head = prev

	def print_list(self):
		print("Printing List values")
		p = self.head
		while p is not None:
			print(p.value)
			p = p.next


def main():
	l1 = LinkedList()
	l1.push_node(2)
	l1.push_node(4)
	l1.push_node(6)
	l1.push_node(7)
	# Print the list after pushing couple of nodes
	l1.print_list()
	# Now reverse the linked list and print the result again
	l1.reverse_list()
	l1.print_list()


if __name__ == "__main__":
	main()


