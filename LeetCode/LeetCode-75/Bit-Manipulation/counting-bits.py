class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # Creating an array and initilize with zeroes store the result
        bits = [0] * (n+1)

        for i in range(1, n+1):

            # Calculate the number of 1s in the binary representation
            # by reusing the result of i/2 and adding 1 if the last bit is one

            bits[i] = bits[i >> 1] + (i & 1)

        return bits
    
# Example usage
sol = Solution()
print(sol.countBits(2))  # Output: [0, 1, 1]
print(sol.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]

'''

Credits (for explaining the logic):
https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation

Time Complexity: 
- O(n): Each number from 0 to n is processed exactly once with constant time operations.

Space Complexity:
- O(n): Additional space is used to store the result array of size n+1.


'''