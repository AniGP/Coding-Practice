public class LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {

        if(strs == null || strs.length == 0)
        {
            return "";
        }

        String comm_pref = "";

        for(int i=0; i<strs[0].length(); i++)
        {
            char curr_char = strs[0].charAt(i);

            for(int j=1; j<strs.length; j++)
            {
                if(i >= strs[j].length() || strs[j].charAt(i) != curr_char)
                {
                    return comm_pref;
                }
            }

            comm_pref = comm_pref + curr_char;
        }

        return comm_pref;
        
    }
    
}

/*
The time complexity for this solution would be O(m*n), where 'm' is the length of the longest string and 'n' is the number of strings in the list, due to the following reasons:

i.) We go through each character in string in the outer loop
ii.) The inner loop iterated through all the strings in the list for character matches
iii.) In the worst case, it has to go through all the characters in the string and all the strings in the list 
*/
