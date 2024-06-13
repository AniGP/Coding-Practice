class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        curr_alt = 0
        max_alt = 0

        # Iterating over gain array to update the altitudes
        for g in gain:
            curr_alt += g # Update the current altitude with gain
            max_alt = max(max_alt, curr_alt) # Update max altitude if current is higher

        return max_alt
    
# Driver code
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestAltitude([-5,1,5,0,-7]))  # Output: 1
    print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))  # Output: 0

'''
Credits (for helping me understand the problem statement, which is very vague): https://leetcode.com/problems/find-the-highest-altitude/solutions/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: 

- O(n), where n is the number of elements in the gain array. This is because we traverse the gain list once.

Space Complexity: 

- O(1), as we are using a constant amount of space regardless of the input size.
'''