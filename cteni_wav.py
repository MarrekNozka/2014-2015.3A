#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  cteni_wav.py
# Datum:   05.02.2015 11:03
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   čtení hlavičky souboru WAV
############################################################################
from __future__ import division, print_function, unicode_literals

import struct
############################################################################
# WAV formát
# http://www.fi.muni.cz/~qruzicka/Duffek/wav.html

f = open('left.wav', 'r')

f.read(8)
wID = f.read(4)
fID = f.read(4)

fLen = f.read(4)
wFormatTag = f.read(2)
nChannels = f.read(2)
nSamplesPerSec = f.read(4)
nAvgBytesPerSec = f.read(4)
nBitsPerSample = f.read(2)
# dohromady by to šlo udělat i jedním read()
dohromady = b''.join((fLen, wFormatTag, nChannels, nSamplesPerSec,
                     nAvgBytesPerSec, nBitsPerSample))
abych_to_videl = struct.unpack('IHHIIH', dohromady)

print(wID)
print(fID)
print(repr(fLen))
print(repr(wFormatTag))
print(repr(nChannels))
print(repr(nSamplesPerSec))
print(repr(nAvgBytesPerSec))
print(repr(nBitsPerSample))
f.read(2)
print(f.read(4))

print(abych_to_videl)

