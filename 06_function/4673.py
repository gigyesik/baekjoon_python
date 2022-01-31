# 셀프 넘버
# https://www.acmicpc.net/problem/4673

def d(n: int) -> int:
    tho = n // 1000
    hun = (n // 100) % 10
    dec = (n // 10) % 10
    mon = n % 10
    result = n + tho + hun + dec + mon
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
