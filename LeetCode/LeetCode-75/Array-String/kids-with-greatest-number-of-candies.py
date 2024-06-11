class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_candies = max(candies) # maximum number of candies

        answer = []

        # Now, let's check if any kid has the greatest nuumber of candies

        for candy in candies:

            if candy + extraCandies >= max_candies:
                answer.append(True)
            
            else:
                answer.append(False)
        return answer
    
sol = Solution()

# Test cases
tests = [
    ([2, 3, 5, 1, 3], 3),
    ([4, 2, 1, 1, 2], 1),
    ([12, 1, 12], 10)
]

# Expected results
expected_results = [
    [True, True, True, False, True],
    [True, False, False, False, False],
    [True, False, True]
]

# Running the test cases
for i, test in enumerate(tests):
    candies, extraCandies = test
    result = sol.kidsWithCandies(candies, extraCandies)
    print(f"Test case {i + 1}:")
    print("Input:", candies, "Extra Candies:", extraCandies)
    print("Output:", result)
    print("Expected:", expected_results[i])
    print("Pass:", result == expected_results[i])
    print()
    
'''

Time Complexity:

- O(n), where n is the number of kids. We iterate through the list twice - one to find the maximum number of candies and one to check each kid.
 

Space Complexity:

- O(n) -> To store the result for each kid.

'''