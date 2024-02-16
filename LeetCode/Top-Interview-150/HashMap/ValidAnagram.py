class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check for the length
        if len(s) != len(t):
            return False

        # Initialize two HashMaps
        S = {}
        T = {}

        # Count the frequency of each character in s
        for char in s:
            S[char] = S.get(char, 0) + 1

        # Count the frequency of each character in t
        for char in t:
            T[char] = T.get(char, 0) + 1

        # Compare the two dictionaries
        return S == T
    
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # This should print True
print(solution.isAnagram("rat", "car"))  # This should print False

'''

Time Complexity:

- We iterate through each character in both the strings, hence the time complexity would be O(n). 
[O(n + m), if the lengths of the strings are different which rules them out from being an anagram)

- I think the same approach as above should work for unicode characters as well. I am thinking that the implemented algorithm is not dependent on the nature of characters.

'''