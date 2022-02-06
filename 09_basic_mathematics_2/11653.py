# 소인수분해
# https://www.acmicpc.net/problem/11653

def prime(n: int) -> bool:
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        temp = 0
        for i in range(2, n):
            if n % i == 0:
                temp = 0
                break
            else:
                temp += 1
        if temp != 0:
            return True
        else:
            return False

def underprime(n: int) -> list:
    result = []
    for i in range(2, (n+1) // 2):
        if prime(i) == True:
            result.append(i)
    return result

def factorization(n: int) -> list:
    result = []
    if prime(n) == True:
        result.append(n)
        return result
    else:
        temp = underprime(n)
        while prime(n) == False and n != 1:
            for i in temp:
                if n % i == 0:
                    result.append(i)
                    n = n // i
        if n != 1:
            result.append(n)
    return sorted(result)

def main():
    n = int(input())
    result = factorization(n)
    for i in range(len(result)):
        print(result[i])

main()
