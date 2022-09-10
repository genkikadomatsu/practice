# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        node_a = None
        node_b = head
        
        while node_b:
            temp = node_b.next
            node_b.next = node_a
            node_a = node_b
            node_b = temp
        
        return node_a
