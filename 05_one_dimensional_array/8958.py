# OX 퀴즈
# https://www.acmicpc.net/problem/8958

def get_score(inox: str) -> int:

    counter = 0
    add = 1
    for i in range(len(inox)):
        if inox[i] == 'O':
            counter += add
            add += 1
        else:
            add = 1
    return counter

def main():
    case = int(input())
    inox = [None] * case
    for i in range(case):
        inox[i] = input()
    for i in range(case):
        print(get_score((inox)[i]))

main()
