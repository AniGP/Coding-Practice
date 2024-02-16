# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
size = Counter(map(int, input().split()))
N = int(input())

total_earnings = 0

for _ in range(N):
    
    shoe_size, price = map(int, input().split())
    
    if size[shoe_size]> 0:
        
        total_earnings+= price
        size[shoe_size]-= 1
        
print(total_earnings)