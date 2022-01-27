# 평균
# https://www.acmicpc.net/problem/1546

import sys

subject = int(input())
arr = [None] * subject
prescore = sys.stdin.readline().split()
score = list(map(int, prescore))

for i in range(subject):
    arr[i] = int(score[i])
    arr[i] = (arr[i] / max(score)) * 100

print(sum(arr) / subject)