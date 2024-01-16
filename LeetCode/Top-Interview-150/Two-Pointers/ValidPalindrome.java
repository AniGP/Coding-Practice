class Solution 
{
    public boolean isPalindrome(String s) 
    {
        // Use StringBuilder

        StringBuilder chars = new StringBuilder();

        // Check for alphanumeric and append to chars
        for(int i=0; i<s.length(); i++)
        {
            char ch = s.charAt(i);

            if(Character.isLetterOrDigit(ch))
            {
                chars.append(Character.toLowerCase(ch));
            }
        }

        String new_str = chars.toString();

        // Two Pointers 
        int l = 0;
        int r = new_str.length() - 1;

        while(l<r)
        {
            if(new_str.charAt(l) != new_str.charAt(r))
            {
                return false;
            }

            l ++;
            r --;
        }

        return true;
            
    }

    public static void main(String[] args) 
    {
        Solution sol = new Solution();

        // Test cases
        String[] testStrings = {
            "A man, a plan, a canal: Panama",
            "race a car",
            "",
            " ",
            "a.",
            "Abba",
            "No lemon, no melon"
        };

        for (String string : testStrings) 
        {
            boolean result = sol.isPalindrome(string);
            System.out.println("Is '" + string + "' a Palindrome? '" + result + "'");
        }
    }

}

/*
 Time Complexity: 

- Appending to List and Converting to Lower Case: O(1)
- Using two pointers for Comparison: O(n)
- O(n)
 */