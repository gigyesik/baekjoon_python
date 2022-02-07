# 소수 구하기 (에라토스테네스의 체)
# https://www.acmicpc.net/problem/1929

import sys

def eratos(n: int) -> list:
    prime = [None] * n
    counter = 0
    if n == 1:
        return []
    elif n == 2:
        return [2]
    prime[counter] = 2
    counter += 1
    prime[counter] = 3
    counter += 1

    for i in range(5, n + 1, 2):
        j = 1
        while prime[j] ** 2 <= i:
            if i % prime[j] == 0:
                break
            j += 1
        else:
            prime[counter] = i
            counter += 1
    
    result = set(prime)
    if None in result:
        result.remove(None)
    result = sorted(result)
    return result

def main():
    mn = sys.stdin.readline().split()
    listmn = list(map(int, mn))
    resultm = eratos(listmn[0])
    resultn = eratos(listmn[1])
    result = set(resultn) - set(resultm) 
    result = sorted(result)
    if resultm == []:
        resultm = []
    elif resultm[-1] == listmn[0]:
        result.append(listmn[0])
    result = sorted(result)
    if len(result) == 0:
        print(listmn[0])
    else:
        for i in range(len(result)):
            print(result[i])

main()