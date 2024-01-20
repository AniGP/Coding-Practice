class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Test the Solution
sol = Solution()

# Test case 1
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(sol.isSameTree(p, q))  # Output: True

# Test case 2
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, right=TreeNode(2))
print(sol.isSameTree(p, q))  # Output: False

# Test case 3
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print(sol.isSameTree(p, q))  # Output: False

'''

Time Complexity: O(n), where n is the smallest number of nodes in either of the two trees being compared.

 - The function works by comparing nodes from both trees together. 
 It starts at the root of each tree and then moves down through both trees simultaneously. At each step, it compares the current pair of nodes. This means each node in each tree is visited only once.

- Since each node is visited and compared exactly once, the total number of comparisons made is equal to the 
total number of nodes in the smaller tree. This is because if one tree is smaller, the comparison stops as 
soon as the smaller tree is fully traversed, even if the larger tree has more nodes.

'''