# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        temp = head
        while temp:
            after = temp.next  # 1
            temp.next = pre  # 2
            pre = temp  # 3
            temp = after  # 4
            # 1: initialise/move pointer 'after'
            # 2: reverse arrow
            # 3: move pointer 'pre'
            # 4: move pointer 'temp'
        return pre
