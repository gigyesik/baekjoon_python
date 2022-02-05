# 설탕 배달
# https://www.acmicpc.net/problem/2839

def sugar(gram: int) -> int:
    five = 0
    three = 0
    result = 0

    for i in range(0, (gram // 3) + 1):
        three = i
        result = three * 3 + five * 5
        for j in range(0, (gram // 5) + 1):
            five = j
            result = three * 3 + five * 5
            if result == gram:
                return five + three
        if result == gram:
            return five + three
    return -1


def main():
    gram = int(input())
    print(sugar(gram))

main()