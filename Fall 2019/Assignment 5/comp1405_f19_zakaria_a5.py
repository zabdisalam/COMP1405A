def main():
    fullinput = []
    wordinputs = []
    fullinputstr = ''
    myinput = input("Type the string to be translated: \n")
    for i in myinput:
        asciimyinput = ''
        if 97 <= ord(i) <= 122:
            asciimyinput = ord(i) - 32
        else:
            asciimyinput = ord(i)
        finalinput = chr(asciimyinput)
        fullinput.append(finalinput)
        fullinputstr = "".join(fullinput)
        wordinputs = fullinputstr.split()
    print(f'String for translation: {fullinputstr}')
    return fullinput, fullinputstr, wordinputs


def run():
    fullinput, fullinputstr, wordinputs = main()
    def changewords():
        finalvalue = []
        changeivalues = input("Would you like to replace any of the words?:\n").lower()
        if changeivalues == 'yes':
            changedivalues = input(f"What word would you like to replace: {fullinputstr}\n")
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
                changeinput = input(f"What would you want to replace '{changedivalues}' with: \n")
                changedivalues = wordinputs.index(changedivalues)
                wordinputs[changedivalues] = changeinput
                print(f"After replacing words: {' '.join(wordinputs)}")
        elif changeivalues == 'no':
            print()
        else:
            print("Answer with either 'yes' or 'no'")
            changewords()

    def changingphrase():
        txtstr1 = " ".join(wordinputs)
        txt = list(txtstr1)
        txtstr = "".join(txt)
        changeval = input("Would you like to replace a phrase?: \n").lower()
        if changeval == "yes":
            changedphrase = input(f"What phrase would you like to replace: {txtstr}\n")
            splittedchangedphrase = changedphrase.split()
            joinedwordinputs = "".join(wordinputs)
            changingval = []
            if changedphrase not in " ".join(wordinputs):
                print(f"'{changedphrase}' cannot be replaced. It is not part of your string."
                      f" (Uppercase your characters)")
            else:
                changingval.append(changedphrase)
            if " ".join(changingval) != changedphrase:
                changingphrase()
            else:
                inputindex = txtstr.index(changedphrase)
                inputlength = len(changedphrase)
                myoutput = input(f"What would you like to replace '{changedphrase}' with?:\n")
                inputrange = (inputindex + inputlength)
                outputrange = (inputindex + len(myoutput))
                for i in range(inputindex, inputrange):
                    txt[i] = ''
                for i, x in zip(range(inputindex, outputrange), myoutput):
                    txt.insert(i, x)
                print(f"After replacing phrases: {''.join(txt)}")
        elif changeval == 'no':
            print()
        else:
            print("Answer with either 'yes' or 'no'")
            changingphrase()
        return txt
    def changingletters():
        txt = changingphrase()
        def changedletters():
            wanttochange = input("Do you want to replace any letters: \n").lower()
            if wanttochange == "yes":
                changevalue = input(f"What letters do you want to replace?: {''.join(txt)}\n")
                splittedchangevalue = list(changevalue)
                changingvalue = []
                changedvalue = []
                finalvalue = ''
                for i in range(0, len(splittedchangevalue)):
                    if splittedchangevalue[i] in txt:
                        changingvalue.append(splittedchangevalue[i])
                        currentvalue = input(f"What would you like to replace '{splittedchangevalue[i]}' with?: \n")
                        changedvalue.append(currentvalue)
                    elif splittedchangevalue[i] not in txt:
                        print(f"'{splittedchangevalue[i]}' cannot be replaced. It is not part of your string."
                              f" (Uppercase your characters)")
                        break
                finalvalue = "".join(changingvalue)
                if finalvalue != changevalue:
                    changedletters()
                else:
                    for m, x in zip(finalvalue, changedvalue):
                        for j in range(0, len(txt)):
                            if txt[j] == m:
                                txt[j] = x
                    print(f'After replacing letters: {"".join(txt)}')
            elif wanttochange == "no":
                print()
            else:
                print("Answer with either 'yes' or 'no'")
                changedletters()
            print(f'Your translated string: {"".join(txt)}')
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
