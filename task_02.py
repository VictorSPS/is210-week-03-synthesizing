#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
inquisition.SPANISH
y = len(inquisition.SPANISH)
x = inquisition.SPANISH.index('Spanish')
print x
FLEMISH = inquisition.SPANISH[:x] + "Flemish" + inquisition.SPANISH[26:y]
print FLEMISH
