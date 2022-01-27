# 최소, 최대

import sys

case = int(input())
num = [None] * case
a = sys.stdin.readline().split()

def get_min() -> int:
    for i in range(case):
        num[i] = int(a[i])
    temp = num[0]
    for j in range(1, case):
        if num[j] <= num[j - 1]:
            temp = num[j]
        else:
            pass
    return temp

def get_max() -> int:
    for i in range(case):
        num[i] = int(a[i])
    temp = num[0]
    for j in range(1, case):
        if num[j] >= num[j - 1]:
            temp = num[j]
        else:
            pass
    return temp

def minmax() -> int:

    for i in (range(case)):
        num[i] = int(a[i])
    print(get_min(), get_max(), end=' ')


minmax()
