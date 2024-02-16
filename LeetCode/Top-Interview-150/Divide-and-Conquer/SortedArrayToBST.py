# Definition for a binary tree node.
# class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None

        # The middle element will be the root in the sorted array
        mid = len(nums) // 2

        # Create a new tree node with the root
        root = TreeNode(nums[mid])

        # Left subtree
        root.left = self.sortedArrayToBST(nums[:mid])

        # Right subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
    
'''

Time Complexity:

- O(n)
- Each element is traversed once

'''