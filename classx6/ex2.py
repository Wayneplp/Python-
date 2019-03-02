# -*- coding: utf-8 -*-
import requests
import itchat


itchat.login()

friends = itchat.get_friends(update=True)[0:]
male = famle = other = 0
for i in friends[1:]:
	print i 
 	sex = i ["Sex"]
 	if sex ==1:
 		male +=1
 	elif sex ==2:
 		famle +=1
 	else:
 		other +=1

total= len(friends[1:])
man = male/(total*0.1)
woman = famle/(total*0.1)
print man
print woman