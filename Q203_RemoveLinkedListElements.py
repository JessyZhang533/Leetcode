# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements_1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        pre = head
        while temp:
            if temp.val == val:
                if temp == head:  # this should be handled specifically
                    head = head.next
                    temp.next = None
                    # next two lines very important
                    pre, temp = head, head
                    continue
                else:
                    after = temp.next
                    temp.next = None
                    pre.next = after
                    temp = after
            else:  # !!!
                pre = temp
                if temp:
                    temp = temp.next
        return head

    def removeElements_2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Use dummy head to solve the 'head' edge case
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next  # concise!
            else:
                current_node = current_node.next
                
        return dummy_head.next
