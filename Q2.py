# Add two numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def convert(node):
            num = 0
            while node.next:
                temp = node
                pre = node
                j = 0
                while temp.next:
                    pre = temp
                    temp = temp.next
                    j += 1
                num += temp.val * 10**j
                pre.next = None
            num += node.val
            return num

        num_1 = convert(l1)
        num_2 = convert(l2)
        print(num_1, num_2)
        sum_of_nums = num_1 + num_2
        sum_digits = [int(x) for x in str(sum_of_nums)]

        head = ListNode(sum_digits[-1])
        temp = head
        if len(sum_digits) == 1:
            return head
        for i in range(len(sum_digits) - 2, -1, -1):
            temp.next = ListNode(sum_digits[i])
            temp = temp.next
        return head
            
            