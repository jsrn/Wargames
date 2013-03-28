#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/oxygen.html
# For this challenge, we have an image with a greyscale barcode looking thing
# across it. The file is 629x95

import Image

im = Image.open("tmp/oxygen.png")

pix = im.load()

ans = ''
for i in range(1,608,7):
  ans = ans + chr(pix[i,47][0])

print ans
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

ans = ''
for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
	ans = ans + chr(i)

print ans
#integrity
