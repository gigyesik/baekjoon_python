# 한수
# https://www.acmicpc.net/problem/1065

"""
def hansoo(n: int) -> list:
    result = [True] * n
    seperatern = list(map(int, str(n)))
    for i in range(1, n + 1):
        if i >= 100:
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
"""
# fail code
