#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  prvocisla.py
# Datum:   16.10.2014 09:59
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Provočísla
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators


def jeToProvocislo(cislo):
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False  # ukončí funkci s danou návratovou hodnotou
    return True

# vypíšu všechna prvočísla menší než 1000
for i in range(2, 1000):
    if jeToProvocislo(i):
        print(i, end=' ')
print()

# vypíšu prvních 1000 prvočísel
i = 2
pocet = 0
while pocet < 1000:
    if jeToProvocislo(i):
        print(i, end=' ')
        pocet = pocet + 1
    i = i + 1
print()


############################################################################
# načtu vstup, cislo je řetězec
cislo = raw_input("Zadej celé číslo > ")
# převedu řetězec na číslo
cislo = int(cislo)

AnoNe = True
# zjišťuji jestli je cislo prvočíslo
for i in range(2, cislo // 2):
    if cislo % i == 0:
        AnoNe = False
        break   # když najdu prvního dělitele vyskočím z cyklu ven
if AnoNe:
    print("Hurá, hurá", cislo, "je prvočíslo")
else:
    print(cislo, "není prvočíslo")

# ještě jedno trochu jinak
for i in range(2, cislo // 2):
    if cislo % i == 0:
        print(cislo, "není prvočíslo")
        exit()  # ukončení programu
print("Hurá, hurá", cislo, "je prvočíslo")
