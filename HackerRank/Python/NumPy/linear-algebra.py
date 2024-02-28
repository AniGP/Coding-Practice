import numpy as np

N = int(input())
A = np.array([input().split() for _ in range(N)], dtype=float)
print(round(np.linalg.det(A), 2))