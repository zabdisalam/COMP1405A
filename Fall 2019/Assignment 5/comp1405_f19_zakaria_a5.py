def main():
    fullinput = []
    wordinputs = []
    exportedinput = []
    fullinputstr = ''
    myinput = input("input ur char \n")
    for i in myinput:
        asciimyinput = ''
        if 65 <= ord(i) <= 90:
            asciimyinput = ord(i)
        elif 97 <= ord(i) <= 122:
            asciimyinput = ord(i) - 32
        else:
            asciimyinput = ord(i)
        finalinput = chr(asciimyinput)
        fullinput.append(finalinput)
        print(f"{finalinput}", end='')
        fullinputstr = "".join(fullinput)
        wordinputs = fullinputstr.split()
        exportedinput = list(fullinputstr)
    return fullinput, fullinputstr, wordinputs, myinput, exportedinput


def run():
    fullinput, fullinputstr, wordinputs, myinput, exportedinput = main()
    def changewords():

        changeivalues = input("Would you like to change the words?")
        if changeivalues == 'yes':
            changedivalues = input(f"What word would you like to change?"
                                   f" (write down the word you want to change): {fullinputstr}\n")
            changeinput = input(f"What would you want to change {changedivalues} to: ")
            changedivalues = wordinputs.index(changedivalues)
            wordinputs[changedivalues] = changeinput
            print(" ".join(wordinputs))
        elif changeivalues == 'no':
            print()
        else:
            print("Answer with either yes or no")
            changewords()

    def changingphrase():
        txtstr1 = " ".join(wordinputs)
        txt = list(txtstr1)
        txtstr = "".join(txt)
        changeval = input("Would you like to change a phrase?")
        if changeval == "yes":
            changedphrase = input(f"What phrase would you like to change: {txtstr}\n")
            inputindex = txtstr.index(changedphrase)
            inputlength = len(changedphrase)
            myoutput = input(f"What would you like to change {changedphrase} to?\n")
            inputrange = (inputindex + inputlength)
            outputrange = (inputindex + len(myoutput))
            for i in range(inputindex, inputrange):
                txt[i] = ''
            for i, x in zip(range(inputindex, outputrange), myoutput):
                txt.insert(i, x)
            print("".join(txt))
        elif changeval == 'no':
            print()
        else:
            print("Answer with either yes or no")
            changingphrase()
        return txt
    def changingletters():
        txt = changingphrase()
        txtstr = "".join(txt)
        def changedletters():
            wanttochange = input("Do you want to change any letters")
            if wanttochange == "yes":
                changevalue = input("What letters do you want to change? \n")
                splittedchangevalue = list(changevalue)
                changingvalue = []
                finalvalue = ''
                for i in range(0, len(splittedchangevalue)):
                    if splittedchangevalue[i] in txt:
                        changingvalue.append(splittedchangevalue[i])
                    elif splittedchangevalue[i] not in txt:
                        print(f"'{splittedchangevalue[i]}' cannot be replaced. It is not part of your string.")
                        print("".join(txt))
                        changedletters()
                finalvalue = "".join(changingvalue)
                changedvalue = input(f"What would you like to change '{finalvalue}' letters to")
                for m, x in zip(changevalue, changedvalue):
                    for j in range(0, len(txt)):
                        if txt[j] == m:
                            txt[j] = x
            elif wanttochange == "no":
                print()
            else:
                print("Answer with either yes or no (lowercase)")
                changedletters()
            print("".join(txt))
        changedletters()
    changewords()
    changingletters()


run()
