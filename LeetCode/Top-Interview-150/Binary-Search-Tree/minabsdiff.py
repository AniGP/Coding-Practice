class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inOrder(node):

            if not node:
                return
            
            # Left subtree
            inOrder(node.left)

            # Current node
            if self.prev is not None:

                self.min_diff = min(self.min_diff, node.val - self.prev)

            self.prev = node.val  # Update the current value to previous

            # Right subtree
            inOrder(node.right)

        inOrder(root)
        return int(self.min_diff)  

# Create the BST nodes
node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2, node1, node3)
node6 = TreeNode(6)
root = TreeNode(4, node2, node6)

# Instantiate Solution and find minimum difference
solution = Solution()
min_diff = solution.getMinimumDifference(root)

print(f"The minimum absolute difference in the BST is: {min_diff}")

'''

Time Complexity:

- O(n)
- Each node is visited once during the InOrder Traversal.
- Constant amount of work is done when each node is visited (comparison, updating the min. diff and 
the current value to previous)

'''