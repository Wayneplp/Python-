# -*- coding: utf-8 -*-
import requests
import itchat

KEY = "ae8790529ebd4025b10ee1f22abfb19b"

def get_response(msg):
	apiUrl = "http://www.tuling123.com/openapi/api"
	data = {
	     "key":KEY,
	     "info":msg,
	     "userid":"Wayne"
	}
	try:
		r = requests.post(apiUrl,data=data)
		print r
		r=r.json()
		print r
		return r.get("text")
	except:
		return

@itchat.msg_register([itchat.content.SHARING,itchat.content.TEXT])
def tuling_reply(msg):
	 
	defaultReply = u"目前正忙"
	reply = get_response(msg["Text"])
	return reply or defaultReply 

		
itchat.auto_login(hotReload=True)
itchat.run()