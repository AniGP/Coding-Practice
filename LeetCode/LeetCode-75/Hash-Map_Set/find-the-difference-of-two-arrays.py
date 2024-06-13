class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # Convert the lists to sets to remove duplicates
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        # Find elements present in nums1 but not in nums2
        nums1_unique = []
        nums1_unique = set(nums1) - set(nums2)

        # Find elements present in nums2 but not in nums1
        nums2_unique = []
        nums2_unique = set(nums2) - set(nums1)

        return [nums1_unique, nums2_unique]

sol = Solution()
print(sol.findDifference([1,2,3], [2,4,6]))  # Output: [[1,3],[4,6]]
print(sol.findDifference([1,2,3,3], [1,1,2,2]))  # Output: [[3],[]]
    
'''
    
Time Complexity:

- O(N + M): Where N is the length of nums1 and M is the length of nums2. 
Converting lists to sets and performing set operations (difference) both take linear time relative 
to the size of the inputs.

Space Complexity:

- O(N + M): Space is used to store the unique elements of nums1 and nums2 in sets. The maximum 
space needed depends on the distinct elements present in both lists.
    
    '''