# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = set(map(int, input().split()))

m = int(input())

for i in range(m):
    
    s = input().split()
    
    if s[0] == "intersection_update":
        
        b = set(map(int, input().split()))
        a.intersection_update(b)
        
    elif s[0] == "update":
        
        b = set(map(int, input().split()))
        a.update(b)
        
    elif s[0] == "symmetric_difference_update":
        
        b = set(map(int, input().split()))
        a.symmetric_difference_update(b)
        
    elif s[0] == "difference_update":
        
        b = set(map(int, input().split()))
        a.difference_update(b)
        
print(sum(a))