class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)

        # Start from the last digit and move to the first digit

        for i in range(n-1, -1, -1):

            # If the current digit is < 9, icnrement
            if digits[i] < 9:
                
                digits[i]+=1
                return digits
        
            digits[i] = 0 # If 9, set the current digit to 0 and it will roll over

        return [1] + digits # If all the digits in the array are 9, the length increases by 1
    
"""

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

"""