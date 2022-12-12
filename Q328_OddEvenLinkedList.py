# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        o = head
        e = head.next
        while e and e.next:
            temp = e.next
            e.next = e.next.next
            temp.next = o.next
            o.next = temp
            e = e.next
            o = o.next
        return head

    def oddEvenList_2(self, head):
        " Form the linked list of odd nodes and even nodes separately; join these two after the while loop "
        if not head:
            return head
        
        odd = head # Both of them point at the first node of the target linked list
        even = head.next # always one node behind odd; doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even # We have to keep where the even-node list starts
        
        while even and even.next: # won't get in the loop at first if there's only one node in the linked list
            # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
            # AND, why these two, small discussion by myself as below
            odd.next = odd.next.next
            even.next = even.next.next
            # After these two ops, odd/even still points at its original place
            # Therefore, we move them to the next node repectively
            odd = odd.next
            even = even.next
        odd.next = eHead # the odd pointer currently points at the last node of the odd-node list
        return head # We keep the start of the odd-node list in the first of our code
