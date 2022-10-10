# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # fast & slow pointers; even & odd length dealt with separately
    def isPalindrome_1(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        values = []
        even = True
        while f:
            values.append(s.val)
            s = s.next
            # This if statement deals with a linked list of odd length an even length
            if f.next:
                f = f.next.next
            else:
                even = False
                f = None
        
        if even:
            i = len(values) - 1
            while s:
                if s.val == values[i]:
                    i -= 1
                    s = s.next
                else:
                    return False
            return True
        else:
            i = len(values) - 2
            while s:
                if s.val == values[i]:
                    i -= 1
                    s = s.next
                else:
                    return False
            return True

    # fast & slow pointers; reversed first half = second half
    def isPalindrome_2(self, head):
        rev = None  # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        slow = fast = head  # initially slow and fast are the same, starting from head
        while fast and fast.next:  # !!! deal with even and odd at the same time: fast for even, fast.next for odd
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # upper line equivalent to:
            # temp = rev
            # rev = slow
            # rev.next = temp
            # slow = slow.next
        if fast:
            slow = slow.next  # fast is at the end, move slow one step further for comparison(cross middle one)
        while rev and rev.val == slow.val:  # compare the reversed first half with the second half
            slow = slow.next
            rev = rev.next
        return not rev  # if equivalent then rev become None, return True; otherwise return False