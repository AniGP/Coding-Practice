class Solution:
    
    def isHappy(self, n: int) -> bool:

        # Function to calculate the Sum of Squares

        def SumofSquares(num):

            sum = 0

            while num:

                digit = num % 10
                sum += digit ** 2
                num //= 10
            
            return sum

        # HashMap to keep track of sums

        sums = {}

        while n!=1 and n not in sums:

            sums[n] = True # Marking the current sum as "tracked"
            n = SumofSquares(n) # Calculate the next

        return n == 1 # Returned if it's a happy number
    
'''

Time Complexity:

- O(log n)

'''