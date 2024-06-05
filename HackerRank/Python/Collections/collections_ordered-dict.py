# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N=int(input())
od = OrderedDict()

for _ in range(N):
    items=input().rsplit(' ', 1)
    
    if items[0] in od:
        od[items[0]] += int(items[1])
    else:
        od[items[0]] =int(items[1])
        
for key, value in od.items():
    print(key, value)