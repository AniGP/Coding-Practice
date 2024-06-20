class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        xor_result = 0

        for num in nums:
            xor_result = xor_result ^ num
        
        return xor_result

'''

Credits for explaining the logic: 
https://leetcode.com/problems/single-number/solutions/1771771/think-it-through-time-o-n-space-o-1-python-go-explained

Time Complexity:
- O(n) - The loop iterates through each element in the array exactly once.

Space Complexity:
- O(1) - No additional space is required regardless of the input size, as we're only using a single extra variable.

'''