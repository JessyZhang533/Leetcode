# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # this question is essentially reversing an arrow in every two arrows;
        # prev and cur wiil point at that arrow we will not reverse,
        # and we will revese the next arrow in the while loop
        dummy = ListNode(None, head)  # !!! dummy node
        prev, cur = dummy, head
        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = cur  # reverse
            prev, cur = cur, cur.next  # move pointer
        return dummy.next
