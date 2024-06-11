class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # Convert the string into a list 
        s = list(s)

        # Define a set of vowels for quick lookup
        vowels = set('AaEeIiOoUu')

        left = 0
        right = len(s) - 1
        
        # Use a two-pointer technique to find and swap vowels
        while left < right:

            # Move the left pointer until a vowel is found
            while left < right and s[left] not in vowels:
                left = left + 1

            # Move the right pointer until a vowel is found
            while right > left and s[right] not in vowels:
                right = right - 1

            # Swap the vowels
            s[left], s[right] = s[right], s[left]

            # Move both pointers towards the center
            left = left + 1
            right = right - 1
        
        # Convert the list of characters back to a string
        return ''.join(s)
    
sol = Solution()
print(sol.reverseVowels("hello"))  # Output: "holle"
print(sol.reverseVowels("leetcode"))  # Output: "leotcede"

'''

Time Complexity:

- O(n), where n is the length of the string. Each character is checked at most 2 times.

Space Complexity:
- O(1), where n is the length of the string. 
- The swaps are being done in-place, although we have a set for vowels.

'''