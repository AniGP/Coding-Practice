class Solution {
    public int removeDuplicates(int[] nums) {

        if(nums.length == 0)
        {
            return 0;
        }

        int k=0;

        for(int i=1; i<nums.length; i++)
        {
            if(nums[k]!=nums[i])
            {
                k+=1;
                nums[k] = nums[i];
            }
        }

        return k+1;
    }
}/*The provided solution has a time complexity of O(n).

I feel that I would not be further able to improve the time complexity of this problem, because of the following reasons:

i.) The input array is already sorted
ii.) Each element must be checked at least once for identifying duplicated and removing them in place
iii.) Any more further attempts of simplifying the problems using data structures would make it more complex without advantage.*/