# 소수 찾기
# https://www.acmicpc.net/problem/1978

import sys

def search_prime(numlist: list) -> int:
    counter = 0
    for i in range(len(numlist)):
        check = numlist[i]
        temp = 0
        if check == 1:
            pass
        else:
            for j in range(2, check):    
                if check % j == 0:
                    break
            else:
                temp += 1
            if temp != 0:
                counter += 1
    return counter

def main():
    case = int(input())
    num = sys.stdin.readline().split()
    numlist = (list(map(int, num)))[:case]
    print(search_prime(numlist))

main()
