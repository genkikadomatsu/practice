from typing import List, Optional 


# LeetCode 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Get number one
        n1, n2, multiplier = 0, 0, 1

        while l1:
            n1 += l1.val * multiplier
            l1 = l1.next
            multiplier = multplier * 10

        multiplier = 1

        while l2:
            n2 += l2.val * multiplier
            l2 = l2.next
            multiplier = multiplier * 10

        return (n1 + n2)