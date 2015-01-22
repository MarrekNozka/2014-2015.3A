#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  reverzni_kalkulator.py
# Datum:   22.01.2015 10:29
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL
# Úloha:
############################################################################
from __future__ import division, print_function, unicode_literals

############################################################################
zasobnik = []


def fce2argumenty(funkce):
    if len(zasobnik) >= 2:
        b = zasobnik.pop()
        a = zasobnik.pop()
        try:
            zasobnik.append(funkce(a, b))
        except Exception as e:
            print('Chyba:', e.__class__)
            print('Chyba:', e.message)
            zasobnik.extend([a, b])
    else:
        print('"' + token + '":',
              'nelze provést, v zásobníku musí být alespoň dvě čísla')


def plus(a, b):
    return a+b


def minus(a, b):
    return a-b

while True:
    try:
        radek = raw_input(str(zasobnik) + ' >> ')
        for token in radek.split():
            try:
                zasobnik.append(float(token))
            except ValueError:
                if token == '+':
                    fce2argumenty(plus)
                elif token == '-':
                    fce2argumenty(minus)
                elif token == '*':
                    fce2argumenty(lambda x, y: x * y)
                elif token == '/':
                    fce2argumenty(lambda x, y: x / y)
    except EOFError:
        exit(0)
    except KeyboardInterrupt:
        exit(1)
