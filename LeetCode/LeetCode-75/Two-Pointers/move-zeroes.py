class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        insertPos = 0 # ptr for the position to insert the non-zero number

        # Move no non-zero values to the front
        for num in nums:
            if num != 0:
                nums[insertPos] = num
                insertPos += 1

        # The remaining array has to be filled with zeroes
        while insertPos < len(nums):
            nums[insertPos] = 0
            insertPos+=1

# Driver code to test the function
nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)
print(nums)  # Output should be [1, 3, 12, 0, 0]

'''

Time Complexity:

- O(n), where n is the length of the array. This is because we are iterating through the array at least once to relocate the non-zero elements and then to fill in the zeroes.

Space Complexity:

- O(1), since we are performing the operation in-place without using any additional space for another array.

The approach minimizes operations by ensuring that each element is either:

- Moved directly to its new position if it's non-zero.
- Ignored if it's zero, until the end when remaining positions are filled with zeroes.

'''