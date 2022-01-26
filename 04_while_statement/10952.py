# A+B - 5

import sys

while True:
    a = sys.stdin.readline().split()
    A = list(map(int, a))
    if sum(A) > 0:
        print(sum(A))
    else:
        break
