#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  kladna_a_zaporna.py
# Datum:   23.10.2014 11:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Je dána posloupnost celých čísel. Přerovnejte čísla tak, aby na
#          začátku posloupnosti byla všechna záporná čísla v původním pořadí
#          a za nimi všechna nezáporná čísla v opačném pořadí. Upravenou
#          posloupnost vypište.
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

radek = raw_input("zadej cisla > ")
radek = radek.split()

nezaporna = []
zaporna = []
for i in radek:
    i = int(i)
    if i >= 0:
        nezaporna.append(i)
    else:
        zaporna.append(i)

zaporna.reverse()
hotovo = nezaporna + zaporna
print(hotovo)
