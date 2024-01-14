class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize the counter for the number of elements not equal to val

        # Iterate through each element in the nums array
        for i in range(len(nums)):
            # Check if the current element is not equal to val
            if nums[i] != val:
                # If it's not val, swap this element with the element at index k
                nums[k], nums[i] = nums[i], nums[k]
                k += 1  # Increment k since we found an element not equal to val

        # k now represents the number of elements not equal to val
        return k

# Test cases
sol = Solution()

# Test case 1
print(sol.removeElement([3, 2, 2, 3], 3))  # Expected output: 2

# Test case 2
print(sol.removeElement([1, 2, 4, 5], 3))  # Expected output: 4

# Test case 3
print(sol.removeElement([2, 2, 2, 2], 2))  # Expected output: 0

# Test case 4
print(sol.removeElement([], 1))  # Expected output: 0

# Test case 5
print(sol.removeElement([1], 1))  # Expected output: 0

'''
The time complexity of this solution is O(n), where n is the number of elements in the array nums.


- The algorithm iterates through the array exactly once.
- During each iteration, it performs a constant amount of work: checking if an element is equal to val, and swapping elements as per the condition.
'''