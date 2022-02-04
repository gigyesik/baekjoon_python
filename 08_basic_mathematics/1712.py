# 손익분기점
# https://www.acmicpc.net/problem/1712

import sys

def brevpooint(data: list) -> int:
    A = data[0]
    B = data[1]
    C = data[2]
    counter = 1
    # result = (C - B) * counter - A

    if C - B <= 0:
        return -1
    else:
        counter = A // (C - B)
        return counter + 1

def main():
    data = sys.stdin.readline().split()
    intdata = list(map(int, data))
    print(brevpooint(intdata))

main()
