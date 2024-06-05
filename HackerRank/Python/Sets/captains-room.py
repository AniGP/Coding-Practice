# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
nums = list(map(int, input().split()))

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for key, value in count.items():
    if value != n:
        res = key
        break

print(res)