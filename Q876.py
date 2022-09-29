# Middle of the Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 1. In Leetcode, a noed is represented by a list
    # 2. integer division //: 5//2=2, 4//2=2, -3//2=-2
    def middleNode_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        length = 1
        while temp.next:  # NOT while temp
            temp = temp.next
            length = length + 1
        mid = head
        i = 0
        while i < (length // 2):
            mid = mid.next
            i += 1
        return mid

    # Slow and fast pointers
    def middleNode_2(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head  # !!!
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # !!!
        return slow