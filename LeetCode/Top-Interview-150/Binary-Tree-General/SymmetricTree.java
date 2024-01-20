// Definition for a binary tree node.
class TreeNode 
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
    public boolean isSymmetric(TreeNode root) 
    {
        if (root == null) 
        {
            return true;
        }

        return isMirror(root.left, root.right);
    }

    private boolean isMirror(TreeNode left, TreeNode right) 
    {
        if (left == null && right == null) 
        {
            return true;
        }

        if (left == null || right == null) 
        {
            return false;
        }

        return (left.val == right.val) && isMirror(left.left, right.right) && isMirror(left.right, right.left);
    }
}

class Main 
{
    public static void main(String[] args)
     {
        Solution sol = new Solution();

        // Example 1: Symmetric tree
        TreeNode node1 = new TreeNode(1);
        node1.left = new TreeNode(2, new TreeNode(3), new TreeNode(4));
        node1.right = new TreeNode(2, new TreeNode(4), new TreeNode(3));
        System.out.println("Tree 1 is symmetric: " + sol.isSymmetric(node1));  // Expected: True

        // Example 2: Non-symmetric tree
        TreeNode node2 = new TreeNode(1);
        node2.left = new TreeNode(2, null, new TreeNode(3));
        node2.right = new TreeNode(2, null, new TreeNode(3));
        System.out.println("Tree 2 is symmetric: " + sol.isSymmetric(node2));  // Expected: False
    }
}

/*

Time Complexity: O(n)

- We're traversing each node exactly once. 
- At every step, we perform a constant amount of work: comparing values and making two recursive calls.

*/