#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/evil.html

import Image, ImageDraw, sys

info=open("tmp/evil2.gfx").read()
[open("12_f%d.dat" %i, "w").write(info[i::5]) for i in range(5)]
