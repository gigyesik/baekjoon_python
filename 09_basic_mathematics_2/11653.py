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

def factorization(n: int) -> list:
    result = []
    if prime(n) == True:
        result.append(n)
        return result
    else:
        temp = 2
        while prime(n) == False:
            if prime(temp) == True and n % temp == 0:
                result.append(temp)
                n = n // temp
            else:
                temp += 1
        if prime(n) == True:
            result.append(n)
    return result

def main():
    n = int(input())
    result = factorization(n)
    if result != None:
        for i in range(len(result)):
            print(result[i])

main()

# TimeOut
