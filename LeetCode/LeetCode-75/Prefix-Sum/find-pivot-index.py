class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Check if the left sum equals the right sum
            #right_sum = total_sum - left_sum - num

            if left_sum == total_sum - left_sum - num:
                return i # return the current index if it is the pivot index
            left_sum += num

        return -1 # Return -1 if no pivot index is found

'''

Time Complexity: 

- The time complexity of this solution is O(n), where n is the number of elements in the array. 
This is because we make a single pass to calculate the total sum and another pass to find the pivot 
index.

Space Complexity:

- The space complexity is O(1). We only use a few variables (total_sum and left_sum) and do not use 
any additional data structures that scale with the input size.


'''