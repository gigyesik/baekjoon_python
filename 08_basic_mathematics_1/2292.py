# 벌집
# https://www.acmicpc.net/problem/2292

def honeycomb(n: int) -> int:
    a0 = [1]
    counter = 0
    an = a0
    
    while n not in an:
        counter += 1        
        an = list(range(3*(counter**2) - 3*counter + 2, 
        3*(counter**2) + 3*counter + 2))
    return counter + 1


def main():
    num = int(input())
    print(honeycomb(num))

main()

# TimeOut
