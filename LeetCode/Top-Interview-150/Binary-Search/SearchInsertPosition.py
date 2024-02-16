class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2  # Find the middle index

            if nums[mid] == target:  # Target value found
                return mid

            elif nums[mid] < target:  # Target is in the right half
                left = mid + 1
                
            else:  # Target is in the left half
                right = mid - 1

        # If the target is not found, the 'left' index is where it should be inserted
        return left