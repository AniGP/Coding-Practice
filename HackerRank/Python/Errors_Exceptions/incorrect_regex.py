# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

T = int(input())

for i in range(0, T):
    
    try:
        # Try to compile regex
        re.compile(input())
        print(True)
            
    except Exception:
        print(False)