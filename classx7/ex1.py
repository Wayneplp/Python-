# -*- coding: utf-8 -*-
import itchat
itchat.auto_login(True)
MessText=[u"高博","彭家琛"]
firstusers=[]
for name in (MessText):
	users = itchat.search_friends(name=name,
		userName = None,
		remarkName = None,
		nickName = None)
	
	firstusers.append(users)
# print users
# print firstusers
newuser=[]
for users in (firstusers):
	for user in users:
		userName = (user["UserName"])
		newuser.append(userName)

# print userName

for guy in (newuser):
	itchat.send(u"内容",toUserName = guy)