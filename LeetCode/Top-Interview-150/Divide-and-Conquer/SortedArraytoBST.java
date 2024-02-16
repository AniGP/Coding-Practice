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
    public TreeNode sortedArrayToBST(int[] nums) 
    {
        if (nums == null || nums.length == 0) 
        {
            return null;
        }

        return constructBSTRecursive(nums, 0, nums.length - 1);
    }
    
    private TreeNode constructBSTRecursive(int[] nums, int start, int end) 
    {
        if (start > end) 
        {
            return null;
        }
        
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        
        root.left = constructBSTRecursive(nums, start, mid - 1);
        root.right = constructBSTRecursive(nums, mid + 1, end);
        
        return root;
    }
}

/*

Time Complexity:

- O(n)
- Each element is traversed once

 */