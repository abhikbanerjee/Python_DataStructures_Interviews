from interview_questions.LinkedLists.listnode import ListNode
from interview_questions.LinkedLists.LinkedLIst import LinkedList


def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        tmp = l3
        carry = 0
        while l1 and l2:
            sum = (l1.val + l2.val + carry)
            if sum >= 10:
                val = sum%10
                carry = 1
                tmp.next = ListNode(val)
            else:
                tmp.next = ListNode(sum)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            tmp = tmp.next
        while l1:
            sum = l1.val+carry
            if sum >= 10:
                val = sum%10
                carry = 1
                tmp.next = ListNode(val)
            else:
                tmp.next = ListNode(sum)
                carry = 0
            tmp = tmp.next
            l1 = l1.next
        while l2:
            sum = l2.val+carry
            if sum >= 10:
                val = sum%10
                carry = 1
                tmp.next = ListNode(val)
            else:
                tmp.next = ListNode(sum)
                carry = 0
            tmp = tmp.next
            l2 = l2.next
        if carry==1:
            tmp.next = ListNode(1)
        return l3.next


def main():
    l1 = LinkedList()
    l1.push_node(2)
    l1.push_node(4)
    l1.push_node(6)
    l1.push_node(7)

    l2 = LinkedList()
    l1.push_node(3)
    l1.push_node(7)
    l1.push_node(9)
    l1.push_node(1)

    add_two_numbers(l1, l2)

if __name__ == "__main__":
    main()