def mainnn():
    quit= ""
    while (quit != "YES"):
        empchess = []
        chessboard = board(empchess)
        mainchess = chessboard[0]
        for x in range(8):
            row = mainchess[x]
            print(row)
        sscoree = sscorecheckerr(mainchess)
        print("black currently has a score of {} and white has a score of {}".format(sscoree[0],sscoree[1]))
        userrrchange = uppercase(input("Would you like to move any peices around.Yes or no"))
        if userrrchange=="YES":
            peices = ["k", "q", "b", "n", "r", "p", "K", "Q", "B", "N", "R", "P"]
            x=0
            while x != 1:
                userrrpeice = input("What is the piece you would like to move?")
                if userrrpeice in peices:
                    rowval = 0
                    while rowval!= 1 :
                        userrrrow =  int(input("Which row would you like it to be in ?"))
                        if userrrrow < 9 and userrrrow>=0:
                            rowval = 1
                            columnval = 0
                            while columnval != 1:
                                userrrcolumn = int(input("Which column would you like it to be in ?"))
                                if userrrcolumn < 9 and userrrcolumn>=0:
                                    columnval = 1
                                else:
                                    print("The row you entered is not valid, please try again")
                                    columnval = 0
                        else:
                            print("The row you entered is not valid, please try again")
                            rowval = 0
                    newboard = gamechanger(userrrpeice,userrrrow,userrrcolumn,mainchess)
                    x=1
                else:
                    print("The character you entered is not valid, please try again")
                    x=0

            for x in range(8):
                row = newboard[x]
                print(row)
        quit = uppercase(input("Do you want to start a new board? yes or no"))
        if (quit == "NO"):
            print("It was great meeting you")
            break


def board(mainboard):
    whitepeices = ["k","q","b","n","r","p"]
    blackpeices = ["K","Q","B","N","R","P"]
    empspace = ["-"]
    B = []
    W = []
    E= []
    for u in range(1,9):
        x = 1
        while x !=0:
            userrrinput = (input("type the pieces of your {} row \t".format(u)))
            userrrinputlist = list(userrrinput)
            userrrinputlistlen = len(userrrinputlist)
            if userrrinputlistlen == 8  :
                for i in range(userrrinputlistlen) :
                    letter = userrrinputlist[i]
                    if letter in whitepeices:
                        W.append(letter)
                        x=0
                    elif letter in blackpeices:
                        B.append(letter)
                        x=0
                    elif letter in empspace:
                        E.append(letter)
                        x=0
                    else:
                        x=3
                if x ==3:
                    print("Please confirm you have valid characters")
            else:
                print("Confirm you have inserted eight characters")

        mainboard.append(userrrinputlist)

    return [mainboard,B,E,W]

def sscorecheckerr(anylist):
    b=0
    w=0
    for y in anylist:
        for x in y:
            if x == "P":
                b=b+1

            elif x == "p":
                w=w+1

            elif x == "Q":
                b=b+10

            elif x == "q":
                w=w+10

            elif x == "R":
                b=b+5

            elif x == "r":
                w=w+5
            elif x == "N":
                b=b+3.5

            elif x == "n":
                w=w+3.5

            elif x == "B":
                b=b+3

            elif x=="b":
                w=w+3
    return [b,w]
def gamechanger(insitem,userrrinputrow,userrrinputcolumn,y):
    row = y[userrrinputrow]
    row.pop(userrrinputcolumn)
    row.insert(userrrinputcolumn,insitem)
    return y

def uppercase(charrr):
    charrrlist = list(charrr)
    length = len(charrrlist)
    k= list()
    i = 0
    while i < length:
        check = charrrlist[i]
        acssi_charrr = ord(check)
        i=i+1
        if (acssi_charrr >= 97 and acssi_charrr<=122) :
            newupper = acssi_charrr-32
            newupperchr = chr(newupper)
            k.append(newupperchr)
        else:
            k.append(check)
    Pop = ""
    heck = Pop.join(k)
    return(heck)

mainnn()
