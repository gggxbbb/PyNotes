c = 100

from random import choice
gList = ['石头','剪刀','布']

w_a = 0
w_b = 0


def win(a,b):
    if a == b:
        return 0
    elif a == '石头':
        if b == '剪刀':
            return 1
        elif b == '布':
            return 2
        else:
            return
    elif a == '剪刀':
        if b == '石头':
            return 2
        elif b == '布':
            return 1
        else:
            return
    elif a == '布':
        if b == '石头':
            return 1
        elif b == '剪刀':
            return 2
        else:
            return
    else:
        return 

for _ in range(c):
    a = choice(gList)
    b = choice(gList)
    print(f'A:{a} B:{b}',end=' ')
    w = win(a,b)
    if w == 1:
        print('A胜')
        w_a += 1
    elif w == 2:
        print('B胜')
        w_b += 1
    else:
        print('平局')


print(f'共{c}局')
print(f'A胜{w_a}局, 胜率{"%0.5f"%(w_a/c)}')
print(f'B胜{w_b}局, 胜率{"%0.5f"%(w_b/c)}')
