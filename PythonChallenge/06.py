#!/usr/bin/env python

# channel.jpg is a picture of a zip, and the comments of the challenge page
# include the comment <!-- <-- zip -->. We can download channel.zip from the
# site. Unzipped, we get a lot of text files, with another bunch of nothings.

import zipfile
history = []

def openfile(val):
  with open(str(val) + '.txt') as f:
		resp = f.read()
		if 'Next nothing is ' in resp:
			resp = resp.replace('Next nothing is ','')
			history.append(resp)
			return resp
		else:
			print resp
			return -1
	f.close()

val = 90052

while openfile(val) != -1:
	val = openfile(val)

file = zipfile.ZipFile("channel.zip", "r")
ans = ''
for item in history:
	ans = ans + file.getinfo(item+'.txt').comment

print ans

# Going to hockey.html just gives us the message 'it's in the air. look at the
# letters.' In this case, the letters used to spell hockey were 'oxygen'
