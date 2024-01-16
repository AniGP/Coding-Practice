# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False
        
        ptr1 = head
        ptr2 = head.next

        while ptr2 and ptr2.next:
            
            if ptr1 == ptr2:

                return True
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

        return False
    
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test the hasCycle method
solution = Solution()

# Test Case 1: No cycle
list1 = createLinkedList([1, 2, 3, 4])
print("Test Case 1 - Has Cycle:", solution.hasCycle(list1))

# Test Case 2: No cycle (Single element)
list2 = createLinkedList([1])
print("Test Case 2 - Has Cycle:", solution.hasCycle(list2))

# Test Case 3: No elements
list3 = createLinkedList([])
print("Test Case 3 - Has Cycle:", solution.hasCycle(list3))