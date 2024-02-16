import numpy as np

N, M = map(int, input().split())
arr = np.empty((N, M), dtype=int)

for i in range(N):
    
    arr[i] = list(map(int, input().split()))

print(np.prod(np.sum(arr, axis=0)))