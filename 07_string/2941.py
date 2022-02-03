# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

def croatia(word: str) -> int:
    crolist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    result = word
    for i in range(len(crolist)):
        if crolist[i] in result:
            result = result.replace(crolist[i], 'a')
    return len(result)

def main():
    word = input()
    print(croatia(word))

main()