public class IntegerToRoman {

    public int romanToInt(String s) {

        Map<Character, Integer> roman_val = new HashMap<>();
        roman_val.put('I', 1);
        roman_val.put('V', 5);
        roman_val.put('X', 10);
        roman_val.put('L', 50);
        roman_val.put('C', 100);
        roman_val.put('D', 500);
        roman_val.put('M', 1000);

        int tot_val = 0;
        int prev_val = 0;

        for(int i=0; i<s.length(); i++)
        {
            int val = roman_val.get(s.charAt(i));
            tot_val+=val;

            if(val > prev_val)
            {
                tot_val = tot_val - 2*prev_val;
            }

            prev_val = val;
        }

        return tot_val;
        
    }    
}

/*
The time complexity for this solution would be O(n) due to the following reasons:

i.) We go through each string, exactly once from left to right.
ii.) The number of iterations is directly proportional to the length of the string.
iii.) Looking up the equivalent integer value in the dictionary, comparison, updating are all constant time operations.
*/