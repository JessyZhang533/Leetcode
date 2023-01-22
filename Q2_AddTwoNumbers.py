# Add two numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers_1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

    # The concept of carry: add digits from the lowest level (10**0)
    def addTwoNumbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)  # if statement
            val2  = (l2.val if l2 else 0)  # if statement
            carry, out = divmod(val1 + val2 + carry, 10)  # divmod(divident, divisor): returns a tuple containing the quotient and the remainder.
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next