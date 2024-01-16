/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution 
{
    public boolean hasCycle(ListNode head) 
    {
        if (head == null || head.next == null) 
        {
            return false;
        }

        ListNode ptr1 = head;
        ListNode ptr2 = head.next;

        while (ptr2 != null && ptr2.next != null) 
        {
            if (ptr1 == ptr2) 
            {
                return true;
            }
            
            ptr1 = ptr1.next;
            ptr2 = ptr2.next.next;
            
        }

        return false;

    }

    public static ListNode createLinkedList(int[] arr) 
    {
        if (arr.length == 0) 
        {
                return null;
        }
        
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        
        for (int i = 1; i < arr.length; i++) 
        {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
            return head;
    }

    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        // Test Case 1: No cycle
        ListNode list1 = createLinkedList(new int[]{1, 2, 3, 4});
        System.out.println("Test Case 1 - Has Cycle: " + solution.hasCycle(list1));

        // Test Case 2: No cycle (Single element)
        ListNode list2 = createLinkedList(new int[]{1});
        System.out.println("Test Case 2 - Has Cycle: " + solution.hasCycle(list2));

        // Test Case 3: No elements
        ListNode list3 = createLinkedList(new int[]{});
        System.out.println("Test Case 3 - Has Cycle: " + solution.hasCycle(list3));
    }
}