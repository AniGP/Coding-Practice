# Define the Solution class with the canConstruct method
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}  # Dictionary for count of letters

        # Populate the HashMap with the frequency of letters in Magazine
        for letter in magazine:
            letters[letter] = letters.get(letter, 0) + 1

        # Checking ransomNote against the HashMap
        for letter in ransomNote:
            if letters.get(letter, 0) == 0:
                return False  # If the count is 0 or the letter is not in the HashMap

            letters[letter] -= 1  # If letter found, decrement the count

        return True  # If we can construct by using the letters from magazine

solution = Solution()

# Example 1
ransomNote1 = "a"
magazine1 = "b"
print(f"Can construct \"{ransomNote1}\" from \"{magazine1}\": {solution.canConstruct(ransomNote1, magazine1)}")

# Example 2
ransomNote2 = "aa"
magazine2 = "ab"
print(f"Can construct \"{ransomNote2}\" from \"{magazine2}\": {solution.canConstruct(ransomNote2, magazine2)}")

# Example 3
ransomNote3 = "aa"
magazine3 = "aab"
print(f"Can construct \"{ransomNote3}\" from \"{magazine3}\": {solution.canConstruct(ransomNote3, magazine3)}")

'''

Time Complexity:

- O(m + n)
- m -> length of magazine, n -> length of ransomNote
- Each letter has to be iterated in both the words
- Inserting and Accessing are constant time operations


'''