# 숫자의 합
# https://www.acmicpc.net/problem/11720

def sumn(n: int) -> int:
    seperaten = list(map(int, str(n)))
    result = 0
    for i in range(len(seperaten)):
        result += seperaten[i]
    return result

def main():
    n1 = int(input())
    n2 = int(input())
    print(sumn(n2))

main()