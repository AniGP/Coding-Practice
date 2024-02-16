public class Solution 
{
    public int searchInsert(int[] nums, int target)
    {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) 
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) 
            { 
                // Target value found
                return mid;
            } 
            
            else if (nums[mid] < target) 
            { 
                // Target is in the right half
                left = mid + 1;
            } 
            
            else 
            { 
                // Target is in the left half
                right = mid - 1;
            }
        }

        // If the target is not found, the 'left' index is where it should be inserted
        return left;
    }
}