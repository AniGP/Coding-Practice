class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

        for num in nums[1:]:

            if num == end + 1:
                end = num
            
            else:

                if start == end:
                    ranges.append(str(start))

                else:
                    ranges.append(f"{start}->{end}")
                
                start = end = num
    
        # Add the last range
        
        if start == end:
            ranges.append(str(start))
        
        else:
            ranges.append(f"{start}->{end}")

        return ranges
    
'''

Time Compexlity:

- O(n)
- Each element is visited once and there are constant time operations 
(such as adding range to the ranges list, checking if the current number is consecutive to the previous one etc.)

'''