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
    public TreeNode invertTree(TreeNode root) 
    {
        // Base case: If the tree is empty, just return the node
        if (root == null)
        {
            return null;
        }

        // Swap the left and right children of the current node
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        // Recursively invert the left subtree
        invertTree(root.left);

        // Recursively invert the right subtree
        invertTree(root.right);

        // Return the root of the inverted tree
        return root;
    }
}

public class Main 
{
    public static void printInOrder(TreeNode root) 
    {
        if (root != null) {
            printInOrder(root.left);
            System.out.print(root.val + " ");
            printInOrder(root.right);
        }
    }

    public static void main(String[] args) 
    {
        // Create a binary tree
        // Example: 4,2,7,1,3,6,9
        TreeNode root = new TreeNode(4, 
            new TreeNode(2, new TreeNode(1), new TreeNode(3)), 
            new TreeNode(7, new TreeNode(6), new TreeNode(9))
        );

        // Print the original tree
        System.out.print("Original Tree: ");
        printInOrder(root);
        System.out.println();

        // Invert the tree
        Solution sol = new Solution();
        sol.invertTree(root);

        // Print the inverted tree
        System.out.print("Inverted Tree: ");
        printInOrder(root);
    }
}

/*

Time Complexity: O(n)

- Each node is visited exactly once. 
- The amount of work done is constant, that is, swapping.

*/