class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Mappings from s to t and t to s
        s_to_t = []
        t_to_s = []

        # Iterate through each character in s and t, checking mapping from
        # s to t

        for char_s in s:
            
            s_to_t.append(s.index(char_s))
        
        for char_t in t:

            t_to_s.append(t.index(char_t))
        
        if s_to_t == t_to_s:
            return True

        return False
    
solution = Solution()

print(solution.isIsomorphic("egg", "add"))  # Output: True
print(solution.isIsomorphic("foo", "bar"))  # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True

'''

Time Complexity:

- O(n^2)
- The whole string is scanned for both s and t

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Mappings from s to t and t to s
        s_to_t = {}
        t_to_s = {}

        # Iterate through each character in s and t
        for char_s, char_t in zip(s, t):
            # Check if the mapping exists and is correct
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
               (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False
            
            # Create or update the mapping
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True

if __name__ == "__main__":

    solution = Solution()
    
    print(solution.isIsomorphic("egg", "add"))  # Output: True
    print(solution.isIsomorphic("foo", "bar"))  # Output: False
    print(solution.isIsomorphic("paper", "title"))  # Output: True


'''

Time Complexity:

- O(n)
- Both the strings are scanned in a single pass

'''