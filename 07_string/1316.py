# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

def checker(word: str) -> bool:
    if len(word) < 3:
        return True
    else:
        for i in range(1, len(word)- 1):
            before = word[:i]
            middle = word[i]
            after = word[i:]
            if middle not in before:
                for j in range(len(before)):
                    if before[j] in after:
                        return False
        return True

def main():
    case = int(input())
    counter = 0
    for _ in range(case):
        word = input()
        if checker(word) == True:
            counter += 1
    print(counter)

main()