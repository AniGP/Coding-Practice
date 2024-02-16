import numpy as np

N, M = map(int, input().split())

A = np.array([input().split() for _ in range(N)], dtype=int)
B = np.array([input().split() for _ in range(N)], dtype=int)

print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))
print(np.mod(A, B))
print(np.power(A, B))