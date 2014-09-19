#!/usr/bin/python
# -*- coding: utf8 -*-
############################################################################

from __future__ import division
from __future__ import print_function

vek = input("Kolik ti je? > ")

if vek < 6:
    print('Ti jsi ještě předškolák.')
    a = 10 * 59
    print('Ti jsi ještě předškolák.')
elif vek == 6:
    print('Hurá jdeš do školy.')
elif vek <= 17:
    print('Ještě prisim tě poslouchej maminku.')
elif vek > 18 and vek < 65:
    print('Makej, makej, makej.')
else:
    print('Jsi fakt starej.')
print("konec")
