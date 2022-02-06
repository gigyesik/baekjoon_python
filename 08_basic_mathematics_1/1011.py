# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

import sys

def fmttac(xy: list) -> int:
    x = xy[0]
    y = xy[1]
    length = y - x
    counter = 1

    while True:
        if length == 1:
            return 1
        else:
            if (counter ** 2) < length <= ((counter + 1) ** 2):
                if length >= (((counter ** 2) + 1) + ((counter + 1) ** 2)) / 2:
                    return (counter * 2) + 1
                else:
                    return counter * 2
            else:
                counter += 1

def main():
    case = int(input())
    for _ in range(case):
        xy = sys.stdin.readline().split()
        listxy = list(map(int, xy))
        print(fmttac(listxy))

main()

#success
