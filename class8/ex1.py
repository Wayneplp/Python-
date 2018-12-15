import random

ROCK=1
PAPER=2
SCISSOR=3

hasWon = False
print "Game: ROCK-PAPER-SCISSORS"

while hasWon == False:
    print "Please enter your choice with all capital letters"
    choice = input()
    

    cump =random.randint(1,3)
    print cump
    if (choice - cump) == 0:
        print "tie"
    elif (choice - cump) == -1 or (choice - cump) == 2:
            print " Losing. Please enter your choice with all capital letters again"
    else:
        hasWon == True
        print"Wining."
    
        
    
       
    
