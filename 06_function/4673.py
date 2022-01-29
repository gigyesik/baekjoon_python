# 셀프 넘버
# https://www.acmicpc.net/problem/4673

def d(n: int) -> int:
    strn = str(n)
    for i in strn:
        n += int(i)
    return n

def selfnum(n: int) -> list:
    numlist = list(range(1, n+1))
    counter = 0
    choiceremove = numlist[counter]
    lengthnum = len(numlist)

    while counter < lengthnum:
        choiceremove = numlist[counter]
        while d(choiceremove) <= n :
            if d(choiceremove) not in numlist:
                pass
            else:
                numlist.remove(d(choiceremove))
            choiceremove = d(choiceremove)
        lengthnum = len(numlist)
        counter += 1

    return numlist
    


def main(n):
    for i in range(len(selfnum(n))):
        print(selfnum(n)[i])

main(10000)
