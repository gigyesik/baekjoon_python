# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

from copy import deepcopy

def president(k: int, n: int) -> int:
    person = list(range(1, n+1))
    floor = 0
    
    while k > floor:
        floor += 1
        underfloor = deepcopy(person)
        for i in range(len(person)):
            person[i] = sum(underfloor[:i + 1])
    return person[n - 1]

def main():
    case = int(input())
    for _ in range(case):
        k = int(input())
        n = int(input())
        print(president(k, n))

main()