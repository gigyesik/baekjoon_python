# 최소, 최대
# https://www.acmicpc.net/problem/10818

import sys

def get_min(case: int, num: list) -> int:
    temp = num[0]
    for j in range(1, case):
        if num[j] <= num[j - 1]:
            temp = num[j]
        else:
            pass
    return temp

def get_max(case: int, num: list) -> int:
    temp = num[0]
    for j in range(1, case):
        if num[j] >= num[j - 1]:
            temp = num[j]
        else:
            pass
    return temp

def main():
    case = int(input())
    a = sys.stdin.readline().split()
    num = list(map(int, a))
    print(get_min(case, num), get_max(case, num))
    
main()
