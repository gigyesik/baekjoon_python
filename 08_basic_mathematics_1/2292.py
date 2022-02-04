# 벌집
# https://www.acmicpc.net/problem/2292

def honeycomb(n: int) -> int:
    a0 = 1
    counter = 1
    an = 3*(counter**2) - 3*counter + 2
    annext = 3*((counter + 1)**2) - 3*(counter + 1) + 2
    
    while True:
        if n == a0:
            return counter
        elif n >= an:
            if n >= annext:
                an = annext
                counter += 1
                annext = 3*((counter + 1)**2) - 3*(counter + 1) + 2
            else:
                return counter + 1


def main():
    num = int(input())
    print(honeycomb(num))

main()
