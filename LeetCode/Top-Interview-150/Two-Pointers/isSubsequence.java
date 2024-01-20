class Solution 
{
    public boolean isSubsequence(String s, String t) 
    {
        int i = 0, j = 0;

        while (i < s.length() && j < t.length()) 
        {
            if (s.charAt(i) == t.charAt(j)) 
            {
                i++;
            }
            j++;
        }

        return i == s.length();
    }

    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        // Test cases
        System.out.println(solution.isSubsequence("abc", "ahbgdc")); // Expected output: true
        System.out.println(solution.isSubsequence("axc", "ahbgdc")); // Expected output: false
    }
}

/*

- Time Complexity : O(len(t))

- The loop runs at most len(t) times because it iterates through each character in t once.

-  Within each iteration of the loop, we perform a constant-time operation by comparing characters from s and t, 
and possibly incrementing the pointer i. It is tied to increment of t.

 */