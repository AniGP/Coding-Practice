class Solution:
    def tribonacci(self, n: int) -> int:

        A = [0] * (n+1) # we create an array of size n+1 and initialize it with 0's

        if n == 0 or n == 1:
            return n
        
        if n == 2:
            return 1
        
        A[0] = 0
        A[1] = 1
        A[2] = 1

        for i in range(3, n+1):
            A[i] = A[i-1] + A[i-2] + A[i-3]
        return A[n]


'''

Credits: https://leetcode.com/problems/n-th-tribonacci-number/solutions/3115558/beats-100-basics-of-dp-explained-java-c-python/
(for explaining the logic)

Time Complexity: 
- O(n) because the function computes each Tribonacci number up to n exactly once.

Space Complexity: 
- O(n) due to the array A which stores the Tribonacci sequence up to the nth term.

'''