# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num_1 = l1
        num_2 = l2
        carry = 0
        # Result LL with sentinel node
        res = ListNode(None)
        current = res
        
        # Add columns using carry addition
        while num_1 and num_2:
            
            col_sum = (num_1.val + num_2.val + carry) % 10
            carry = (num_1.val + num_2.val + carry) // 10
            current.next = ListNode(col_sum)
            current = current.next
            
            num_1 = num_1.next
            num_2 = num_2.next
        
        # Exhaust the remaining summand
        while num_1:
            
            col_sum = (num_1.val + carry) % 10
            carry = (num_1.val + carry) // 10
            current.next = ListNode(col_sum)
            current = current.next
            
            num_1 = num_1.next
        
        while num_2:
            
            col_sum = (num_2.val + carry) % 10
            carry = (num_2.val + carry) // 10
            current.next = ListNode(col_sum)
            current = current.next
            
            num_2 = num_2.next
        
        # If there is still a carry value, add it to the end of the result LL
        if carry:
            current.next = ListNode(carry)
            
        # Slice off the head sentinel node
        return res.next