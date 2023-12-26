class Solution:
    def isValid(self, s: str) -> bool:

        # Initialize an empty stack
        stack = []

        # This dictionary will have the mapping for the parantheses
        parentheses_mapping = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in '({[':
                # If the character is an opening bracket push it to the stack
                stack.append(char)
            else:
                # If the character is a closing bracket check whether the stack is empty or not
                if len(stack) == 0:
                    return False
                top = stack.pop()
                
                # Check whether the popped element from the stack matches with the current character
                if parentheses_mapping[top] != char:
                    return False
                
        return len(stack) == 0
    
'''
The time complexity of this solution is O(n), where n is the length of the input string s.

- We iterate through each character in the input string once, processing each character in constant time.
- In the worst case, we push each open parenthesis onto the stack and pop it off when we encounter its corresponding closing parenthesis. 
In this case, we perform push and pop operations for each character in the string.
- Since we perform a constant amount of work for each character, the overall time complexity is linear, O(n), where n is the length of the input string.
'''