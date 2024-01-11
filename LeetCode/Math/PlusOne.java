public class PlusOne 
{
    public int[] plusOne(int[] digits) {
        int n = digits.length;

        // Starting from the last digit and moving to the first
        for (int i = n - 1; i >= 0; i--) {
            // If the current digit is less than 9, increment and return
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            // Set the current digit to 0 as it's 9 and will roll over
            digits[i] = 0;
        }

        // If all the digits were 9, the array length increases by 1 with a leading 1
        int[] newDigits = new int[n + 1];
        newDigits[0] = 1;
        return newDigits;
    }
    
} 

/*

The time complexity of the plusOne solution can be calculated 
based on the operations performed on the input list digits.

- Iteration Through the List: The function iterates through the list of digits starting from the end 
towards the beginning. In the worst-case scenario, where all digits are 9 (e.g., [9, 9]), 
the loop runs through each digit exactly once. Therefore, if there are n digits, the loop runs n times.

- Carry Handling and List Expansion: The operation inside the loop is a constant-time operation, 
as it either increments a digit or sets it to 0. In the case where an additional digit 
is added (for example, when the input is all 9s, like [9, 9] resulting in [1, 0, 0]), 
this is done outside the loop with a single operation.

Hence, the time complexity of the function is O(n), where n is the number of digits in the input list.

 */