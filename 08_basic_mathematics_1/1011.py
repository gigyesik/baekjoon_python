# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

import sys

def fmttac(xy: list) -> int:
    x = xy[0]
    y = xy[1]
    length = y - x
    sumn = 1
    n = 1
    remain = length - sumn

    while sumn < length:
        sumn = n * (n + 1)
        remain = length - sumn
        if sumn > length:
            n -= 1
            sumn = n * (n + 1)
            remain = length - sumn
            break
        else:
            n += 1

    if remain - n > 1:
        return 2 * n + 2
    else:
        return 2 * n + 1

def main():
    case = int(input())
    for _ in range(case):
        xy = sys.stdin.readline().split()
        listxy = list(map(int, xy))
        print(fmttac(listxy))

main()

# fail
