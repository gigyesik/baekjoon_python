# A + B - 4

import sys

while True:
    a = sys.stdin.readline().split()
    A = list(map(int, a))
    if len(a) == 0:
        break
    print(sum(A))