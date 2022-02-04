# 분수찾기
# https://www.acmicpc.net/problem/1193

def find_fraction(x: int) -> str:
    remain = 1
    groupnum = 1

    while True:
        if x > groupnum:
            x -= groupnum
            groupnum += 1
            remain = x
        else:
            if groupnum == 1:
                return '1/1'
            elif groupnum % 2 == 0:
                son = remain
                mother = groupnum + 1 - son
                return f'{son}/{mother}'
            elif groupnum % 2 == 1:
                mother = remain
                son = groupnum + 1 - mother
                return f'{son}/{mother}'
        
        
def main():
    x = int(input())
    print(find_fraction(x))

main()
