import random
keydict={}
def encrypt(*message):
    global keydict
    elist = []
    for item in message:
        letterlist = list (item)
        encryptlist = []
        keylist = []
        print letterlist
        for i in range(len(letterlist)):
            key=random.randint(1,6)
            #key=random.randint(1,6)
            keylist.append(key)
            acsNum = ord(letterlist[i])
            acsNum = acsNum + key
            encryptlist.append(chr(acsNum))
        encryptmessage = ''.join(encryptlist)
        keydict[encryptmessage]=keylist
        elist.append(encryptmessage)
    return elist

x = encrypt('abc','acc')
print x
        
