#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def br_check(N, a=1):
    if N <= 0 or a == N:
        return False
    elif N != 0:
        b = N - a
        if b == a:
            print(b, "+", a, "==", N)
            return True
        elif b < a:
            return True
        else:
            print(b, "+", a, "==", N)
            return br_check(N, a + 1)
    else:
        return True


if __name__ == '__main__':
    if br_check(int(input('Введите N-ое число: '))):
        print('Вывели все возможные пары чисел')
    else:
        print('Нужно ввести натруальные числа, кроме 1!')
