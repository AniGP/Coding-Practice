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
    public boolean isSameTree(TreeNode p, TreeNode q) 
    {
        if (p == null && q == null) 
        {
            return true;
        }

        if (p == null || q == null || p.val != q.val) 
        {
            return false;
        }
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    // Test the Solution
    public static void main(String[] args) 
    {
        Solution sol = new Solution();

        // Test case 1
        TreeNode p = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode q = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        System.out.println(sol.isSameTree(p, q));  // Output: True

        // Test case 2
        p = new TreeNode(1, new TreeNode(2), null);
        q = new TreeNode(1, null, new TreeNode(2));
        System.out.println(sol.isSameTree(p, q));  // Output: False

        // Test case 3
        p = new TreeNode(1, new TreeNode(2), new TreeNode(1));
        q = new TreeNode(1, new TreeNode(1), new TreeNode(2));
        System.out.println(sol.isSameTree(p, q));  // Output: False
    }
}
