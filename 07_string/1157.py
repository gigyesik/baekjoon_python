# 단어 공부
# https://www.acmicpc.net/problem/1157

def searching(word: str) -> str:
    alphabet = []
    for i in range(97, 123):
        alphabet.append(chr(i))

    wordlower = word.lower()
    alphacount = [0] * len(alphabet)

    for i in range(len(wordlower)):
        if wordlower[i] in alphabet:
            alphacount[alphabet.index(wordlower[i])] += 1

    resultcount = sorted(alphacount)
    max1 = resultcount[len(resultcount) - 1]
    max2 = resultcount[len(resultcount) - 2]
    
    if max1 == max2:
        return '?'
    else:
        return alphabet[alphacount.index(max(alphacount))].upper()

def main():
    word = input()
    print(searching(word))

main()