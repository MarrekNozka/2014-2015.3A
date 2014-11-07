#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  platidla.py
# Datum:   06.11.2014 11:03
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

platidla = [1, 2, 5]

while platidla[-1] < 5000:
    platidla.append( platidla[-3] * 10 )
platidla.reverse()

castka = raw_input('zadej částku > ')
castka = int(castka)

for bankovka in platidla:
    if castka // bankovka == 0:
        continue
    else:
        print(castka // bankovka, 'x', bankovka)
        castka = castka % bankovka
