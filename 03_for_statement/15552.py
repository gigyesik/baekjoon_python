# 빠른 A+B

import sys
case = int(input())
C = [None] * case

for i in range(case):
    a = sys.stdin.readline().split()
    A = int(a[0])
    B = int(a[1])
    C[i] = A + B

for i in range(case):
    print(C[i])