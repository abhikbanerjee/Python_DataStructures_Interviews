from interview_questions.LinkedLists.listnode import ListNode


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
	runner = head
	prev = head
	count = 0

	check_count = head
	while check_count is not None:
		count += 1
		check_count = check_count.next

	if n == count:
		# delete the first node
		return head.next

	for i in range(1, n + 1):
		runner = runner.next

	# there is only 1 element in the list
	if runner is None:
		return None

	# now move both the pointers together to find the K+1 node from the end
	while runner.next is not None:
		runner = runner.next
		prev = prev.next

	# we found the node whose next node need to be deleted
	prev.next = prev.next.next
	return head

