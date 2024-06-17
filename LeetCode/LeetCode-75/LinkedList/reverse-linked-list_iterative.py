# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize previous as null
        previous = None

        # Initialize the current as head
        current = head

        # Until the current reaches the end of the list

        while current:
            
            # Initialize the next ptr as the next ptr of current
            # Store next node
            next = current.next

            # Assign the previous ptr to current's next ptr
            # Reverse current node's ptr
            current.next = previous

            # Assign current to previous, next to current
            # Move pointers one position forward
            previous = current
            current = next

        return previous # Previous is the new head of the reversed list

    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

# Example usage:
lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
reversed_lst = sol.reverseList(lst)
print_list(reversed_lst)  # Expected output: 5 -> 4 -> 3 -> 2 -> 1 -> None


'''

Time Complexity:

- O(n): The iterative approach involves a single loop that traverses all the nodes of the linked list 
exactly once. Here, n is the number of nodes in the linked list. Each node is processed once as the 
loop moves the current pointer from the head to the end of the list.


Space Complexity:

- O(1): This approach uses a fixed amount of space regardless of the input size. 
The space is used for a few pointers (current, prev, next_node), which does not depend on the size 
of the linked list.

'''