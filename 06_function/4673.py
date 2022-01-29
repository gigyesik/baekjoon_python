# 셀프 넘버
# https://www.acmicpc.net/problem/4673

def dn(n: int) -> int:
    strn = str(n)
    for i in strn:
        n += int(i)
    return n

def selfnum(n: int) -> int:
    result = n
    for i in range(n+1):
        if dn(i) == n:
            return
        else:
            result = n
    return result


def main(n):
    for i in range(1, n+1):
        if selfnum(i) == None:
            pass
        else:
            print(selfnum(i))

main(10000)
