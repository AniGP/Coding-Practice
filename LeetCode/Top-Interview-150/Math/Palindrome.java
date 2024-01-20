public class Solution 
{
    public boolean isPalindrome(int x) 
    {
        if (x < 0) 
        {
            return false;
        }

        int num = x;
        int reverse = 0;

        while (x > 0) 
        {
            reverse = reverse * 10 + x % 10;
            x = x / 10;
        }

        return num == reverse;
    }

    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        // Test cases
        System.out.println("Is 121 a palindrome? " + solution.isPalindrome(121));   // Should return true
        System.out.println("Is -121 a palindrome? " + solution.isPalindrome(-121)); // Should return false
        System.out.println("Is 10 a palindrome? " + solution.isPalindrome(10));     // Should return false
        System.out.println("Is 12321 a palindrome? " + solution.isPalindrome(12321)); // Should return true
        System.out.println("Is 0 a palindrome? " + solution.isPalindrome(0));       // Should return true
    }
}

/* 

Time Complexity: O(n)

- We loop through all the digits in the number once.

*/