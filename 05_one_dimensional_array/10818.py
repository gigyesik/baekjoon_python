# 최소, 최대

import sys

def minmax() -> int:
    case = int(input())
    num = [None] * case
    a = sys.stdin.readline().split()
    for i in (range(case)):
        num[i] = int(a[i])
    print(min(num), max(num), end=' ')


minmax()
