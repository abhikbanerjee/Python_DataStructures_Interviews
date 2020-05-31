from typing import List
from interview_questions.LinkedLists.listnode import ListNode


def remove_elements(head: ListNode, val: int) -> ListNode:
    if head is None:
        return head
    while head and head.val == val:
        head = head.next
    if head is None:
        return head
    p = head
    while p.next is not None:
        if p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    return head
