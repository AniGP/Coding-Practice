class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Boyer Moore Voting Algorithm

        element = None
        count = 0

        for n in nums:
            if count == 0:
                element = n

            # Increment or decrement count based on the current element
            if n == element:
                count += 1
            else:
                count -= 1
        
        return element
    
# Test cases
solution = Solution()

# Test case 1
nums1 = [3, 2, 3]
print("Majority element in [3, 2, 3]:", solution.majorityElement(nums1))

# Test case 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print("Majority element in [2, 2, 1, 1, 1, 2, 2]:", solution.majorityElement(nums2))
    
'''

The time complexity of the Boyer-Moore Voting Algorithm is O(n), 
where n is the number of elements in the array `nums`. 


- The algorithm goes through the array only once, element by element. Each element is looked at exactly once.

- For each element, the algorithm performs a few simple operations: comparison, 
incrementing or decrementing the count, and possibly changing the element. These operations take a constant amount of time, regardless of the size of the array.

'''        