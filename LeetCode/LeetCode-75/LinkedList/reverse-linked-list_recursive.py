# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        ptr = self.reverseList(head.next)
        head.next.next = head # To point the next node's next to the current node
        head.next = None

        return ptr
    
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

- O(n): Like the iterative method, the recursive method processes each node exactly once. 
Each function call handles one node of the list, and since there are n nodes, the recursion will 
occur n times.

Space Complexity:

- O(n): The primary space consumption in the recursive approach comes from the call stack used to 
handle the recursion. Since the recursion can go as deep as the number of nodes in the list 
(in the worst case where the list is not empty or has only one node), the maximum depth of the call 
stack will be n. Thus, the space complexity is O(n).

'''