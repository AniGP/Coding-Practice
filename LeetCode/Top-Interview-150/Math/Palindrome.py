class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        num, reverse = x, 0

        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return num == reverse

# Driver code to test the method
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    print("Is 121 a palindrome? ", solution.isPalindrome(121))   # Should return True
    print("Is -121 a palindrome? ", solution.isPalindrome(-121)) # Should return False
    print("Is 10 a palindrome? ", solution.isPalindrome(10))     # Should return False
    print("Is 12321 a palindrome? ", solution.isPalindrome(12321)) # Should return True
    print("Is 0 a palindrome? ", solution.isPalindrome(0))       # Should return True

'''

Time Complexity: O(n)

- We loop through all the digits in the number once.

'''