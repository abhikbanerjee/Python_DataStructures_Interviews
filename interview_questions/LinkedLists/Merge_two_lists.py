from interview_questions.LinkedLists.listnode import ListNode


def merge_two_lists(l1:ListNode, l2:ListNode):
	dummy_head = tail = ListNode()
	while l1 and l2:
		if l1.value < l2.value:
			tail = l1
			l1 = l1.next
		else:
			tail = l2
			l2 = l2.next


def main():
	l1 = create_list()
	l2 = create_list()
	l3 = merge_two_lists(l1, l2)

	print_list(l3)


if __name__ == '__main__':
	main()
