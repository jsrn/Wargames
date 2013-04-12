#!/usr/bin/env python
# <!-- remember: 100*100 = (100+99+99+98) + (...  -->

import Image, ImageDraw, sys

imorig = Image.open('tmp/wire.png')
imnew =  Image.new('RGBA', (100, 100), (0, 0, 0, 255))
draw = ImageDraw.Draw(imnew)

pix = imorig.load()

directions = [(1,0), (0,1), (-1,0), (0,-1)]
x,y,count = 0,0,0
maxSteps = 200

for s in range(maxSteps):
  for d in directions:
		steps = maxSteps / 2
		for s in range(steps):
			x,y = x+d[0],y+d[1]
			draw.point((x, y), fill=(pix[count,0][0],pix[count,0][1],pix[count,0][2]))
			count += 1
		maxSteps = maxSteps - 1

imnew.save('tmp/new.png', "PNG")
