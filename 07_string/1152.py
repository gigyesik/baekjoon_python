# 단어의 개수
# https://www.acmicpc.net/problem/1152

import sys

def numofwords(word: str) -> int:
    return len(word)

def main():
    word = sys.stdin.readline().split()
    print(numofwords(word))

main()