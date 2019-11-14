def main():
    fullinput = []
    wordinputs = []
    fullinputstr = ''
    myinput = input("Type in your string \n")
    for i in myinput:
        asciimyinput = ''
        if 97 <= ord(i) <= 122:
            asciimyinput = ord(i) - 32
        else:
            asciimyinput = ord(i)
        finalinput = chr(asciimyinput)
        fullinput.append(finalinput)
        print(f"{finalinput}", end='')
        fullinputstr = "".join(fullinput)
        wordinputs = fullinputstr.split()
    print('\n')
    return fullinput, fullinputstr, wordinputs


def run():
    fullinput, fullinputstr, wordinputs = main()
    def changewords():
        finalvalue = []
        changeivalues = input("Would you like to change the words?\n").lower()
        if changeivalues == 'yes':
            changedivalues = input(f"What word would you like to change: {fullinputstr}\n")
            splittedchangedivalues = list(changedivalues)
            for i in range(0, len(splittedchangedivalues)):
                if splittedchangedivalues[i] not in list(fullinputstr):
                    print(f"'{splittedchangedivalues[i]}' cannot be replaced. It is not part of your string."
                          f" (Uppercase your characters)")
                else:
                    finalvalue.append(splittedchangedivalues[i])
            if "".join(finalvalue) != changedivalues:
                changewords()
            else:
                changeinput = input(f"What would you want to change {changedivalues} to \n")
                changedivalues = wordinputs.index(changedivalues)
                wordinputs[changedivalues] = changeinput
                print(" ".join(wordinputs))
        elif changeivalues == 'no':
            print()
        else:
            print("Answer with either 'yes' or 'no'")
            changewords()

    def changingphrase():
        txtstr1 = " ".join(wordinputs)
        txt = list(txtstr1)
        txtstr = "".join(txt)
        changeval = input("Would you like to change a phrase? \n").lower()
        if changeval == "yes":
            changedphrase = input(f"What phrase would you like to change: {txtstr}\n")
            splittedchangedphrase = list(changedphrase)
            changingval = []
            for i in range(0, len(splittedchangedphrase)):
                if splittedchangedphrase[i] not in txt:
                    print(f"'{splittedchangedphrase[i]}' cannot be replaced. It is not part of your string."
                          f" (Uppercase your characters)")
                else:
                    changingval.append(splittedchangedphrase[i])
            if "".join(changingval) != changedphrase:
                changingphrase()
            else:
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
            print("Answer with either 'yes' or 'no'")
            changingphrase()
        return txt
    def changingletters():
        txt = changingphrase()
        wanttochange = input("Do you want to change any letters \n").lower()
        def changedletters():
            if wanttochange == "yes":
                changevalue = input(f"What letters do you want to change? {''.join(txt)}\n")
                splittedchangevalue = list(changevalue)
                changingvalue = []
                changedvalue = []
                finalvalue = ''
                for i in range(0, len(splittedchangevalue)):
                    if splittedchangevalue[i] in txt:
                        changingvalue.append(splittedchangevalue[i])
                        currentvalue = input(f"What would you like to change '{splittedchangevalue[i]}' with? \n")
                        changedvalue.append(currentvalue)
                    elif splittedchangevalue[i] not in txt:
                        print(f"'{splittedchangevalue[i]}' cannot be replaced. It is not part of your string."
                              f" (Uppercase your characters)")
                finalvalue = "".join(changingvalue)
                if finalvalue != changevalue:
                    changedletters()
                else:
                    for m, x in zip(finalvalue, changedvalue):
                        for j in range(0, len(txt)):
                            if txt[j] == m:
                                txt[j] = x
                    print(f'Your replaced string: {"".join(txt)}')
            elif wanttochange == "no":
                print()
            else:
                print("Answer with either 'yes' or 'no'")
                changedletters()
        changedletters()
    changewords()
    changingletters()
    def newstrings():
        newstring = input("Do you want to translate a new string \n")
        if newstring == "yes":
            run()
        elif newstring == "no":
            print("Goodbye.")
        else:
            print("Answer with either yes or no")
            newstrings()
    newstrings()


if __name__ == '__main__':
    run()
