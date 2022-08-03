
print("MERGE TWO LINKED LISTS")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:ListNode, list2: ListNode) -> ListNode:
        
        # Trivial Case
        if not list1:
            return list2
        elif not list2:
            return list1
        
        p1, p2 = list1, list2
        new_head = ListNode()
        
        # Set new head
        if p1.val <= p2.val:
            new_head = p1
        else:
            new_head = p2

        # Returns the node whose pointer we should reassign
        # and the node who should be the new p1 or p2
        def f(node, val):
            temp = None
            while (node) and (node.val <= val):
                temp = node
                node = node.next
            return temp, node
                
        while p1 or p2:

            if p1.val <= p2.val:
                to_switch, new_p = f(p1, p2.val)
                to_switch.next = p2
                if new_p:
                    p1 = new_p
                else:
                    return new_head

            else:
                to_switch, new_p = f(p2, p1.val)
                to_switch.next = p1
                if new_p:
                    p2 = new_p
                else:
                    return new_head
            

        return new_head

x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(4)

y = ListNode(1)
y.next = ListNode(3)
y.next.next = ListNode(4)

z = ListNode(5)

sol = Solution()
temp = sol.mergeTwoLists(z, x)

while temp:
    print(temp.val)
    temp = temp.next