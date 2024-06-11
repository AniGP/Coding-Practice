class Solution(object):

    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        return self.gcdOfStrings(str1, str2[len(str1):])

# Test cases
sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(sol.gcdOfStrings("LEET", "CODE"))    # Output: ""
print(sol.gcdOfStrings("ABCDEF", "ABC"))   # Output: ""

'''

Approach - 

- If concatenating str1 and str2 is not equal to concatenating str2 and str1, 
then there's no common divisor possible. So, we return an empty string "".

- If the lengths of str1 and str2 are equal, and the concatenated strings are equal, 
then str1 (or str2) itself is the greatest common divisor, and we return str1 (or str2).

- If the length of str1 is greater than the length of str2, it means that str1 contains str2 
as a prefix. In this case, we recurse with the substring of str1 after removing (slicing) 
the prefix that matches str2.

- If the length of str2 is greater than the length of str1, it means that str2 contains str1 as a 
prefix. In this case, we recurse with the substring of str2 after removing (slicing) the prefix that 
matches str1.


Time Complexity - 

- Recursive Calls: 

    - Each recursive call reduces the problem size by the length of the shorter string 
    (either `str1` or `str2`). 
    - The total number of recursive calls depends on the ratio of the lengths of the two strings.

- String Operations: 

    - The primary operations inside each call are string concatenation and substring extraction. 
    - The concatenation `str1 + str2` and `str2 + str1` are both O(n + m) operations, 
    where `n` and `m` are the lengths of `str1` and `str2` respectively.

- Overall Complexity: 

    - The complexity of each recursion level is O(n + m) due to the concatenation, 
    and the number of recursive calls can be approximated by the ratio of the lengths of the strings. 
    
    - In the worst case, this method could perform O(min(n, m)) recursive calls before the base case 
    is reached (similar to the Euclidean algorithm). Thus, the worst-case time complexity can 
    be O((n + m) * min(n, m)).

Space Complexity - 

- Recursive Stack:

    - The recursion depth is bounded by O(min(n, m)) because each recursion reduces the length of 
    one string until the strings are equal or empty.

- String Storage:

    - Each recursive call involves substring operations.
    
    - However, considering the maximum space used by substrings and the concatenation operation, 
    the additional space is bounded by O(n + m) due to string concatenation.

- Overall Space Complexity: 

    - O((n + m) * min(n, m)) when considering the recursion stack and the storage for substrings 
    and concatenated strings.

'''    