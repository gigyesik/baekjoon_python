# 소인수분해
# https://www.acmicpc.net/problem/11653

def underprime(n: int) -> list:
    prime = [None] * n
    counter = 0

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
    
    if None in prime:
        indexnone = prime.index(None)
        return(prime[:indexnone])
    else:
        return prime

def factorization(n: int) -> list:
    result = []
    temp = underprime(n)
    lastvalue = underprime(n)[-1]
    if n == lastvalue:
        result.append(n)
        return result
    else:
        while n != 1:
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

# TimeOut
