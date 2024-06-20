class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)  # Directly return the minimum of the two if there are only two steps.
        
        # Initialize the DP array that will store the minimum cost to reach each step
        min_cost = [0] * len(cost)
        min_cost[0], min_cost[1] = cost[0], cost[1]
        
        # Fill the DP table
        for i in range(2, len(cost)):
            min_cost[i] = cost[i] + min(min_cost[i-1], min_cost[i-2])
        
        # Return the minimum cost to reach the top of the floor
        return min(min_cost[-1], min_cost[-2])

sol = Solution()
cost1 = [10, 15, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(sol.minCostClimbingStairs(cost1))  # Output: 15
print(sol.minCostClimbingStairs(cost2))  # Output: 6

'''

Credits for helping me understand the logic:
https://leetcode.com/problems/min-cost-climbing-stairs/solutions/773865/a-beginner-s-guide-on-dp-validation-how-to-come-up-with-a-recursive-solution-python-3/

Time Complexity:
- O(n), where n is the length of the cost list, as we need to fill the DP table with n entries.

Space Complexity:
- O(n) for the dynamic programming table (min_cost).


'''