# Enter your code here. Read input from STDIN. Print output to STDOUT

scores = []
n, x = map(int, input().split())

for i in range(x):
    scores.append(list(map(float, input().split())))
    
print(*[sum(student)/len(student) for student in zip(*scores)], sep='\n')