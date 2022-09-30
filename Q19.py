# Remove nth node from end of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd_1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1
        i = length - n
        pointer = head
        if i == 0:  # Edge case
            head = head.next
            pointer.next = None
            return head
        while i > 1:
            pointer = pointer.next
            i -= 1
        nth = pointer.next
        pointer.next = nth.next
        nth.next = None
        return head

    # fast & slow pointers
    # Fast moves first, and moves n steps. After that, slow starts to move, and when fast points to the last item, slow points to the (n-1)th node from the end of list
    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next  # no need to point the nth item to None
        return head
