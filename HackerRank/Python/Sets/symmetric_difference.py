# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
a = set(input().split())

N = int(input())
b = set(input().split())

ans = []

a_diff = a.difference(b)
b_diff = b.difference(a)

ans += [int(num) for num in a_diff]
ans += [int(num) for num in b_diff]

for num in sorted(ans):
    print(num)