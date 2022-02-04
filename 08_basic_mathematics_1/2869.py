# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

import sys
import math

def snail(height: list) -> int:
    clim = height[0]
    slip = height[1]
    dest = height[2]

    return math.ceil((dest - clim) / (clim - slip)) + 1


def main():
    height = sys.stdin.readline().split()
    listheight = list(map(int, height))
    print(snail(listheight))

main()
