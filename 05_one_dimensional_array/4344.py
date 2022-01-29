# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

import sys

def afteraverage(score: list) -> float:
    n = score[0]
    average = sum(score[1:]) / (int(score[0]))
    counter = 0
    for i in range(1, len(score)):
        if score[i] > average:
            counter += 1
    result = ((counter / ((score[0]))) * 100)
    return result


def main():
    case = int(input())
    for _ in range(case):
        score = sys.stdin.readline().split()
        intscore = list(map(int, score))
        print(f'{afteraverage(intscore):.3f}%')

main()
