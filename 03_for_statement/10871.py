# X보다 작은 수

import sys

a = sys.stdin.readline().split()
N = int(a[0])
X = int(a[1])
A = [None] * N

b = list(sys.stdin.readline().split())
B = list(map(int, b))

for i in range(N):
    A[i] = B[i]
    if A[i] < X:
        print(f'{A[i]}', end=' ')