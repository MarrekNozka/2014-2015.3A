#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  kalendar.py
# Datum:   30.10.2014 10:53
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL
# Úloha:   Ascii kalendář
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

import sys
echo = sys.stdout.write

den = tuple(range(1, 32))

'''tato proměnná obsahuje den v týdnu, kterým začíná měsíc'''
prvni = 3  # středa

echo(' ' * 3 * (prvni - 1) )
for i in den:
    echo('{0:2d}'.format(i) )
    if i % (7-prvni+1) == 0:
        echo('\n')
    else:
        echo(' ')
