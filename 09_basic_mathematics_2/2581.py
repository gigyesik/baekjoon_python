# 소수
# https://www.acmicpc.net/problem/2581

def prime(numlist: list) -> list:
    m = numlist[0]
    n = numlist[1]
    result = []

    for i in range(m, n + 1):
        if i == 1:
            pass
        elif i == 2:
            result.append(2)
        else:
            temp = 0
            for j in range(2, i):
                if i % j == 0:
                    temp = 0
                    break
                else:
                    temp += 1
            if temp != 0:
                result.append(i)
    if len(result) == 0:
        return [-1, None]
    else:
        return [sum(result), result[0]]


def main():
    m = int(input())
    n = int(input())
    numlist = [m, n]
    result = prime(numlist)
    print(result[0])
    if result[1] != None:
        print(result[1])

main()