# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

def searching(n: str) -> int:
    alpha = []
    for i in range(97, 123):
        alpha.append(chr(i))
    for j in alpha:
        if j in n:
            print(n.index(j), end=' ')
        else:
            print('-1', end=' ')

def main():
    n = input()
    searching(n)

main()