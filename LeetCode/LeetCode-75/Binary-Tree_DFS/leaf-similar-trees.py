# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Helper function to traverse the tree and collect leaf node values
        def checkLeaf(root, ans):
            # Base case: If the node is null, return
            if not root:
                return

            # Recursively check the left subtree
            checkLeaf(root.left, ans)

            # If the node is a leaf (both left and right children are null), add its value to the list
            if not root.left and not root.right:
                ans.append(root.val)

            # Recursively check the right subtree
            checkLeaf(root.right, ans)

        # Lists to store leaf values for each tree
        ans1, ans2 = [], []

        # Populate lists with leaf values using the helper function
        checkLeaf(root1, ans1)
        checkLeaf(root2, ans2)

        # Check if the leaf sequences for both trees are equal
        return ans1 == ans2


'''

Credits: https://leetcode.com/problems/leaf-similar-trees/solutions/4534398/easy-beginner-friendly-solution-explained-with-comments

Time complexity: 

- O(N), The space complexity is also O(N), where N is the total number of nodes in the larger of the two trees.

Space complexity: 
- O(N), This space is primarily used for the vectors ans1 and ans2 to store the leaf values.
In the worst case, where all nodes in both trees are leaf nodes, the vectors will store N/2 leaf values for each tree.

'''