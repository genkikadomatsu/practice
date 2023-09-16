# LeetCode 23

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        node = self
        result = ""

        while node.next:
            result += str(node.val) + "->"
            node = node.next

        return result 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Returns flattenned, sorted list."""

        length = len(lists)

        # Base cases
        match length:

            case 0:
                return None
            
            case 1:
                return lists[0]
            
            case 2:
                return Solution.merge(lists[0], lists[1])

            case _:
                a, b = lists[:length//2], lists[length//2:]
                a, b = self.mergeKLists(a), self.mergeKLists(b)
                return Solution.merge(a, b)


    @staticmethod
    def merge(a: ListNode, b: ListNode) -> ListNode:
        """Merges two linked lists and returns the head of the result."""
         
        # Empty list cases
        if not a or not b:
            return b if b else a
        
        # Set the new head        
        if a.val <= b.val:
            head = a
            a = a.next
        else:
            head = b
            b = b.next

        curr = head

        # Merge the rest of the elements 
        while a or b:
            
            if not a:
                curr.next = b
                return head
            
            if not b:
                curr.next = a
                return head
        
            if a.val < b.val:
                curr.next = a
                curr = a 
                a = a.next
                 
            else:
                curr.next = b
                curr = b
                b = b.next
        
        return head

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
l2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10, ListNode(12, None))))))
l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
l4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
print(Solution().mergeKLists([l1, l2, l3, l4]))