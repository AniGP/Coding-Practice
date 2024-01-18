public class Solution 
{
    public int majorityElement(int[] nums) 
    {
        // Boyer Moore Voting Algorithm

        // Initialization
        int element = nums[0];
        int count = 1;

        // Majority Candidate Identification
        for (int i = 1; i < nums.length; i++) 
        {
            if (count == 0) 
            {
                element = nums[i];
                count = 1;
            } 
            
            else if (element == nums[i]) 
            {
                count++;
            } 
            
            else 
            {
                count--;
            }
        }

        return element;
    }

    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        // Test case 1
        int[] nums1 = {3, 2, 3};
        System.out.println("Majority element in [3, 2, 3]: " + solution.majorityElement(nums1));

        // Test case 2
        int[] nums2 = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("Majority element in [2, 2, 1, 1, 1, 2, 2]: " + solution.majorityElement(nums2));
    }
}

/*
 The time complexity of the Boyer-Moore Voting Algorithm is O(n), 
where n is the number of elements in the array `nums`. 


- The algorithm goes through the array only once, element by element. Each element is looked at exactly once.

- For each element, the algorithm performs a few simple operations: comparison, 
incrementing or decrementing the count, and possibly changing the element. These operations take a constant amount of time, regardless of the size of the array.
 */