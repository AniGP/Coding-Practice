class TreeNode 
{
    int val;
    TreeNode left;
    TreeNode right;
    
    // Constructor for tree node
    TreeNode(int val) 
    { 
        this.val = val; 
    }
    
    // Constructor with left and right child nodes
    TreeNode(int val, TreeNode left, TreeNode right) 
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution 
{
    private TreeNode prev = null;
    private int minDiff = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) 
    {
        inOrder(root);
        return minDiff;
    }

    private void inOrder(TreeNode node) 
    {
        if (node == null) return; // Base case for recursion
        
        // Traverse left subtree
        inOrder(node.left);

        // Process current node
        if (prev != null) 
        {
            minDiff = Math.min(minDiff, node.val - prev.val);
        }

        prev = node; // Update prev to current node for the next iteration

        // Traverse right subtree
        inOrder(node.right);
    }
}

// Driver code to test the Solution class
public class Main 
{
    public static void main(String[] args) 
    {
        TreeNode node1 = new TreeNode(1);
        TreeNode node3 = new TreeNode(3);
        TreeNode node2 = new TreeNode(2, node1, node3);
        TreeNode node6 = new TreeNode(6);
        TreeNode root = new TreeNode(4, node2, node6);

        Solution solution = new Solution();
        int minDiff = solution.getMinimumDifference(root);

        System.out.println("The minimum absolute difference in the BST is: " + minDiff);
    }
}

/*

Time Complexity:

- O(n)
- Each node is visited once during the InOrder Traversal.
- Constant amount of work is done when each node is visited (comparison, updating the min. diff and 
the current value to previous)

 */