# 사분면 고르기

a = int(input())
b = int(input())

if a == 0 or b == 0:
    pass
elif a > 0:
    if b > 0:
        print('1')
    else:
        print('4')
elif a < 0:
    if b > 0:
        print('2')
    else:
        print('3')