# 소인수분해
# https://www.acmicpc.net/problem/11653

def factorization(n: int) -> list:
    result = []
    prime = 3

    if n == 1:
        return [1]
    elif n == 2:
        return [2]
    else:
        while n != 1:
            if n % 2 == 0:
                result.append(2)
                n = n // 2
            else:
                if n % prime == 0:
                    result.append(prime)
                    n = n // prime
                else:
                    prime += 2
    return result


def main():
    n = int(input())
    result = factorization(n)
    for i in range(len(result)):
        print(result[i])

main()

# Fail
