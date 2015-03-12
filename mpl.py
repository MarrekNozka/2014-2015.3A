#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  mpl.py
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   výkon střídavého proudu
##############################################################################
from __future__ import division, print_function, unicode_literals

import pylab as lab
from pylab import pi

f = 50
T = 1/f
fi = lab.deg2rad(int(raw_input("zadej fázový posuv > ")))

t = lab.linspace(0, 1.8 * T, 300)
u = 1.5 * lab.sin(2*pi*f*t)
i = 1.2 * lab.sin(2*pi*f*t + fi)

lab.figure(1)
lab.plot(t, u, label='napětí')
lab.plot(t, i, label='proud')
lab.plot(t, u*i, label='výkon')
lab.grid(True)
lab.xlim(min(t), max(t))
lab.legend()

lab.show()
