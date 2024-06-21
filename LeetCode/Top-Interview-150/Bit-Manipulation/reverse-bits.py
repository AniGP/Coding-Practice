class Solution:
    def reverseBits(self, n: int) -> int:

        answer = 0

        for i in range(32):

            bit = (n >> i) & 1
            answer = answer | (bit << (31 - i))
        
        return answer
    
'''

Credits: 

https://leetcode.com/problems/reverse-bits/solutions/3218837/190-solution-step-by-step-explanation

Time Complexity: 
- O(1) since we always iterate over a fixed number of bits (32).

Space Complexity: 
- O(1) as we use a fixed amount of space regardless of the input size.

'''