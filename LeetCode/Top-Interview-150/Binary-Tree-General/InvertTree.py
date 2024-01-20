# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the tree is empty or the node is a leaf, just return the node
        if root is None:
            return None

        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree
        self.invertTree(root.left)

        # Recursively invert the right subtree
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root

def printInOrder(root):
    """ Helper function to print the tree in in-order traversal """
    if root:
        printInOrder(root.left)
        print(root.val, end=' ')
        printInOrder(root.right)

# Create a binary tree
# Example: 4,2,7,1,3,6,9
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Print the original tree
print("Original Tree: ", end='')
printInOrder(root)
print()

# Invert the tree
sol = Solution()
sol.invertTree(root)

# Print the inverted tree
print("Inverted Tree: ", end='')
printInOrder(root)

"""

Time Complexity: O(n)

- Each node is visited exactly once. 
- The amount of work done is constant, that is, swapping.

"""