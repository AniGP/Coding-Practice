class Solution:

    def maxProfit(self, prices):

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

if __name__ == "__main__":

    solution = Solution()

    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Max profit for prices1:", solution.maxProfit(prices1))  # Expected output: 5

    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print("Max profit for prices2:", solution.maxProfit(prices2))  # Expected output: 0

'''

The time complexity is O(n), where n is the number of days, or the length of the array.

- The solution iterates through the  array exactly once.

- Within each iteration, the operations performed (updating min_price and max_profit) are constant time 
operations, meaning their execution time does not depend on the size of the input array.

'''