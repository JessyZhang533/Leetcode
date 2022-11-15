# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode  # pre starts from dummy node

        for _ in range(m - 1):  # use m-1 because range is 0-indexed
            pre = pre.next
        # now pre points at left-1

        # reverse the [m, n] nodes
        reverse = None  # !!! to avoid cycle in the linked list
        cur = pre.next
        for _ in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        # now pre.next is where integer m represents
        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
