#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def br_check(N, a=1, res=[]):
    if N <= 0 or a == N:
        return res
    elif N != 0:
        b = N - a
        res.append((a, b))
    return br_check(N, a + 1, res)


if __name__ == '__main__':
    print((br_check(int(input('Введите N-ое число: ')))))
