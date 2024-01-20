class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isSame(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and isSame(left.left, right.right) and isSame(left.right, right.left)

        return isSame(root.left, root.right)

# Example 1: Symmetric tree
node1 = TreeNode(1)
node1.left = TreeNode(2, TreeNode(3), TreeNode(4))
node1.right = TreeNode(2, TreeNode(4), TreeNode(3))

# Example 2: Non-symmetric tree
node2 = TreeNode(1)
node2.left = TreeNode(2, None, TreeNode(3))
node2.right = TreeNode(2, None, TreeNode(3))

sol = Solution()
print("Tree 1 is symmetric:", sol.isSymmetric(node1))  # Expected: True
print("Tree 2 is symmetric:", sol.isSymmetric(node2))  # Expected: False

'''

Time Complexity: O(n)

- We're traversing each node exactly once. 
- At every step, we perform a constant amount of work: comparing values and making two recursive calls.

'''