import random
keydict={}
def encrypt(*message): 
    global keydict
    elist = []
    for item in message:
        letterList = list (item)
        encryptList = []
        keylist = []
        print letterList
        for i in range(len(letterList)):
            key=random.randint(1,6) 
            keylist.append(key)
            acsNum = ord(letterList[i])
            acsNum = acsNum + key
            encryptList.append(chr(acsNum))
        encryptMessage = "".join(encryptList)
        keydict[encryptMessage]=keylist
        elist.append(encryptMessage)
    return elist
def decode(elist):
    global keydict
    dlist= []
    for item in elist:
        itemList = list (item)
        decodeList=[]
        key = keydict[item]
        
        for x in range(len(itemList)):
             acsNum = ord(itemList[x])
             acsNum = acsNum - key[x]
             decodeList.append(chr(acsNum))
        decodeMessage = "".join(decodeList)
        dlist.append(decodeMessage)
    return(dlist)


#m=encrypt(raw_input("please input the message to encrypt")m)
m = encrypt("abc","bcd" )
print m 
u=decode(m)
print u

