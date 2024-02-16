n = int(input())
s = set(map(int, input().split()))
N = int(input())

commands = [input() for _ in range(N)]

for command in commands:
    
    command = command.split()
    
    if command[0] == "remove":
        s.remove(int(command[1]))
        
    elif command[0] == "discard":
        s.discard(int(command[1])) 
        
    elif command[0] == "pop":
        s.pop()
        
print(sum(s))
