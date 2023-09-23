class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0

        for i in range(1, len(nums)):  # Use range to create a range of indices
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]

        return k + 1
'''The provided solution has a time complexity of O(n).

I feel that I would not be further able to improve the time complexity of this problem, because of the following reasons:

i.) The input array is already sorted
ii.) Each element must be checked at least once for identifying duplicated and removing them in place
iii.) Any more further attempts of simplifying the problems using data structures would make it more complex without advantage.'''
