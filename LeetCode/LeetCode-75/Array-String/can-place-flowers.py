class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # Length of Flowerbed
        length = len(flowerbed)
        
        # Iterate over each plot in the flowerbed
        for i in range(length):

            # Check the adjacent plots
            
            # Check there is no flower in the previous plot 
            # or it's the start of the array

            # Check there is no flower in the next plot 
            # or it's the end of the array

            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0):
                
                flowerbed[i] = 1 # Mark this plot as planted
                n = n - 1 # Reduce the count of flowers to be planted

        # If the loop finishes and n is still positive, 
        # return false as there are not enough free spaces in the flowerbed 
        # to plant all flowers.
        if n > 0:
            return False
        
        return True # If n becomes 0, return true as all flowers have been planted.
    
sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
    
'''
    
Time Complexity:

- O(n), where n is the number of plots in the flowerbed. This is because we traverse the flowerbed list once.

Space Complexity:

- O(1). The flowerbed list is being modified in-place, so extra space is being used.
    
'''