# 상수
# https://www.acmicpc.net/problem/2908

import sys

def sangsoo(nums: str) -> int:
    result = [nums[0][::-1], nums[1][::-1]]
    if int(result[0]) >= int(result[1]):
        return result[0]
    else:
        return result[1]

def main():
    nums = sys.stdin.readline().split()
    print(sangsoo(nums))

main() 