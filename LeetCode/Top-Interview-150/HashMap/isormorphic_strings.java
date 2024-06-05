class Solution 
{
    public boolean isIsomorphic(String s, String t) 
    {
        // Mappings for s to t and t to s
        HashMap<Character, Character> sToT = new HashMap<>();
        HashMap<Character, Character> tToS = new HashMap<>();

        // Iterate through each character in s and t

        for(int i=0; i < s.length(); i++)
        {
            char charS = s.charAt(i);
            char charT = t.charAt(i);

            // Now check if the mapping exists, and if it exists, is it
            // correct or not

            
            if (sToT.containsKey(charS) && sToT.get(charS) != charT || 
                tToS.containsKey(charT) && tToS.get(charT) != charS) {
                return false;
            }

            // Update mapping, create one if not present

            sToT.put(charS, charT);
            tToS.put(charT, charS); 
        }

        return true;    
    }

    public static void main(String[] args) 
    {
        Solution solution = new Solution();
        
        System.out.println(solution.isIsomorphic("egg", "add")); // Output: true
        System.out.println(solution.isIsomorphic("foo", "bar")); // Output: false
        System.out.println(solution.isIsomorphic("paper", "title")); // Output: true
    }
}

/*
 Time Complexity:

- O(n)
- Both the strings are scanned in a single pass
 */