/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution 
{
    public boolean hasPathSum(TreeNode root, int targetSum) 
    {
        if (root == null) 
        {
            return false;
        }

        // Check if it's a leaf node
        if (root.left == null && root.right == null) 
        {
            return root.val == targetSum;
        }

        // Recursive call for left and right subtree
        return hasPathSum(root.left, targetSum - root.val) || 
               hasPathSum(root.right, targetSum - root.val);
        
    }
}

/*
 The time complexity of this solution is O(n), where n is the number of nodes in the binary tree. 
    This is because in the worst case, we might have to visit each node once to check if a valid path sum exists.
 */
