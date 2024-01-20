// Definition for a binary tree node.
public class TreeNode 
{
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }

      TreeNode(int val, TreeNode left, TreeNode right) 
      {
          this.val = val;
          this.left = left;
          this.right = right;
      }
}

class Solution 
{
    public int maxDepth(TreeNode root) 
    {
        if (root == null) 
        {
            return 0;
        } 
        
        else 
        {
            int leftDepth = maxDepth(root.left);
            int rightDepth = maxDepth(root.right);
            return Math.max(leftDepth, rightDepth) + 1;
        } 
    }

    public static void main(String[] args) 
    {
        // Example 1: [3, 9, 20, null, null, 15, 7]
        TreeNode root1 = new TreeNode(3);
        root1.left = new TreeNode(9);
        root1.right = new TreeNode(20);
        root1.right.left = new TreeNode(15);
        root1.right.right = new TreeNode(7);

        // Example 2: [1, null, 2]
        TreeNode root2 = new TreeNode(1);
        root2.right = new TreeNode(2);

        // Solution instance
        Solution sol = new Solution();

        // Test Example 1
        System.out.println("Max Depth of Example 1: " + sol.maxDepth(root1));  // Output should be 3

        // Test Example 2
        System.out.println("Max Depth of Example 2: " + sol.maxDepth(root2));  // Output should be 2
    }

}

