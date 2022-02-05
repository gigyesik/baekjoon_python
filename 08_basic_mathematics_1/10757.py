# 큰 수 A + B
# https://www.acmicpc.net/problem/10757

import sys

def maxnum(ablist: list) -> int:
    a = ablist[0]
    b = ablist[1]
    return a+b

def main():
    ablist = sys.stdin.readline().split()
    intablist = list(map(int, ablist))
    print(maxnum(intablist))

main()