#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  opp.py
# Datum:   29.01.2015 10:35
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Ukázka OOP
############################################################################
from __future__ import division, print_function, unicode_literals
import math


class Ccislo():
    """můj Datový typ pro komplaxní čísla"""
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __del__(self):
        print('umírám')

    @property
    def arg(self):
        return math.atan(self.im/self.re)

    def __add__(a, b):
        return Ccislo(a.re + b.re, a.im + b.im)

    def __str__(self):
        return "{} + {}j".format(self.re, self.im)


class Ccislo2(Ccislo):
    @property
    def arg(self):
        return math.degrees(math.atan(self.im/self.re))


x = Ccislo2(3, 4)
y = Ccislo(4, 3)
Q = Ccislo(4, 3)
del(Q)
print(x.arg)
print(y.arg)

z = x + y
print(z.re)
print(z.im)
print(z.arg)

print(x)
print(y)
print(z)
