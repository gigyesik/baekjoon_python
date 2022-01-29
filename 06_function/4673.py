# 셀프 넘버
# https://www.acmicpc.net/problem/4673

def d(n: int) -> int:
    strn = str(n)
    for i in strn:
        n += int(i)
    return n

def selfnum(n: int) -> list:
    numlist = list(range(1, n+1))
    
    for i in range(1, n+1):
        if d(i) not in numlist:
            pass
        else:
            numlist.remove(d(i))

    return numlist


def main(n):
    for i in range(len(selfnum(n))):
        print(selfnum(n)[i])

main(10000)
