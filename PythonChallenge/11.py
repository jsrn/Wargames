#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/5808.html

import Image, ImageDraw, sys

imorig = Image.open('tmp/cave.jpg')
imeven =  Image.new('RGBA', (640, 480), (0, 0, 0, 255))
imodd =  Image.new('RGBA', (640, 480), (0, 0, 0, 255))
draweven = ImageDraw.Draw(imeven)
drawodd = ImageDraw.Draw(imodd)

pix = imorig.load()

for y in range(480):
  for x in range(640):
		if x % 2 == 0 and y % 2 == 0:
			draweven.point((x, y), fill=(pix[x,y][0],pix[x,y][1],pix[x,y][2]))
		else: 
			drawodd.point((x, y), fill=(pix[x,y][0],pix[x,y][1],pix[x,y][2]))

imeven.save('tmp/even.png', "PNG")
imodd.save('tmp/odd.png', "PNG")

#even.png ends up with the word 'evil' barely visible
