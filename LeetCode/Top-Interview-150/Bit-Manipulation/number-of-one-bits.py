class Solution:
    def hammingWeight(self, n: int) -> int:

        # Convert the number to binary representation and skip the first two characters '0b'
        binary_representation = bin(n)[2:]
        
        # Count and return the number of '1's in the binary representation
        return binary_representation.count('1')

# Driver Code
if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.hammingWeight(11))  # Output: 3
    print(solution.hammingWeight(128)) # Output: 1
    print(solution.hammingWeight(2147483645)) # Output: 30

'''

Credits:

https://leetcode.com/problems/number-of-1-bits/solutions/4341511/faster-lesser-3-methods-simple-count-brian-kernighan-s-algorithm-bit-manipulation-explained

Time Complexity:
- The time complexity of converting an integer to its binary representation and counting the '1's 
both depend on the number of bits in the number. Since the problem constrains the number to be at 
most 2^31 - 1, the binary representation will have at most 31 bits. Thus, the overall operation 
is O(1) in terms of the input's size because the size is capped by 31 bits.

Space Complexity:
- The space complexity is also O(1) because the storage used does not scale with the size of the 
input but is constant due to the fixed maximum size of the binary representation.

'''