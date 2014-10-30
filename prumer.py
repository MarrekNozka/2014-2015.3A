#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  prumer.py
# Datum:   30.10.2014 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Vypočítá aritmetický průměr
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

import random

'''Pokud zádám jen Enter, čísla se vygenerují náhodně,
jinak se čtou ze vstupu.'''
radek = raw_input('zadej čísla oddělená mezerou > ')

if radek == '':
    cisla = []
    for _ in range(20):
        cisla.append( random.randint(-20, 20) )
    cisla = [ random.randint(-20, 20) for _ in range(20) ]
else:
    cisla = radek.split()   # rozdělím řetězec
    for i, cislo in enumerate(cisla):
        cisla[i] = int(cislo)
    cisla = [ int(i) for i in cisla ]  # převedu řetězce na čísla

print(cisla)

suma = 0
for hodnota in cisla:
    suma = suma + hodnota
print("Průměr:", suma / len(cisla) )

pocet_kladnych = 0
for hodnota in cisla:
    if hodnota > 0:
        pocet_kladnych = pocet_kladnych + 1
print("Počet kladných:", pocet_kladnych)
