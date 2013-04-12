#!/usr/bin/env python

import Image, ImageDraw, sys

info=open("tmp/evil2.gfx").read()
[open("12_f%d.dat" %i, "w").write(info[i::5]) for i in range(5)]
