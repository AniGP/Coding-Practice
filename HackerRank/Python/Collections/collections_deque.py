# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

N = int(input())
D = deque()

for _ in range(N):
    
    commands = input().split()
    
    if commands[0] == 'append':
        D.append(int(commands[1]))
        
    elif commands[0] == 'appendleft':
        D.appendleft(int(commands[1]))
        
    elif commands[0] == 'pop':
        D.pop()
        
    elif commands[0] == 'popleft':
        D.popleft()
        
print(*D)