# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Base Case
        if not root or root.val == val:
            return root

        # Search left and tight subtrees
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        
'''

Time Complexity:

- Best case: O(1), when the root node is the value we are looking for.
- Avg./Worst case: O(log n) on a balanced BST. This is because half of the tree gets eliminated at each step.

Space Complexity:

- O(log n) for a balanced tree.
O(n) in the worst case scenario due to DFS (Recursion)

'''