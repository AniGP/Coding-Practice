class Solution 
{
    public int maxProfit(int[] prices) 
    {
        int minPrice = Integer.MAX_VALUE;
        int maxPrice = 0;

        for(int price : prices)
        {
            if(price < minPrice)
            {
                minPrice = price;
            }

            else if(price - minPrice > maxPrice)
            {
                maxPrice = price - minPrice;
            }
        }

        return maxPrice;
    }

    public static void main(String[] args) 
    {
        Solution solution = new Solution();

        // Test case 1
        int[] prices1 = {7, 1, 5, 3, 6, 4};
        System.out.println("Max profit for prices1: " + solution.maxProfit(prices1));  // Expected output: 5

        // Test case 2
        int[] prices2 = {7, 6, 4, 3, 1};
        System.out.println("Max profit for prices2: " + solution.maxProfit(prices2));  // Expected output: 0
    }
        
}