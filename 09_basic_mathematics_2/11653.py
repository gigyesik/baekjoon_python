# 소인수분해
# https://www.acmicpc.net/problem/11653

def factorization(n: int) -> list:
    result = []
    current = n
    prime = 3

    if current == 1:
        return [None]
    else:
        while current != 1:
            if current % 2 == 0:
                result.append(2)
                current = current // 2
            else:
                if current % prime == 0:
                    result.append(prime)
                    current = current // prime
                else:
                    prime += 2
                    if prime > current:
                        result.append(current)
                        return result
    return result


def main():
    n = int(input())
    result = factorization(n)
    if result == [None]:
        pass
    else:
        for i in range(len(result)):
            print(result[i])

main()
