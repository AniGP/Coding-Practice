class TwoSum_Optimized {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> num_indices = new HashMap<>();

        for(int i=0; i<nums.length; i++)
        {
            int num = nums[i];
            int diff = target - num;

            // Checking for the difference in HashMap

            if(num_indices.containsKey(diff))
            {
                return new int[]{num_indices.get(diff), i};
                // returns the indices of the two numbers
                // that add up to the target
            }

            num_indices.put(num, i);
            // If the difference is not present in the HashMap,
            // add the current num and it's index to the HashMap
        }

        return null;
    }
}