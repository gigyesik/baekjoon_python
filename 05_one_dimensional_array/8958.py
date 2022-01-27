# OX 퀴즈
# https://www.acmicpc.net/problem/8958


scorelist = []
def score(case: int) -> list:
    arr = [None] * case

    for i in range(case):
        arr[i] = input()

    for i in range(case):
        counter = 0
        add = 1
        for j in range(len(arr[i])):
            if arr[i][j] == 'O':
                counter += add
                add += 1
            else:
                add = 1
        scorelist.append(counter)
    return scorelist


def main():
    case = int(input())
    result = score(case)
    for i in range(case):
        print(result[i])

main()