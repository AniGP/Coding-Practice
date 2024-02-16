# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
country = set()

for _ in range(n):
    country.add(input())
print(len(country))