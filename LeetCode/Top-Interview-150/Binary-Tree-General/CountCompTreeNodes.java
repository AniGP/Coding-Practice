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

// Recurisve DFS

class Solution 
{
    public int countNodes(TreeNode root) 
    {
        if (root == null)
        {
            return 0;
        }

        return 1 + countNodes(root.left) + countNodes(root.right);        
    }
}

/*

Time Complexity:

- O(n)
- We count the node itself (1) plus the count of nodes in its left subtree and the count of nodes in its right subtree. 
It visits every node in the tree.

*/