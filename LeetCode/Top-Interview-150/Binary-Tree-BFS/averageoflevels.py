# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def dfs(node, depth):
            
            if not node:
                return

            if depth == len(levels):
                levels.append([0, 0])

            levels[depth][0] += node.val
            levels[depth][1] += 1

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        levels = []
        dfs(root, 0)

        return [sum_count[0] / sum_count[1] for sum_count in levels]
    
'''

Time Complexity:

- O(n)
- All the nodes are visited once till the maximum depth.

'''