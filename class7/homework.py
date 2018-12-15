num=['M','T','W','F','S']
letter = raw_input("please input the firet letter.Please give me a capital letter")
letter = letter.upper()
if letter == "S":
    print("please input the second letter.Please give me a lowercase")
    letter = raw_input()
    letter = letter.lower
    if letter == "a":
        print ("Saturday")
    elif letter == "u":
        print ("Sunday")
    else:
        print('date error')
elif letter =="M":
    print ('Monday')
elif letter =='W':
    print ('Wednesday')
elif letter =="F":
    print ('Friday')
elif letter == 'T':
    print("please input the second letter.Please give me a lowercase")
    letter = raw_input()
    
    if letter == "u":
        print ('Tuesday')
    elif letter =='h':
        print ('Thursday')
    else:
        print ('data error')

elif letter not in num:
    print ('Are you kidding me ?')
        
        




          
