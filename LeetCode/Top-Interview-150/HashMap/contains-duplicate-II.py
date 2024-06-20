class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nums = {}

        for i, num in enumerate(nums):

            if num in nums:
             
             # If the number is already in the dictionary, check the difference between indices
                j = nums[num] # Current value's previous index

                if i-j <= k:
                    return True

                nums[num] = i # Update the index of the current value

        return False

'''

Credits:

https://leetcode.com/problems/contains-duplicate-ii/solutions/2463150/very-easy-100-fully-explained-java-c-python-javascript-python3-using-hashset
https://leetcode.com/problems/contains-duplicate-ii/solutions/4069377/python-99-runtime-hash-table-easy-to-understand

Time Complexity:
- O(n): You go through the list once, and for each element, dictionary operations (check and insert) 
are average O(1).

Space Complexity:
- O(min(n, k)): The dictionary will hold at most k+1 elements if all are unique within a window 
size of k. If k is larger than n, then at most n elements are stored.

'''