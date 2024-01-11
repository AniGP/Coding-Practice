class Solution 
{
    public int mySqrt(int x) 
    {
        // If x is less than 2, its square root is x itself
        if (x < 2) 
        {
            return x;
        }

        // Initialize the search range
        long left = 1, right = x / 2;

        while (left <= right) 
        {
            // Calculate the mid-point of the current search range
            long mid = left + (right - left) / 2;

            // Square the mid-point value
            long squared = mid * mid;

            // Check if the squared mid-point is greater than x
            if (squared > x) 
            {
                right = mid - 1;
            }
            
            else 
            {
                left = mid + 1;
            }
        }

        // Return right as the integer square root of x
        return (int) right;
    }
}

/*

The time complexity of the binary search algorithm for finding the square root of `x` is O(log n), where n is the input number `x`. 
The algorithm repeatedly divides the search range in half, starting from a range of 1 to x/2 (for x greater than 1).

*/
