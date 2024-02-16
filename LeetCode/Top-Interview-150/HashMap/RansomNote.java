class Solution 
{
    public boolean canConstruct(String ransomNote, String magazine) 
    {
        // for count of letters
        HashMap<Character, Integer> letters = new HashMap<>();

        // Populate the HashMap with the frequency of letters in the magazine
        for (char letter : magazine.toCharArray()) 
        {
            letters.put(letter, letters.getOrDefault(letter, 0) + 1);
        }

        // Checking ransomNote against the HashMap
        for (char letter : ransomNote.toCharArray()) 
        {
            if (!letters.containsKey(letter) || letters.get(letter) == 0) 
            {
                // If the count is 0 or the letter is not in the HashMap, return false
                return false;
            }

            // If letter found, decrement the count
            letters.put(letter, letters.get(letter) - 1);
        }

        // If we can construct by using the letters from magazine
        return true;
        
    }

    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        // Example 1
        String ransomNote1 = "a";
        String magazine1 = "b";
        System.out.println("Can construct \"" + ransomNote1 + "\" from \"" + magazine1 + "\": " + solution.canConstruct(ransomNote1, magazine1));

        // Example 2
        String ransomNote2 = "aa";
        String magazine2 = "ab";
        System.out.println("Can construct \"" + ransomNote2 + "\" from \"" + magazine2 + "\": " + solution.canConstruct(ransomNote2, magazine2));

        // Example 3
        String ransomNote3 = "aa";
        String magazine3 = "aab";
        System.out.println("Can construct \"" + ransomNote3 + "\" from \"" + magazine3 + "\": " + solution.canConstruct(ransomNote3, magazine3));
    }
}

/*

Time Complexity:

- O(m + n)
- m -> length of magazine, n -> length of ransomNote
- Each letter has to be iterated in both the words
- Inserting and Accessing are constant time operations

 */