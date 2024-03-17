/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.Arrays;

class Solution {
    public ListNode merge(ListNode a, ListNode b) {

        if (a == null && b == null) {
            return a;
        }
        
        ListNode head = new ListNode();
        ListNode current = head;

        while (a != null || b != null) {
            if (a == null) {
                current.val = b.val;
                b = b.next;
            }
            else if (b == null) {
                current.val = a.val;
                a = a.next;
            }
            else if (a.val < b.val) {
                current.val = a.val;
                a = a.next;
            } else {
                current.val = b.val;
                b = b.next;
            }

            if (a != null || b != null) {
                current.next = new ListNode();
                current = current.next;
            }
        }
        return head;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length > 2) {
            int halfLength = lists.length / 2;
            ListNode a = mergeKLists(Arrays.copyOfRange(lists, 0, halfLength));
            ListNode b = mergeKLists(Arrays.copyOfRange(lists, halfLength, lists.length));
            return merge(a, b);
        }
        else if (lists.length == 2) {
            return merge(lists[0], lists[1]);
        }
        else if (lists.length == 1) {
            return lists[0];
        }
        else {
            return null;
        }
    }
}