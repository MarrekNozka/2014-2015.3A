#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  myLMS.py
# Datum:   22.07.2014 15:41
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   adaptivní filter (LMS)
##############################################################################
from __future__ import division, print_function, unicode_literals
import random


def zobraz(data):
    for radek in data:
        for x in radek:
            print(x, end='')
        print()


def generuj(pradku=12, psloupcu=12):
    data = []
    for _ in range(pradku):
        radek = []
        for _ in range(psloupcu):
            radek.append(random.randint(0, 1))
        data.append(radek)
    return data

d = generuj(10, 20)

for r in range(len(d)):
    for s in range(len(d[0])):
        if r == 0 or s == 0 or r == len(d)-1 or s == len(d[0])-1:
            d[r][s] = 2


zobraz(d)

# import pylab as lab
# lab.imshow(d, interpolation='none', cmap='binary')
# lab.show()
