# 분수찾기
# https://www.acmicpc.net/problem/1193

def search_fraction(x: int) -> str:
    counter = 1
    numerator = 1
    denomirator = 1

    while counter != x:
        if numerator == 1 and denomirator % 2 == 1:
            denomirator += 1
            numerator = 1
        elif denomirator == 1 and numerator % 2 == 0:
            numerator += 1
            denomirator = 1
        elif denomirator >= 1 and numerator >= 1 and (denomirator + numerator) % 2 == 1:
            numerator += 1
            denomirator -= 1
        else:
            numerator -= 1
            denomirator += 1
        counter += 1
    return f'{numerator}/{denomirator}'



def main():
    x = int(input())
    print(search_fraction(x))

main

# TimeOut
