# 정수 N개의 합
# https://www.acmicpc.net/problem/15596

import sys

def solve(a: list) -> int:
    ans = 0
    for i in a:
        ans += i
    return ans
        
"""
def main():
    a = sys.stdin.readline().split()
    list_a = list(map(int, a))
    print(sum(list_a))

main()
"""
