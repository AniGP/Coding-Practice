# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n

        while left <=right:

            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid
            
            elif result == -1:
                right = mid - 1

            else:
                left = mid + 1

        return -1
    
sol = Solution()
print(sol.guessNumber(10))

'''

Time Complexity: 
- O(log n) since each step of the binary search halves the size of the problem.

Space Complexity:
- O(1) as only a few variables are needed regardless of the input size.

'''