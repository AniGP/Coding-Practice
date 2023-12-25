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
class Solution 
{
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) 
    {
        // Handle empty lists
        if (list1 == null) 
        {
            return list2;
        }

        if (list2 == null) 
        {
            return list1;
        }
        
        // Create a head for the merged list
        ListNode header_merged = new ListNode(0); 
        ListNode current = header_merged;

        // Iterate through both lists 

        while (list1 != null && list2 != null) 
        {
            if (list1.val <= list2.val) 
            {
                current.next = list1;
                list1 = list1.next;
            } 
            
            else 
            {
                current.next = list2;
                list2 = list2.next;
            }
            
            current = current.next;  // Move the current pointer
        }

        // Add any remaining nodes from either list
        current.next = list1 != null ? list1 : list2;

        return header_merged.next;  
        
    }
}

/*
The time complexity of the solution is O(n + m), 
where n and m are the lengths of the two input linked lists.

Handling empty lists: This takes constant time, O(1).
Creating a head: This also takes constant time, O(1).

Iterating through both lists:
    - The `while` loop runs until one of the lists becomes empty.
    - In each iteration, it compares two node values and updates pointers.
    - These operations take constant time, O(1).
    - The loop runs at most "n + m" times, covering all nodes in both lists.

Appending remaining nodes: This takes constant time, O(1).
 */
