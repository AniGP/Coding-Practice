public class Solution 
{
    public int lengthOfLastWord(String s) 
    {
        int length = s.length();
        int count = 0;

        for (int i = length - 1; i >= 0; i--) 
        {
            if (s.charAt(i) != ' ') 
            {
                count++;
            } 
            
            else if (count > 0) 
            {
                break;
            }
        }

        return count;
    }

    public static void main(String[] args) 
    {
        Solution sol = new Solution();

        String[] examples = {"Hello World", "   fly me   to   the moon  ", "luffy is still joyboy", ""};

        for (String example : examples) 
        {
            int length = sol.lengthOfLastWord(example);
            System.out.println("The length of the last word in '" + example + "' is: " + length);
        }
    }
}

/*

The time complexity of the function is O(n), where n is the length of the input string.

- The function involves a single loop that traverses the string from its end to the start. 
In the worst case, this loop might have to go through the entire length of the string if the last word 
is at the beginning of the string or if there's only one word in the string. 

- Inside the loop, the operations performed (checking if a character is a space, incrementing the count, 
and breaking out of the loop) are all constant time operations, i.e., their execution time does not depend 
on the size of the input.

*/