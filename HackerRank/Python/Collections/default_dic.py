# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

N, M = map(int, input().split())
indices = defaultdict(list)

for i in range(N):
    indices[input()].append(i+1)

for i in range(M):
    inp = input()
    print(*indices[inp] if indices[inp] else [-1])