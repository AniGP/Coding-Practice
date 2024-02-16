import numpy as np

N, M= map(int, input().split())

arr = np.empty((N, M), dtype=int)

for i in range(N):
    arr[i] = input().split()

print(np.transpose(arr), arr.flatten(), sep='\n')