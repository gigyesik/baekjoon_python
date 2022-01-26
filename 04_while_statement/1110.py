# 더하기 사이클

import sys

def pluscycle(n: str) -> int:
    count = 1
    if int(n) >= 10:
        dec = str(n)[0]
        mon = str(n)[1]
        mid = int(mon) * 10 + (int(dec) + int(mon)) % 10
    else:
        dec = 0
        mon = str(n)[0]
        mid = int(mon) * 10 + (int(dec) + int(mon)) % 10
    
    
    while mid != int(n):
        if mid >= 10:
            dec = str(mid)[0]
            mon = str(mid)[1]
            mid = int(mon) * 10 + (int(dec) + int(mon)) % 10
            count += 1
        else:        
            dec = 0
            mon = str(mid)[0]
            mid = int(mon) * 10 + (int(dec) + int(mon)) % 10
            count += 1
    return count

        

def main():
    a = int(input())
    print(pluscycle(a))

main()