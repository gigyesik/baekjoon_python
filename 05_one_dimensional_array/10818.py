# 최소, 최대
# https://www.acmicpc.net/problem/10818

import sys

def get_min(length: int, num: list) -> int:
    temp = num[0]
    for j in range(1, length):
        if num[j] <= temp:
            temp = num[j]
        else:
            pass
    return temp

def get_max(length: int, num: list) -> int:
    temp = num[0]
    for j in range(1, length):
        if num[j] >= temp:
            temp = num[j]
        else:
            pass
    return temp

def main():
    length = int(input())
    numin = sys.stdin.readline().split()
    num = list(map(int, numin))
    print(get_min(length, num), get_max(length, num))
    
main()
