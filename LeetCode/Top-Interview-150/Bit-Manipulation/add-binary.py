class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # List to store the result
        result = []
        # Variable to store the carry-over value
        carry = 0
        
        # Initialize two pointers to traverse the binary strings from right to left
        i, j = len(a)-1, len(b)-1
        
        # Loop until both pointers have reached the beginning of their respective strings and there is no carry-over value left
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add the current binary digit in string a, if the pointer is still within bounds
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            # Add the current binary digit in string b, if the pointer is still within bounds
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Calculate the next binary digit in the result by taking the remainder of the sum divided by 2
            result.append(str(total % 2))
            
            # Calculate the next carry-over value by dividing the sum by 2
            carry = total // 2
            
        # Reverse the result and join the elements to form a single string
        return ''.join(reversed(result))

'''

Credits:

https://leetcode.com/problems/add-binary/solutions/3183205/1ms-beats-100-full-explanation-append-reverse-c-java-python3
https://leetcode.com/problems/add-binary/solutions/3182882/super-easy-solution-full-explanation-c-python3-java-commented/

Time Complexity: 

- O(n), where n is the maximum length of the two binary strings. 
This is because we iterate through the strings once.

Space Complexity: 

- O(n), as we store the result in a list which in the worst case can be n+1 characters 
long (if there is a carry that adds a new most significant bit).


'''