import random
def encrypt(*message): 
    keydict={}
    elist = []
    for item in message:
        letterList = list (item)
        encryptList = []
        keylist = []
        for i in range(len(letterList)):
            key=random.randint(1,6) 
            keylist.append(str(key))
            acsNum = ord(letterList[i])
            acsNum = acsNum + key
            encryptList.append(chr(acsNum))  
        encryptMessage = "".join(encryptList)
        
        keydict[encryptMessage]="".join(keylist) 
        
        elist.append(encryptMessage)
    
    FILENAME = "1.txt"
    file = open(FILENAME,"a")
    for item in keydict.keys():
        file.write(item+":"+keydict[item]+"\n")
    file.close()
    return elist



# def decode(elist):
#     keydict = {}
#     dlist = []
#     FILENAME ="1.txt" 
#     file = open (FILENAME,"r")
#     a = file.readlines() 
#     file.close()
#     keylist=[]
#     for item in a:
#         keylist.append(item.strip().split(":"))
#     for item in keylist:
#         keydict[item[0]]=item[1]      
#     for item in elist:
#         itemList = list (item)
#         decodeList=[]
#         key = keydict[item]
        
#         for x in range(len(itemList)):
#              acsNum = ord(itemList[x])
#              acsNum = acsNum - int(key[x])
#              decodeList.append(chr(acsNum))
#         decodeMessage = "".join(decodeList)
#         dlist.append(decodeMessage)
#     return(dlist)


m = encrypt("abc","123","opp","lol" )
print m 
#u=decode(m)
