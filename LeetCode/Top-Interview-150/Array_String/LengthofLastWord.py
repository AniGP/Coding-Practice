class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = len(s)
        count = 0

        for i in range(length-1, -1, -1):

            if s[i] != ' ':
                count += 1

            elif count > 0:
                break

        return count
    
if __name__ == "__main__":
    
    sol = Solution()

    
    examples = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy", ""]

    
    for example in examples:
        length = sol.lengthOfLastWord(example)
        print(f"The length of the last word in '{example}' is: {length}")

'''

The time complexity of the function is O(n), where n is the length of the input string.

- The function involves a single loop that traverses the string from its end to the start. 
In the worst case, this loop might have to go through the entire length of the string if the last word 
is at the beginning of the string or if there's only one word in the string. 

- Inside the loop, the operations performed (checking if a character is a space, incrementing the count, 
and breaking out of the loop) are all constant time operations, i.e., their execution time does not depend 
on the size of the input.

'''