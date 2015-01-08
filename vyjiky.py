#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  vyjiky.py
# Datum:   08.01.2015 10:18
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   podělí čísla na řádku
############################################################################
from __future__ import division, print_function, unicode_literals

############################################################################
while True:
    try:
        line = raw_input('deleni >> ')
        if 'konec' in line.lower():
            exit(0)
        a, b = line.split()
        print(float(a) / float(b))
    except EOFError:
        print("\nKonec")
        exit(0)
    except KeyboardInterrupt:
        print("\nPřerušeno uživatelem")
        exit(1)
    except ValueError:
        print("\nMusíš zadat celé číslo..")
    except ZeroDivisionError:
        print("\nNelze dělit nulou!")
