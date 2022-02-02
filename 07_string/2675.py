# 문자열 반복
# https://www.acmicpc.net/problem/2675

from typing import Any
import sys

def repeat(s: Any) -> list:
    s = sys.stdin.readline().split()
    r = s[0]
    p = [None] * len(s[1])
    for i in range(len(p)):
        p[i] = s[1][i] * int(r)
    return p
    
def main():
    case = int(input())
    for _ in range(case):
        p = repeat(_)
        for i in range(1, len(p)):
            p[0] += p[i]
        print(p[0])
main()