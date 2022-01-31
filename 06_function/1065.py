# 한수
# https://www.acmicpc.net/problem/1065

def hansoo(n: int) -> list:
    result = [True] * n

    for i in range(100, n + 1):
        seperatern = list(map(int, str(i)))
        if seperatern[0] + seperatern[2] != 2 * seperatern[1]:
            result[i - 1] = False  
    return result

def main():
    n = int(input())
    result = hansoo(n)
    counter = 0
    for i in range(n):
        if result[i]:
            counter += 1
    print(counter)
    

main()
