# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Handle empty lists

        if not list1:
            return list2
        if not list2:
            return list1
        
        # Header Node for the merged list
        header_merged = ListNode()
        current = header_merged

        # Now we'll iterate through the lists

        while list1 and list2:

            if list1.val <= list2.val:

                current.next = list1
                list1 = list1.next
            
            else:

                current.next = list2
                list2 = list2.next

            current = current.next # Move the current pointer

        # Add any more nodes to the list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return header_merged.next
    
'''
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
'''