#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  zelva.py
# Datum:   02.10.2014 10:02
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

import turtle as t
import math

#   t.speed(0)
t.up()
t.goto(-300, 0)
t.down()


def n_uhelnik(n=5, krok=100):
    if n < 1:
        return
    for _ in range(n):
        t.forward(krok)
        t.left(360 / n)
    return


def sinus(amplituda, perioda):
    deleni = 256   # počet díléčků pro periodu
    pocatekX = t.xcor()
    pocatekY = t.ycor()
    krok = perioda / deleni
    krokUhel = 2 * math.pi / deleni
    for i in range(deleni):
        t.goto(pocatekX + i * krok,
               pocatekY + amplituda * math.sin( i * krokUhel  ) )
############################################################################

n_uhelnik(7)
n_uhelnik(7, 50)
n_uhelnik()
n_uhelnik(krok=200, n=8)
t.exitonclick()
exit(0)




t.goto(50, 50)
sinus(100, 200)


for i in range(4):
    t.forward(100)
    t.left(90)

t.left(45)

i = 0
while i < 4:
    t.forward(100)
    t.left(90)
    i = i + 1


############################################################################
t.exitonclick()
