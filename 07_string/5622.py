# 다이얼
# https://www.acmicpc.net/problem/5622

def dial(word: str) -> int:
    wordlist = [['A','B','C'], ['D','E','F'], ['G','H','I'], 
    ['J','K','L'], ['M','N','O'], ['P','Q','R','S'],
    ['T','U','V'], ['W','X','Y','Z']]
    counter = 0
    for i in range(len(word)):
        for j in range(len(wordlist)):
            if word[i] in wordlist[j]:
                counter += j + 2
    return counter + len(word)

def main():
    word = input()
    print(dial(word))

main()