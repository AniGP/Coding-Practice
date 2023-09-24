class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_val = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}

        total_val = 0
        prev_val = 0

        for num in s:

            val = roman_val[num]
            total_val+=val

            if val > prev_val:
                total_val = total_val - 2*prev_val
            prev_val = val
        
        return total_val
    
'''
The time complexity for this solution would be O(n) due to the following reasons:

i.) We go through each string, exactly once from left to right.
ii.) The number of iterations is directly proportional to the length of the string.
iii.) Looking up the equivalent integer value in the dictionary, comparison, updating are all constant time operations.
'''