class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
'''

Time Complexity:

- O(n)
- We count the node itself (1) plus the count of nodes in its left subtree and the count of nodes in its right subtree. 
It visits every node in the tree.

'''