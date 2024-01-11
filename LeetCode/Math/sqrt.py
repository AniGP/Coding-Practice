class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle the edge case where x is less than 2
        if x < 2:
            return x

        # Initialize left and right for binary search
        left, right = 1, x // 2

        # Perform binary search to find the square root
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid

            # Adjust the search range based on the squared value
            if squared > x:
                right = mid - 1
            else:
                left = mid + 1

        # Return the floor of the square root
        return right

'''

The time complexity of the binary search algorithm for finding the square root of `x` is O(log n), where n is the input number `x`. 
The algorithm repeatedly divides the search range in half, starting from a range of 1 to x/2 (for x greater than 1).

'''