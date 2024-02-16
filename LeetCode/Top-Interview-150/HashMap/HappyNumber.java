public class Solution 
{
    
    // Helper method to calculate the sum of squares of digits of a number
    private int sumOfSquares(int num) 
    {
        int sum = 0;

        while (num > 0) 
        {
            int digit = num % 10;
            sum += digit * digit;
            num /= 10;
        }

        return sum;
    }

    public boolean isHappy(int n) 
    {
        // HashMap to keep track of sums we have seen
        HashMap<Integer, Boolean> sums = new HashMap<>();
        
        while (n != 1 && !sums.containsKey(n)) 
        {
            sums.put(n, true); // Mark the current sum as seen
            n = sumOfSquares(n); // Calculate the next sum of squares
        }
        
        // If n is 1, it's a happy number; otherwise, it's not
        return n == 1;
    }
}

/*

Time Complexity:

- O(log n)

*/