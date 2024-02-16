import java.util.HashMap;

class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        // Check for the length
        if (s.length() != t.length()) 
        {
            return false;
        }

        // Initialize two HashMaps
        HashMap<Character, Integer> S = new HashMap<>();
        HashMap<Character, Integer> T = new HashMap<>();

        // Count the frequency of each character in s
        for (char c : s.toCharArray()) 
        {
            S.put(c, S.getOrDefault(c, 0) + 1);
        }

        // Count the frequency of each character in t
        for (char c : t.toCharArray()) 
        {
            T.put(c, T.getOrDefault(c, 0) + 1);
        }

        // Compare the two HashMaps
        return S.equals(T);
    }
}


public class Main 
{
    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        System.out.println(solution.isAnagram("anagram", "nagaram")); // This should print true
        System.out.println(solution.isAnagram("rat", "car")); // This should print false
    }
}


/*

Time Complexity:

- We iterate through each character in both the strings, hence the time complexity would be O(n). 
[O(n + m), if the lengths of the strings are different which rules them out from being an anagram)

- I think the same approach as above should work for unicode characters as well. I am thinking that the implemented algorithm is not dependent on the nature of characters.

*/