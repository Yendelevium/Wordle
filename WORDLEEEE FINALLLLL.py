Count={}
print("Welcome to WORDLE")
print("Your challenge is to guess a 5 letter word within 5 tries, using hints provided as you progress through the game ")
def inputz():
    X=input("Enter your Guess").upper()
    if len(X)==5:
        return X
    else:
        print("Enter a 5 letter word")
        return inputz()

def wrdcount(Inp):
    global Count
    for i in Inp:
        if i in Count:
            Count[i][0]+=1
        else:
            Count[i]=[1,1]
Wrd="PIANO" #The word to be guessed
for x in range(0,5):
    Inp=inputz()#user input
    wrdcount(Inp)
    for i in range(0,5):
        Let=Inp[i]
        if Count[Let][0]<=Wrd.count(Let): #If the letter occurs and equal no.of times, checks for THAT LETTER
            if Let==Wrd[i]:
                print("CORRECT LETTER:",Let)
            elif Inp[i] in Wrd and Inp[i]!=Wrd[i]:
                print("CORRECT LETTER, WRONG PLACE:",Let)

        elif Count[Let][0]>Wrd.count(Let) and Let in Wrd:#And part to prevent wrong repeating letters to re iterarte
            if Inp.index(Let)>=Wrd.index(Let):
                if Inp.index(Let)==Wrd.index(Let):
                    Inpp=[]
                    for j in range(0,5):
                        if Inp[j]==Let and Inp[j]==Wrd[j]:
                            Inpp.append(j)
                    if Let==Wrd[i] and Count[Let][1]<=Wrd.count(Let):
                        print("CORRECT LETTER:",Let)
                    elif Inp[i] in Wrd and Inp[i]!=Wrd[i] and Count[Let][1]<=(Wrd.count(Let)-len(Inpp)) :
                        print("CORRECT LETTER, WRONG PLACE:",Let)
                        Count[Let][1]+=1
                    elif Let==Wrd[i]:
                        print("CORRECT LETTER:",Let)
                    else:
                        print("WRONG LETTER",Let)
                else:
                    Inpp=[]
                    for j in range(0,5):
                        if Inp[j]==Let and Inp[j]==Wrd[j]:
                            Inpp.append(j)
                    if Let==Wrd[i] and Count[Let][1]<=Wrd.count(Let):
                        print("CORRECT LETTER:",Let)
                        Count[Let][1]+=1
                    elif Inp[i] in Wrd and Inp[i]!=Wrd[i] and Count[Let][1]<=(Wrd.count(Let)-len(Inpp)) :
                        print("CORRECT LETTER, WRONG PLACE:",Let)
                        Count[Let][1]+=1
                    elif Let==Wrd[i]:
                        print("CORRECT LETTER:",Let)
                    else:
                        print("WRONG LETTER",Let)
            if Inp.index(Let)<Wrd.index(Let):#??????
                In=[]
                Inpp=[]
                Result=[]
                for j in range(0,5):
                    if Inp[j]==Let and Inp[j]==Wrd[j]:
                        In.append(j)
                        Result.append("R")
                    elif Inp[j]==Let and Inp[j] in Wrd[j]:
                        In.append(j)
                        Result.append("WR")
                if Result.count('R')==Wrd.count(Let):
                    if Let==Wrd[i]:
                        print("CORRECT LETTER",Let)
                    else:
                        print("WRONG LETTER",Let)
                elif Result.count('R')==1 and Wrd.count(Let)==1: #As Wrd.count(Let)-len(Inpp) becomes 0 if R=1
                    if Let!=Wrd[i]:
                        print("WRONG LETTER",Let)
                        Count[Let][1]+=1
                    else:
                        print("CORRECT LETTER",Let)
                        Count[Let][1]+=1
                elif Result.count('R')<Wrd.count(Let) and Count[Let][1]<=Wrd.count(Let):
                    for j in In:
                        if Inp[j]==Wrd[j]:
                            Inpp.append(j)
                    if  i in Inpp:
                        print("CORRECT LETTER",Let)
                        Count[Let][1]+=1
                    elif Count[Let][1]<=Wrd.count(Let):
                        if Count[Let][1]<=(Wrd.count(Let)-len(Inpp)):
                            print("CORRECT LETTER, WRONG PLACE:",Let)
                            Count[Let][1]+=1
                        else:
                            print("WRONG LETTER:",Let)
                else:
                    print("WRONG LETTER:",Let)
        else: #if letter doesnt occur in Word(repeating or not)
                print("WRONG LETTER:",Let)
    if Inp==Wrd:
        print("YOU WON")
        break
else:
    print("The word was",Wrd)
    print("Better Luck Next Time")






