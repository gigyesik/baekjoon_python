# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

import sys

def afteraverage(list: list) -> float:
    average = sum(list[1:]) / (int(list[0]))
    counter = 0
    for i in range(1, len(list)):
        if list[i] > average:
            counter += 1
        else:
            pass
    result = ((counter / (int(list[0]))) * 100)
    return result


def main():
    case = int(input())
    for _ in range(case):
        score = sys.stdin.readline().split()
        intscore = list(map(int, score))
        print(f'{afteraverage(intscore):.3f}%')

main()