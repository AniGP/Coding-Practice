def isSubsequence(s, t):

    i, j = 0, 0

    while i < len(s) and j < len(t):

        if s[i] == t[j]:

            i += 1

        j += 1

    return i == len(s)

print(isSubsequence("abc", "ahbgdc"))  # Expected output: true
print(isSubsequence("axc", "ahbgdc"))  # Expected output: false

'''

- Time Complexity : O(len(t))

- The loop runs at most len(t) times because it iterates through each character in t once.

-  Within each iteration of the loop, we perform a constant-time operation by comparing characters from s and t, 
and possibly incrementing the pointer i. It is tied to increment of t.

'''