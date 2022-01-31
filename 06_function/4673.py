# 셀프 넘버
# https://www.acmicpc.net/problem/4673

def d(n):
    result = n
    while n > 0:
        res += n % 10
        n //= 10
    return result


def underselfnum(n: int) -> list:
    result = [True] * n
    result[0] = False
    result[1] = True
    for i in range(1, n):
        if d(i) < n:
            result[d(i)] = False 
    return result


def main():
    n = 10000
    result = underselfnum(n)
    for i in range(n):
        if result[i]:
            print(i)

main()
