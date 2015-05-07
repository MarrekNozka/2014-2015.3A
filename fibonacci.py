#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  fibonacci.py
# Datum:   07.05.2015 10:33
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Fibonacciho posloupnost
############################################################################
from __future__ import division, print_function, unicode_literals


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        i = 2
        x, y = 0, 1
        while i <= n:
            i += 1
            vysledek = x + y
            x, y = y, vysledek
        return vysledek
    else:
        return None


def fibG(n):
    yield 0
    yield 1
    x, y = 0, 1
    i = 2
    while i <= n:
        yield x + y
        x, y = y, x+y
        i += 1
    return


def fibR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibR(n-2) + fibR(n-1)
    else:
        return None


n = 10
print(fib(n))
print(fibR(n))

g = fibG(10)
print(g.next())
print(g.next())
print(g.next())
print(g.next())
print(g.next())

print('-----------------')
for i in fibG(10):
    print(i)
