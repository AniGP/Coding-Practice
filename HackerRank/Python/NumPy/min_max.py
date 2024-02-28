import numpy as np

N, M=map(int, input().split())

arr=[list(map(int, input().split())) for _ in range(N)]

print(np.max(np.min(arr, axis=1)))