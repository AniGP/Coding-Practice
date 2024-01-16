class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Intialize a new list
        chars = []

        # Check if a character in the string is alphanumeric
        for ch in s:
            if ch.isalnum():
                # Convert it to lower case and append to list
                chars.append(ch.lower())

        # Convert the list back to the string
        new_str = ''.join(chars)

        # Check for Palindrome using Two Pointers     
        l = 0
        r = len(new_str) - 1

        while(l < r):
            if new_str[l] != new_str[r]:
                return False
            
            l = l + 1
            r = r - 1
        
        return True
    
sol = Solution()

# Test cases
test_strings = [

        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        " ",
        "a.",
        "Abba",
        "No lemon, no melon"
    ]

for string in test_strings:
    result = sol.isPalindrome(test_strings)
    print(f"Is '{string}' a Palindrome? '{result}'")

'''

Time Complexity: 

- Appending to List and Converting to Lower Case: O(1)
- Using two pointers for Comparison: O(n)
- O(n)

'''