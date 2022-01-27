# 숫자의 개수
# https://www.acmicpc.net/problem/2577

num = [None] * 3
multi = 1
for i in range(3):
    num[i] = int(input())
    multi *= num[i]

result = str(multi)
for i in range(10):
    print(result.count(str(i)))