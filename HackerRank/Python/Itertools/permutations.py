# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

word, length = input().split()

for p in permutations(sorted(word), int(length)):
    print("".join(p))