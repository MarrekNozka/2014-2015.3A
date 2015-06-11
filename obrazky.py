#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  myLMS.py
# Datum:   22.07.2014 15:41
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   adaptivní filter (LMS)
##############################################################################
from __future__ import division, print_function, unicode_literals

import pylab as lab
from random import random
obrazek = lab.imread('samec.png')
obrazek = lab.imread('sachy.png')

print(obrazek[0][0][0])
print(obrazek[0][0][1])
print(type(obrazek[0][0][2]))

novy = []
for radek in obrazek:
    novy_r = []
    for bod in radek:
        # seda = 0.3*bod[0] + 0.59*bod[1] + 0.11*bod[2]
        seda = 0.33*bod[0] + 0.33*bod[1] + 0.33*bod[2]
        if seda > random():
            novy_r.append(0)
        else:
            novy_r.append(1)
    novy.append(novy_r)


lab.imshow(obrazek)
lab.imshow(novy, cmap='binary')
lab.show()
