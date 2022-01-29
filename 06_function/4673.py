# 셀프 넘버
# https://www.acmicpc.net/problem/4673

def d(n: int) -> int:
    strn = str(n)
    for i in strn:
        n += int(i)
    return n

def underselfnum(n: int) -> list:
    numset = set(range(1,n+1))
    dnumset = set()

    for i in range(1, len(numset) + 1):
        if d(i) in numset:
            dnumset.add(d(i))
    result = sorted(numset - dnumset)

    return result


def main(n: int):
    result = underselfnum(n)
    for i in range(len(result)):
        print(result[i])

main(10000)
