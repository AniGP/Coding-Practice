class Solution 
{
    public int strStr(String haystack, String needle) 
    {
        // If the needle is an empty string, return 0
        if (needle.isEmpty()) 
        {
            return 0;
        }

        // Iterate through all possible starting positions of 'needle' in 'haystack'
        // without going beyond the end of 'haystack'
        for (int i = 0; i <= haystack.length() - needle.length(); i++) 
        {
            // Look at a substring of haystack which has the same length as needle
            String substring = haystack.substring(i, i + needle.length());

            if (substring.equals(needle)) 
            {
                return i;
            }
        }

        return -1;
        
    }
}

/*

The time complexity  is O((n-m+1) * m), where:
- n is the length of the 'haystack' string.
- m is the length of the 'needle' string.


1. The outer loop runs from 0 to (n - m + 1), where n is the length of haystack and m is the length of needle. 
This is because once you reach a point where the remaining length of haystack 
is less than needle, it's impossible for needle to fit in haystack. 
So, it runs at most (n - m + 1) iterations.

2. For each iteration of the outer loop, you extract a substring of length m from haystack. 
This substring extraction takes O(m) time.

3. You compare the extracted substring with needle using if substring == needle:. 
This comparison takes O(m) time in the worst case.

Therefore, for each iteration of the outer loop, it takes O(m) time.
Since the outer loop can run at most (n - m + 1) times, the overall time complexity is O((n - m + 1) * m), 
which simplifies to O(n * m) in the worst case.

If needle is short and haystack is long, the algorithm can be relatively efficient. 
However, if both needle and haystack are long, the time complexity can be closer to O(n^2) in the worst case.

There is scope of improvement using KMP algorithm, which has a time complexity of O(n+m).

*/