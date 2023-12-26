class Solution 
{
    public boolean isValid(String s) 
    {
        // Empty stack

        Stack<Character> stack = new Stack();

        // A hashmap for mapping the pair of parantheses

        HashMap<Character, Character> parantheses = new HashMap<>();
        parantheses.put('(', ')');
        parantheses.put('{', '}');
        parantheses.put('[', ']');

        for(char c : s.toCharArray())
        {
            // If the character is an opening bracket, push it to the stack
            if(c == '(' || c == '{' || c == '[')
            {
                stack.push(c);
            }

            // If the character is a closing bracket, check whether the stack is empty or not
            else
            {
                if(stack.isEmpty())
                {
                    return false;
                }

                char top = stack.pop();

                // Check whether the popped element from the stack matches with the current character
                if (parentheses.get(top) != c) 
                {
                    return false;
                }
            }
        }

        return stack.isEmpty();       
    }

}

/*
The time complexity of this solution is O(n), where n is the length of the input string s.

- We iterate through each character in the input string once, processing each character in constant time.
- In the worst case, we push each open parenthesis onto the stack and pop it off when we encounter its corresponding closing parenthesis. 
In this case, we perform push and pop operations for each character in the string.
- Since we perform a constant amount of work for each character, the overall time complexity is linear, O(n), where n is the length of the input string.
'''
*/