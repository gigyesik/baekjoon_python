# 최댓값 
# https://www.acmicpc.net/problem/2562

num = [None] * 9

for i in range(9):
    num[i] = int(input())

print(max(num))
print(num.index(max(num)) + 1)