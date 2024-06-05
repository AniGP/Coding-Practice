class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):

            if (char in char_to_word and char_to_word[char]!=word) or \
               (word in word_to_char and word_to_char[word]!=char):

               return False
            
            char_to_word[char] = word
            word_to_char[word] = char

        return True

# Create an instance of the Solution class
sol = Solution()

# Test cases
print(sol.wordPattern("abba", "dog cat cat dog"))  # Expected output: True
print(sol.wordPattern("abba", "dog cat cat fish")) # Expected output: False
print(sol.wordPattern("aaaa", "dog cat cat dog"))  # Expected output: False

'''

Time Complexity:

- O(n)
- We iterate through the pattern and the words once

'''