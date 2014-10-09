#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  trojuhelnik.py
# Datum:   09.10.2014 10:23
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Popis:   Trojúhelníkový fraktál
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

import turtle as t


def troj(delka=100, n=2):
    if n >= 3:
        troj(delka / 3, n - 1)
    else:
        t.forward(delka)
    t.left(60)
    if n >= 2:
        troj(delka / 3, n - 1)
    else:
        t.forward(delka)
    t.right(120)
    if n >= 2:
        troj(delka / 3, n - 1)
    else:
        t.forward(delka)
    t.left(60)
    if n >= 3:
        troj(delka / 3, n - 1)
    else:
        t.forward(delka)


def vlocka(velikost=100, pstran=6, rev=False):
    for _ in range(pstran):
        troj(velikost / 3, 3)
        if rev:
            t.left( 360 / pstran )
        else:
            t.right( 360 / pstran )

t.up()
t.goto(-200, 0)
t.down()
"""troj(200, 4)"""
vlocka(rev=0)
vlocka(rev=1)
t.exitonclick()
