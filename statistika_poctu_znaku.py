#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  statistika_poctu_znaku.py
# Datum:   15.01.2015 10:28
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Vypíše na výstup počet použití jednotlivých znaků
#          načtených ze vstupu
############################################################################
from __future__ import division, print_function, unicode_literals

############################################################################
pocet = {}
while True:
    try:
        radek = raw_input()
        for znak in radek.upper():
            if znak.isalpha():
                if znak in pocet:
                    pocet[znak] += 1
                else:
                    pocet[znak] = 1
    except EOFError:
        m = max(pocet.values())
        for znak, pocet in pocet.items():
            print("{:>2s}: {:6d} |{:s}".format(znak, pocet,
                                               '#' * int(60*pocet/m)))
        exit(0)
    except KeyboardInterrupt:
        exit(1)
