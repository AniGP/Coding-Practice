class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # Create a dictionary to count the frequency of each number

        occurences = {}

        for num in arr:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1

        # Now, let's check if the occurences are unique or not
        check_unique_occurences = set()

        for count in occurences.values():
            if count in check_unique_occurences:
                return False # if the count is repeated, return False

            
            check_unique_occurences.add(count)
        return True # All the counts are unique

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3]))  # Output: True
    print(sol.uniqueOccurrences([1,2]))          # Output: False
    print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))  # Output: True


'''

Credits: https://leetcode.com/problems/unique-number-of-occurrences/solutions/4577893/beats-100-users-c-java-python-javascript-2-approaches-explained/?envType=study-plan-v2&envId=leetcode-75

Time Complexity:
- O(n), where n is the length of the array. We go through the array twice, once for counting and once for checking uniqueness.

Space Complexity:
- O(k), where k is the number of unique numbers in the array. In the worst case, this is O(n) if all numbers are unique.

'''