# Merge two sorted lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists_1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # DONNOT NEED ANY BASE CASES. Please run base cases orally before running the code
        temp1 = list1
        temp2 = list2
        merged = ListNode(0)
        temp3 = merged
        while temp1 and temp2:  # Note: temp.next can be None, but temp cannot be None when using temp.next
            if temp2.val <= temp1.val:
                temp3.next = temp2
                temp3 = temp3.next
                temp2 = temp2.next
            else:
                temp3.next = temp1
                temp3 = temp3.next
                temp1 = temp1.next

        # Deal with the remaining stuff
        if temp1:
            temp3.next = temp1
        if temp2:
            temp3.next = temp2
        merged = merged.next
        return merged

    # Optimised
    def mergeTwoLists_2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1  # !!!
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:  # !!!
            cur.next = list1 if list1 else list2
            
        return dummy.next
