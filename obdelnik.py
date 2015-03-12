#!/usr/bin/env python
# -*- coding: utf8 -*-
# Licence: GNU/GPL
# Úloha:   harmonické složky obdelníkového časového průběhu
##############################################################################
from __future__ import division, print_function, unicode_literals

import pylab as lab
from pylab import pi


Um = 1
f = 1
DCL = 0.5
N = lab.arange(0, 10)
U = 2.*Um*DCL*lab.sinc(N*DCL)
U[0] = U[0]/2

t = lab.linspace(0, 2, 300)

lab.figure(1)
u = lab.zeros(len(t))
for n in N:
    un = U[n] * lab.cos(2*pi*n*f*t)
    u += un
    lab.plot(t, un, '--')
lab.plot(t, u, 'r-', lw=3)
lab.grid(True)
lab.show()
