# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        temp = head
        while temp:
            visited[temp] = True
            temp = temp.next
            if temp in visited:
                return temp
        return None  # not False

    def detectCycle_2(self, head: Optional[ListNode]) -> Optional[ListNode]:  # t.c.: O(n)  s.c.: O(1)
        # https://leetcode.com/problems/linked-list-cycle-ii/solutions/1701055/java-c-python-best-explanation-ever-happen-s-for-this-problem/
        " Slow and fast pointers "
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head  # !!!
                while slow != fast:
                    slow = slow.next
                    fast = fast.next  # now move one step at a time
                return slow
