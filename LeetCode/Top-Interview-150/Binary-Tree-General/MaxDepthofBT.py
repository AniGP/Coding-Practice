class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0
        
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            
            return max(left_depth, right_depth) + 1

# Example 1: [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# Example 2: [1,null,2]
root2 = TreeNode(1)
root2.right = TreeNode(2)

# Solution instance
sol = Solution()

# Test Example 1
print("Max Depth of Example 1:", sol.maxDepth(root1))  # Output should be 3

# Test Example 2
print("Max Depth of Example 2:", sol.maxDepth(root2))  # Output should be 2

'''

Time Complexity: O(n), where n is the number of nodes in the tree.

- We use a recursive depth-first search (DFS) function that visits each node exactly once.
- At each node, the function makes two recursive calls - one for the left child and one for the right child.
- Since every node in the binary tree is visited once and the work done at each node is constant 
(excluding the recursive calls), the total work done is proportional to the number of nodes in the tree.

'''