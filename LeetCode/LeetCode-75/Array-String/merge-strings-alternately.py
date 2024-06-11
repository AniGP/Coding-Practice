class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = [] # empty list to store the result string

        len1 = len(word1)
        len2 = len(word2)

        # Iterating over the maximum length among both the strings

        for i in range(max(len1, len2)):

            # Append character from word1 if within range
            if i < len1:
                result.append(word1[i])

            # Append character from word2 if within range
            if i < len2:
                result.append(word2[i])

        return ''.join(result)
    

# Create an instance of the Solution class
sol = Solution()

# Test cases
test_cases = [
    ("abc", "pqr"),   # Expected output: "apbqcr"
    ("ab", "pqrs"),  # Expected output: "apbqrs"
    ("abcd", "pq")   # Expected output: "apbqcd"
]

# Run the test cases
for word1, word2 in test_cases:
    result = sol.mergeAlternately(word1, word2)
    print(f"mergeAlternately({word1}, {word2}) -> {result}")

'''
Time Complexity:

- O(n). Each character in the respective string is looked at once.

Space Complexity:

- O(n). The maximum amount of space required would be the length of both the strings combined.
'''