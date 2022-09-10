class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(current_node):
            
            # base case (runs only on last call)
            if not current_node:
                return None
            
            # recursive case
            new_head = current_node
            if current_node.next: 
                new_head = reverse(current_node.next)
                current_node.next.next = current_node
                
            current_node.next = None
            return new_head
        
        
        return reverse(head)