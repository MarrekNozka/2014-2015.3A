#!/usr/bin/python
# -*- coding: utf8 -*-
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

seznam = list( range(10, 20) )

for cislo in seznam:
    if cislo % 3 == 0:
        print(cislo, "je dělitelne 3")
    print(cislo)


for cislo in range(100):
    if cislo % 3 == 0:
        print(cislo, "je dělitelne 3")
        print(100 * cislo)
        print(100 * cislo)
    if cislo % 5 == 0:
        print(cislo, "je dělitelne 5")

seznam = [ 2 ** i for i in range(100) if i < 20 ]
print(seznam)

import random
nahoda = [ random.randint(0, 10) for _ in range(10) ]
print(nahoda)

nahoda = []
for i in range(10):
    nahoda.append( random.randint(0, 10) )
