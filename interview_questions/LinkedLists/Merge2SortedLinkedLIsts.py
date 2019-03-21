from interview_questions.LinkedLists.listnode import ListNode


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        tmp = result
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
                tmp = tmp.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
                tmp = tmp.next
        if l1:
            while l1:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
                tmp = tmp.next
        if l2:
            while l2:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
                tmp = tmp.next
        return result.next

