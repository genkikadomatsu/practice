
print("MERGE TWO LINKED LISTS")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:ListNode, list2: ListNode) -> ListNode:
        
        
        if (list1 is None): return list2
        if (list2 is None): return list1

        head = ListNode()
        tail = head
        a, b = list1, list2
        
        while (a is not None) and (b is not None):
            
            if a.val < b.val:
                tail.next = a
                a = a.next
                if a is None: tail.next.next = b
            else:
                tail.next = b
                b = b.next
                if b is None: tail.next.next = a
            
            tail = tail.next
        
        return head.next


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(4)

y = ListNode(1)
y.next = ListNode(3)
y.next.next = ListNode(4)

z = ListNode(5)

sol = Solution()
temp = sol.mergeTwoLists(z, y)

while temp:
    print(temp.val)
    temp = temp.next