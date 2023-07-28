from typing import List, Optional


# LeetCode 19

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not n:
            return head
 
        current_node = head
        
        while True:
            nth_node_away = current_node
            
            for i in range(n):
                nth_node_away = nth_node_away.next
           
            if not nth_node_away:
                if head is current_node:
                    return head.next
                print(previous.val)
                previous.next = current_node.next
                print(previous.val, "->", previous.next.val)
                return head 
            
            previous = current_node
            current_node = current_node.next


s = Solution()
print(s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 4))