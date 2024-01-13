class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1 # last element of nums1
        j = n - 1 # last element of nums2
        k = m + n - 1 # last element of merged array in nums1

        # Merge all elements of nums2 into nums1

        while j>=0:

            # if nums1[i] > nums2[j], nums1[i] is placed at kth position
            # keep moving ith pointer towards left (backward direction)

            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i -1
            # else place nums2[j] at kth position
            # keep moving jth pointer towards left (backward direction)

            else:
                nums1[k] = nums2[j]
                j = j - 1

            # Move the kth pointer towards left (backward director)
            k = k - 1

# Test Case 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print("Test Case 1 Result:", nums1) # Expected: [1,2,2,3,5,6]

# Test Case 2
nums1 = [1]
m = 1
nums2 = []
n = 0
solution.merge(nums1, m, nums2, n)
print("Test Case 2 Result:", nums1) # Expected: [1]

# Test Case 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
print("Test Case 3 Result:", nums1) # Expected: [1]

'''
The time complexity of this solution is O(m+n), where m is the length of nums1 and n is the length of nums2.

- It looks through each number in both arrays just once. It starts at the end and moves backwards until it has seen every number.

- No repeated loops within loops. This means it doesn't check the same thing many times, which keeps it quick.

- The time it takes depends on the total number of numbers in both arrays. 
  It doesn't matter how they are divided between the two arrays; what counts is the total.
'''