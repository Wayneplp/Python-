import random
keepGoing=True
pythonChoice=random.randint(1,100)
while keepGoing:
    myguess=input("Please give me a number")
    if myguess>pythonChoice:
        print("Too large")
    elif myguess<pythonChoice:
        print("Too small")
    else:
        keepGoing=False
        print("Right")
        
            
