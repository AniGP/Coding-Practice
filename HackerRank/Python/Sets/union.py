# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

k = a.union(b)

count = 0

for i in range(len(k)):
    
    count += 1

print(count)