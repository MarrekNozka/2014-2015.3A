#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  soubory.py
# Datum:   05.02.2015 10:03
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Práce se soubory
############################################################################
from __future__ import division, print_function, unicode_literals
import os


f = open('soubor.txt', 'w')

f.write('ahoj')
f.write(' nazdar\n')
f.write('cau\n')

raw_input('1. stiskni enter')
f.flush()

raw_input('2. stiskni enter')
f.write('haloooo\n')
f.writelines(['Karel\n', "Bob\n", 'Bobek\n', 'Nijak\n'])

f.close()
############################################################
print('######################################')
f = open('soubor.txt', 'r')
byte = f.read(1)
print(byte)
byte = f.read(1)
print(byte)

radek = f.readline()
print(radek)

# čtu zanak po znaku
while True:
    znak = f.read(1)
    if znak == '':
        break
    print(znak.upper(), end=':')

cely = f.read()
print(cely)
f.close()

############################################################
print('######################################')
f = open('soubor.txt', 'r+')

neco = f.read(3)
print(neco)
print(f.tell())
f.write('TADY')
print(f.tell())
f.seek(14)
f.write('14')

# o 4 znky dál
f.seek(4, os.SEEK_CUR)
f.write('RELATIVNE')

#  jdu na konec souboru
f.seek(0, os.SEEK_END)
f.write('\nKonec')

f.write('\x0d')
f.write('\x0d')
f.write('\x0d')
f.write('neco')


f.close()
