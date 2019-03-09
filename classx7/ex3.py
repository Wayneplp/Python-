# -*- coding: utf-8 -*-

import os
from os import listdir
import PIL.Image as Image
import itchat
import math
itchat.auto_login(True)

myDir = "head"

os.mkdir(myDir)


num = 0
friends = itchat.get_friends(update=True)
friends = friends[0:25]
for i in friends:
	img = itchat.get_head_img(userName=i["UserName"])
	f=open(myDir+"/"+str(num)+".jpg","wb")
	f.write(img)
	num+=1
	f.close()
pics = listdir(myDir)
print pics
numPic=len(pics)
eachsize=int(math.sqrt(float(640*640)/numPic))
numline = int (800/eachsize)
background = Image.new("RGBA",(640,640))

x= 0
y= 0

for i in pics:
	try:
	    img= Image.open (myDir+"/"+i)
	except IOError:
		print"inbalid Image"
	else:
		img= img.resize((eachsize,eachsize),Image.ANTIALIAS)
		background.paste(img,(x*eachsize,y*eachsize))
		x+=1
		if x== numline:
			y+=1
			x=0
background.save(myDir+".png")


