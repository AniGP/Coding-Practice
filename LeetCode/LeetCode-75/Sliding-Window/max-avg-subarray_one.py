class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Calculate the sum of first 'k'elements and initialize
        # currentSum and maxSum

        currentSum = sum(nums[:k])
        maxSum = currentSum

        # Start the loop from the kth element
        # Iterate until you reach the end

        for i in range(k, len(nums)):

            # Update the sum by sliding the window: remover the element going out of
            # the window and add the element coming into the window

            currentSum += nums[i] - nums[i-k]

            # If the new window sum is greater, update the maxSum

            if currentSum > maxSum:
                maxSum = currentSum
            
        return maxSum/k # Since we need the average

sol = Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # Output: 12.75
print(sol.findMaxAverage([5], 1))                     # Output: 5.0
        
    
''' 

Credits: https://leetcode.com/problems/maximum-average-subarray-i/solutions/3532127/py3-beginner-friendly-with-details-and-explanation/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: 

- The algorithm runs in O(n) time since each element is added and subtracted exactly once when moving the window across the array.

Space Complexity: 

- The space complexity is O(1) as only a few extra variables are needed regardless of the input size.

'''