class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not str:
            return ""

        comm_pref = ""

        # Let's check the first string in the list
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Now we'll have to check other strings as well
            for word in strs[1:]:

                if i>=len(word) or word[i] != char:
                    
                    return comm_pref

            comm_pref = comm_pref + char
        
        return comm_pref
    
'''
The time complexity for this solution would be O(m*n), where 'm' is the length of the longest string and 'n' is the number of strings in the list, due to the following reasons:

i.) We go through each character in string in the outer loop
ii.) The inner loop iterated through all the strings in the list for character matches
iii.) In the worst case, it has to go through all the characters in the string and all the strings in the list
'''