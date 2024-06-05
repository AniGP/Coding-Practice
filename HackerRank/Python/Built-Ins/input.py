# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k =map(int, input().split())
P=input()

if eval(P)==k:
    print(True)
    
else:
    print(False)