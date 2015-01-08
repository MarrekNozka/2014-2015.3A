#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  vyjiky.py
# Datum:   08.01.2015 10:18
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   sečte všechny čísla zadaná na řádek
############################################################################
from __future__ import division, print_function, unicode_literals

############################################################################
while True:
    try:
        line = raw_input('suma: zadej čísla oddělená mezerou\n >> ')
        if 'konec' in line.lower():
            exit(0)
        suma = 0
        for i in line.split():
            try:
                suma += float(i)
            except ValueError:
                print("Vynechávám", i, "-- není to číslo")
        print('-->', suma, '\n')
    except EOFError:
        print("\nKonec")
        exit(0)
    except KeyboardInterrupt:
        print("\nPřerušeno uživatelem")
        exit(1)
