public class Solution 
{
    public boolean wordPattern(String pattern, String s) 
    {
        String[] words = s.split(" ");
        
        if (pattern.length() != words.length) 
        {
            return false;
        }
        
        Map<Character, String> charToWord = new HashMap<>();
        Map<String, Character> wordToChar = new HashMap<>();
        
        for (int i = 0; i < pattern.length(); i++) 
        {
            char ch = pattern.charAt(i);
            String word = words[i];
            
            if (charToWord.containsKey(ch) && !charToWord.get(ch).equals(word)) 
            {
                return false;
            }
            
            if (wordToChar.containsKey(word) && wordToChar.get(word) != ch) 
            {
                return false;
            }
            
            charToWord.put(ch, word);
            wordToChar.put(word, ch);
        }
        
        return true;
    }
    
    public static void main(String[] args) 
    {
        Solution sol = new Solution();

        // Test cases
        System.out.println(sol.wordPattern("abba", "dog cat cat dog"));  // Expected output: true
        System.out.println(sol.wordPattern("abba", "dog cat cat fish")); // Expected output: false
        System.out.println(sol.wordPattern("aaaa", "dog cat cat dog"));  // Expected output: false
    }
}

/*

Time Complexity:

- O(n)
- We iterate through the pattern and the words once

 */