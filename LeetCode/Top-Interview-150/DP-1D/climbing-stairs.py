class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp = [0] * (n+1)
            dp[1] = 1
            dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

'''

Credits:

https://leetcode.com/problems/climbing-stairs/solutions/3708750/4-method-s-beat-s-100-c-java-python-beginner-friendly/

Time Complexity: 
- O(n) because you calculate the number of ways for each step up to n once.

Space Complexity: 
- O(n) for storing the number of ways for each step up to n in the dp array.

'''