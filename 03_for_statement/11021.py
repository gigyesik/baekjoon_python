# A + B - 7

import sys
case = int(input())
C = [None] * case

for i in range(case):
    a = sys.stdin.readline().split()
    A = int(a[0])
    B = int(a[1])
    C[i] = A + B

for i in range(case):
    print(f'Case #{i+1}: {C[i]}')
