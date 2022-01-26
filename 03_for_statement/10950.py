#A+B-3

case = int(input())
C = [None] * case

for i in range(case):
    a = input().split()
    A = int(a[0])
    B = int(a[1])
    C[i] = A + B

for i in range(case):
    print(C[i])