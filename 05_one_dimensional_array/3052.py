# 나머지
# https://www.acmicpc.net/problem/3052

num = [None] * 10
rmainder = [None] * 10
counter = 0

for i in range(10):
    num[i] = int(input())
    rmainder[i] = num[i] % 42
    
print(len(set(rmainder)))