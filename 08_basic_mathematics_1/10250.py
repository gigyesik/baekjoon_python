# ACM 호텔
# https://www.acmicpc.net/problem/10250

import sys

def acm(where: list) -> int:
    h = where[0]
    w = where[1]
    n = where[2]
    floor = 1
    room = 1

    while True:
        if h < n:
            n -= h
            floor = n % h
            room += 1
        else:
            floor = n
            if room < 10:
                return int(str(floor)+'0'+str(room))
            else:
                return int(str(floor) + str(room))


def main():
    case = int(input())
    for _ in range(case):
        where = sys.stdin.readline().split()
        listwhere = list(map(int, where))
        print(acm(listwhere))

main()