#A+B - 8

import sys
case = int(input())
A = [None] * case
B = [None] * case
C = [None] * case

for i in range(case):
    a = sys.stdin.readline().split()
    A[i] = int(a[0])
    B[i] = int(a[1])
    C[i] = A[i] + B[i]

for i in range(case):
    print(f'Case #{i+1}: {A[i]} + {B[i]} = {C[i]}')