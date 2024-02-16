import numpy as np

N, M, P = map(int, input().strip().split())

A = np.array([input().split() for _ in range(N)], dtype=int)
B = np.array([input().split() for _ in range(M)], dtype=int)

print(np.concatenate((A, B)))
